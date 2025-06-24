from inspect import cleandoc

from injector import inject

from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry
from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.mixins.registry_validation_mixin import Registerable
from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer


class OpenTicketAIConfigValidator:
    """Validate configuration values against the registry."""
    @inject
    def __init__(self, config: OpenTicketAIConfig, registry: Registry):
        """Create a new validator.

        Args:
            config: Loaded ``OpenTicketAIConfig`` instance.
            registry: Registry containing available classes.
        """
        self.config = config
        self.registry = registry

    def validate_registry(self) -> None:
        """Ensure all configured providers are registered."""
        registry_provider_types: dict[type, list[Registerable]] = {
            DataFetcher: self.config.fetchers,
            DataPreparer: self.config.data_preparers,
            AIInferenceService: self.config.ai_inference_services,
            Modifier: self.config.modifiers,
            AttributePredictor: self.config.attribute_predictors
        }
        for provider_type, configs in registry_provider_types.items():
            for config in configs:
                if not self.registry.contains(config.provider_key, provider_type):
                    raise ValueError(cleandoc(f"""
                        Registry does not contain required {provider_type.__name__} with id '{config.id}'
                        There are following registered providers
                        {self.registry.get_registry_types_descriptions(subclass_of=provider_type)}
                        """))
