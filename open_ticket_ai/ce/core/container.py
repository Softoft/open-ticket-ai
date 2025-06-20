import os

from injector import Injector, Module, Binder, singleton, provider

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig, load_config
from open_ticket_ai.ce.core.config_validator import OpenTicketAIConfigValidator
from open_ticket_ai.ce.core.create_registry import create_registry
from open_ticket_ai.ce.core.registry import Registry
from open_ticket_ai.ce.core.util.path_util import find_project_root
from open_ticket_ai.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.ce.run.modifiers.modifier import Modifier
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


class DIContainer(Injector):
    def __init__(self):
        super().__init__([AppModule()])
        self.config: OpenTicketAIConfig = self.get(OpenTicketAIConfig)
        self.registry = self.get(Registry)

    def get_system(self) -> TicketSystemAdapter:
        """
        Get the system configuration.
        """
        return self.create_object(self.registry.get(self.config.system.provider_key, TicketSystemAdapter))

    def get_fetcher(self, fetcher_key: str) -> DataFetcher:
        try:
            fetcher_class = self.registry.get(fetcher_key, DataFetcher)
        except KeyError:
            raise KeyError(f"Unknown fetcher key: {fetcher_key}")
        return self.create_object(fetcher_class)

    def get_preparer(self, preparer_key: str) -> DataPreparer:
        try:
            preparer_class = self.registry.get(preparer_key, DataPreparer)
        except KeyError:
            raise KeyError(f"Unknown preparer key: {preparer_key}")
        return self.create_object(preparer_class)

    def get_ai_inference_service(self, model_key: str) -> AIInferenceService:
        try:
            ai_model_class = self.registry.get(model_key, AIInferenceService)
        except KeyError:
            raise KeyError(f"Unknown model key: {model_key}")
        return self.create_object(ai_model_class)

    def get_modifier(self, modifier_key: str) -> Modifier:
        try:
            modifier_class = self.registry.get(modifier_key, Modifier)
        except KeyError:
            raise KeyError(f"Unknown modifier key: {modifier_key}")
        return self.create_object(modifier_class)

    def get_predictor(self, predictor_key: str) -> AttributePredictor:
        try:
            predictor_class = self.registry.get(predictor_key, AttributePredictor)
        except KeyError:
            raise KeyError(f"Unknown predictor key: {predictor_key}")
        return self.create_object(predictor_class)
