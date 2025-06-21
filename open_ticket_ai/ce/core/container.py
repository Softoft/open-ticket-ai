import os

from injector import Injector, Module, Binder, singleton, provider

from open_ticket_ai.ce.core.abstract_container import AbstractContainer
from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig, load_config, AttributePredictorConfig, \
    RegistryInstanceConfig
from open_ticket_ai.ce.core.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.ce.core.create_registry import create_registry
from open_ticket_ai.ce.core.registry import Registry
from open_ticket_ai.ce.core.util.path_util import find_project_root
from open_ticket_ai.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.ce.run.orchestrator import Orchestrator
from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter

CONFIG_PATH = os.getenv('OPEN_TICKET_AI_CONFIG', find_project_root() / 'config.yml')


class AppModule(Module):
    """
    DI module: binds only the validated config as singleton.
    """

    def configure(self, binder: Binder):
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
        return OpenTicketAIConfigValidator(config, registry)


class DIContainer(Injector, AbstractContainer):

    def __init__(self):
        super().__init__([AppModule()])
        self.config: OpenTicketAIConfig = self.get(OpenTicketAIConfig)
        self.registry = self.get(Registry)
        self.binder.bind(TicketSystemAdapter, to=self.get_system(), scope=singleton)
        self.binder.bind(Orchestrator, to=Orchestrator(self.config, self), scope=singleton)

    def _get_instance[T](self, id: str, subclass_of: type[T],
                         config_list: list[RegistryInstanceConfig]) -> T:
        """
        Get an instance from the registry by ID and subclass type.
        TODO: fix this use factory mehod, dont bind binder isnt working because it doesnt override previous bounded
        """
        instance_config = next((c for c in config_list if c.id == id), None)
        if not instance_config:
            raise KeyError(f"Unknown instance ID: {id}")
        self.binder.bind(type(instance_config), instance_config, scope=singleton)
        instance_class = self.registry.get(instance_config.provider_key, subclass_of)
        if not instance_class:
            raise KeyError(f"Unknown provider key: {instance_config.provider_key}")
        return instance_class(config=instance_config, ticket_system_adapter=self.get(TicketSystemAdapter))

    def get_system(self) -> TicketSystemAdapter:
        """
        Get the system configuration.
        """
        return self.create_object(self.registry.get(self.config.system.provider_key, TicketSystemAdapter))

    def get_fetcher(self, fetcher_id: str) -> DataFetcher:
        return self._get_instance(
            fetcher_id,
            DataFetcher,
            self.config.fetchers
        )

    def get_preparer(self, preparer_key: str) -> DataPreparer:
        return self._get_instance(
            preparer_key,
            DataPreparer,
            self.config.data_preparers
        )

    def get_ai_inference_service(self, inference_service_id: str) -> AIInferenceService:
        return self._get_instance(
            inference_service_id,
            AIInferenceService,
            self.config.ai_inference_services
        )

    def get_modifier(self, modifier_id: str) -> Modifier:
        return self._get_instance(
            modifier_id,
            Modifier,
            self.config.modifiers
        )

    def get_predictor(self, predictor_id: str) -> AttributePredictor:
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
