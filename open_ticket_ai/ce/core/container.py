import os
from typing import Any

from injector import Injector, Module, Binder, singleton

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig, load_config
# Registries
from open_ticket_ai.ce.core.registry import (
    TICKET_SYSTEM_ADAPTER_REGISTRY,
    FETCHER_REGISTRY,
    PREPARER_REGISTRY,
    MODEL_REGISTRY,
    ATTRIBUTE_PREDICTOR_REGISTRY,
    MODIFIER_REGISTRY,
)
from open_ticket_ai.ce.core.util.path_util import find_project_root
from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
# Base interfaces
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer

CONFIG_PATH = os.getenv('OPEN_TICKET_AI_CONFIG', find_project_root() / 'config.yml')


class AppModule(Module):
    """
    DI module: binds only the validated config as singleton.
    """

    def configure(self, binder: Binder):
        open_ticket_ai_config = load_config(CONFIG_PATH)
        binder.bind(OpenTicketAIConfig, to=open_ticket_ai_config, scope=singleton)


class DIContainer:
    """
    Simplified DI container using Injector for config+object construction.
    Components are resolved directly from registries without dynamic imports.
    """

    def __init__(self):
        self.injector = Injector([AppModule()])
        # pre-load config
        self.config: OpenTicketAIConfig = self.injector.get(OpenTicketAIConfig)

    def get_system(self):
        """
        Get the system configuration.
        """
        return self.injector.create_object(TICKET_SYSTEM_ADAPTER_REGISTRY[self.config.system.type])

    def get_fetcher(self, fetcher_key: str) -> DataFetcher:
        try:
            fetcher_class = FETCHER_REGISTRY[fetcher_key]
        except KeyError:
            raise KeyError(f"Unknown fetcher key: {fetcher_key}")
        return self.injector.create_object(fetcher_class)

    def get_preparer(self, preparer_key: str) -> DataPreparer:
        try:
            preparer_class = PREPARER_REGISTRY[preparer_key]
        except KeyError:
            raise KeyError(f"Unknown preparer key: {preparer_key}")
        return self.injector.create_object(preparer_class)

    def get_ai_model(self, model_key: str) -> Any:
        try:
            ai_model_class = MODEL_REGISTRY[model_key]
        except KeyError:
            raise KeyError(f"Unknown model key: {model_key}")
        return self.injector.create_object(ai_model_class)

    def get_modifier(self, modifier_key: str) -> Modifier:
        try:
            modifier_class = MODIFIER_REGISTRY[modifier_key]
        except KeyError:
            raise KeyError(f"Unknown modifier key: {modifier_key}")
        return self.injector.create_object(modifier_class)

    def get_predictor(self, predictor_key: str) -> AttributePredictor:
        try:
            predictor_class = ATTRIBUTE_PREDICTOR_REGISTRY[predictor_key]
        except KeyError:
            raise KeyError(f"Unknown predictor key: {predictor_key}")
        return self.injector.create_object(predictor_class)


# Example usage
if __name__ == '__main__':
    container = DIContainer()
    cfg = container.config
    print('Configured system:', cfg.system.id)

    # Instantiate all registered components
    for key, cls in FETCHER_REGISTRY.items():
        print('Fetcher:', key, '->', container.get_fetcher(key))

    for key, cls in PREPARER_REGISTRY.items():
        print('Preparer:', key, '->', container.get_preparer(key))

    for key, cls in MODEL_REGISTRY.items():
        print('Model:', key, '->', container.get_ai_model(key))

    for key, cls in MODIFIER_REGISTRY.items():
        print('Modifier:', key, '->', container.get_modifier(key))

    for key, cls in ATTRIBUTE_PREDICTOR_REGISTRY.items():
        print('Predictor:', key, '->', container.get_predictor(key))
