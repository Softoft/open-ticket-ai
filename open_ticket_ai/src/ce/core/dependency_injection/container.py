import os

from injector import Binder, Injector, Module, provider, singleton
from otobo import AuthData, OTOBOClient, OTOBOClientConfig, TicketOperation

from open_ticket_ai.src.ce.core import AbstractContainer, Registry, create_registry
from open_ticket_ai.src.ce.core.config.config_models import (
    AttributePredictorConfig,
    OpenTicketAIConfig,
    RegistryInstanceConfig,
    load_config,
)
from open_ticket_ai.src.ce.core.config.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.src.ce.core.util.path_util import find_project_root
from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.src.ce.run.orchestrator import Orchestrator
from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter_config import OTOBOAdapterConfig
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
)

CONFIG_PATH = os.getenv('OPEN_TICKET_AI_CONFIG', find_project_root() / 'config.yml')


class AppModule(Module):
    """Injector module that binds the validated configuration."""

    def configure(self, binder: Binder):
        """Bind core configuration objects."""
        open_ticket_ai_config = load_config(CONFIG_PATH)
        registry = create_registry()
        binder.bind(OpenTicketAIConfig, to=open_ticket_ai_config, scope=singleton)
        binder.bind(Registry, to=registry, scope=singleton)

    @provider
    @singleton
    def provide_validator(
            self,
            config: OpenTicketAIConfig,
            registry: Registry
    ) -> OpenTicketAIConfigValidator:
        """Provide a configuration validator instance."""
        return OpenTicketAIConfigValidator(config, registry)

    @provider
    @singleton
    def provide_otobo_client(self, config: OpenTicketAIConfig) -> OTOBOClient:
        """Create an :class:`OTOBOClient` using the system configuration."""
        otobo_config = OTOBOAdapterConfig.model_validate(config.system.params)
        return OTOBOClient(
            config=OTOBOClientConfig(
                base_url=otobo_config.server_address,
                service=otobo_config.service_name,
                auth=AuthData(
                    UserLogin=otobo_config.user,
                    Password=otobo_config.password
                ),
                operations={
                    TicketOperation.SEARCH.value: otobo_config.search_operation_url,
                    TicketOperation.GET.value: otobo_config.get_operation_url,
                    TicketOperation.UPDATE.value: otobo_config.update_operation_url,
                }
            )
        )

class DIContainer(Injector, AbstractContainer):
    """Dependency injection container for Open Ticket AI."""

    def __init__(self):
        """Initialize the container and bind common instances."""
        super().__init__([AppModule()])
        self.config: OpenTicketAIConfig = self.get(OpenTicketAIConfig)
        self.registry = self.get(Registry)

        self.binder.bind(TicketSystemAdapter, to=self.get_system(), scope=singleton)
        self.binder.bind(Orchestrator, to=Orchestrator(self.config, self), scope=singleton)

    def _get_instance[T](self, id: str, subclass_of: type[T],
                         config_list: list[RegistryInstanceConfig]) -> T:
        """Return an instance from the registry.

        Args:
            id: Identifier of the desired instance.
            subclass_of: Expected base class of the instance.
            config_list: List of configuration entries to search in.

        Returns:
            The created instance of ``subclass_of``.
        """
        instance_config = next((c for c in config_list if c.id == id), None)
        if not instance_config:
            raise KeyError(f"Unknown instance ID: {id}")
        instance_class = self.registry.get(instance_config.provider_key, subclass_of)
        if not instance_class:
            raise KeyError(f"Unknown provider key: {instance_config.provider_key}")
        return self.create_object(instance_class, additional_kwargs={"config":instance_config})

    def get_system(self) -> TicketSystemAdapter:
        """Return the configured ticket system adapter."""
        return self.create_object(self.registry.get(self.config.system.provider_key, TicketSystemAdapter))

    def get_fetcher(self, fetcher_id: str) -> DataFetcher:
        """Instantiate a data fetcher by its ID."""
        return self._get_instance(
            fetcher_id,
            DataFetcher,
            self.config.fetchers
        )

    def get_preparer(self, preparer_key: str) -> DataPreparer:
        """Instantiate a preparer by its ID."""
        return self._get_instance(
            preparer_key,
            DataPreparer,
            self.config.data_preparers
        )

    def get_ai_inference_service(self, inference_service_id: str) -> AIInferenceService:
        """Instantiate an AI inference service by its ID."""
        return self._get_instance(
            inference_service_id,
            AIInferenceService,
            self.config.ai_inference_services
        )

    def get_modifier(self, modifier_id: str) -> Modifier:
        """Instantiate a modifier by its ID."""
        return self._get_instance(
            modifier_id,
            Modifier,
            self.config.modifiers
        )

    def get_predictor(self, predictor_id: str) -> AttributePredictor:
        """Create an attribute predictor instance by its ID."""
        try:
            predictor_config: AttributePredictorConfig = next(
                (p for p in self.config.attribute_predictors if p.id == predictor_id),
                None
            )
            pred_fetcher = self.get_fetcher(predictor_config.fetcher_id)
            pred_preparer = self.get_preparer(predictor_config.preparer_id)
            pred_ai_inference_service = self.get_ai_inference_service(predictor_config.ai_inference_service_id)
            pred_modifier = self.get_modifier(predictor_config.modifier_id)

            predictor_class: AttributePredictor = self.registry.get(predictor_config.provider_key, AttributePredictor)
        except KeyError:
            raise KeyError(f"Unknown predictor key: {predictor_config.provider_key}")
        return predictor_class(
            config=predictor_config,
            fetcher=pred_fetcher,
            preparer=pred_preparer,
            ai_inference_service=pred_ai_inference_service,
            modifier=pred_modifier
        )
