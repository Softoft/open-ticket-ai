import os

from injector import Binder, Injector, Module, provider, singleton
from otobo import OTOBOClient, OTOBOClientConfig, AuthData, TicketOperation

from open_ticket_ai.src.ce.core.config.config_models import (
    OpenTicketAIConfig,
    load_config, PipelineConfig,
)
from open_ticket_ai.src.ce.core.config.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.src.ce.core.dependency_injection.abstract_container import AbstractContainer
from open_ticket_ai.src.ce.core.dependency_injection.create_registry import create_registry
from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry
from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance
from open_ticket_ai.src.ce.core.util.path_util import find_project_root
from open_ticket_ai.src.ce.run.orchestrator import Orchestrator
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.pipeline import Pipeline
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
        binder.bind(Orchestrator, to=Orchestrator, scope=singleton)

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
        # noinspection PyArgumentList
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

        system_adapter_class = self.registry.get_type_from_key(self.config.system.provider_key)
        system_adapter_instance = self.create_object(
            system_adapter_class,
            additional_kwargs={"config": self.config.system}
        )
        self.binder.bind(TicketSystemAdapter, to=system_adapter_instance, scope=singleton)

    def get_instance_config(self, id: str):
        """Retrieve the configuration for a specific instance by its ID.

        Args:
            id: The unique identifier of the instance configuration to retrieve.

        Returns:
            The configuration object for the specified instance.

        Raises:
            KeyError: If no configuration is found for the given ID.
        """
        instance_config = next(
            (c for c in self.config.get_all_register_instance_configs() if c.id == id), None)
        if not instance_config:
            raise KeyError(f"Unknown instance ID: {id}")
        return instance_config

    def get_instance[T: RegistryProvidableInstance](self, id: str, subclass_of: type[T]) -> T:
        """Return an instance from the registry.

        Args:
            id: Identifier of the desired instance.
            subclass_of: Expected base class of the instance.
            config_list: List of configuration entries to search in.

        Returns:
            The created instance of ``subclass_of``.
        """
        instance_config = self.get_instance_config(id)
        instance_class = self.registry.get(instance_config.provider_key, subclass_of)
        if not instance_class:
            raise KeyError(f"Unknown provider key: {instance_config.provider_key}")
        return self.create_object(instance_class, additional_kwargs={"config": instance_config})

    def get_pipeline(self, predictor_id: str) -> Pipe:
        """Create an attribute predictor instance by its ID."""
        predictor_config: PipelineConfig | None = None
        try:
            predictor_config = self.get_instance_config(predictor_id)
            pipe_instances = [
                self.get_instance(pipe_id, Pipe)
                for pipe_id in predictor_config.pipes
            ]

            predictor_class: type[Pipeline] = self.registry.get(predictor_config.provider_key, Pipe)
        except KeyError:
            if predictor_config:
                raise KeyError(f"Unknown predictor key: {predictor_config.provider_key}")
            raise KeyError(f"Unknown predictor ID: {predictor_id}")
        return predictor_class(
            config=predictor_config,
            pipes=pipe_instances
        )