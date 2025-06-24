from inspect import cleandoc

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry

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
        configs = self.config.get_all_register_instance_configs()
        for config in configs:
            if not self.registry.contains(config.provider_key):
                raise ValueError(cleandoc(f"""
                    Registry does not contain required Provider with id
                    '{config.id}'
                    There are following registered providers
                    {self.registry.get_registry_types_descriptions()}
                    """))