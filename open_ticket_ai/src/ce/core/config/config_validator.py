"""Module for validating OpenTicketAI configuration against a registry.

This module provides the `OpenTicketAIConfigValidator` class which validates
that all provider configurations reference registered providers in the registry.
It ensures the application configuration only uses available implementations
during runtime initialization.

Example:
    Typical usage involves injecting dependencies and calling validation:

    ```python
    validator = OpenTicketAIConfigValidator(config, registry)
    validator.validate_registry()
    ```

Raises:
    ValueError: If any configured provider is not found in the registry,
        including details of missing IDs and available providers.
"""
from inspect import cleandoc

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry

class OpenTicketAIConfigValidator:
    """Validate configuration values against the registry.

    This class performs validation checks to ensure all provider configurations
    specified in the application settings correspond to registered implementations
    in the dependency injection registry.

    Attributes:
        config (OpenTicketAIConfig): Loaded application configuration.
        registry (Registry): Dependency injection registry containing provider mappings.
    """

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
        """Ensure all configured providers are registered.

        Iterates through all provider configurations in the application settings
        and verifies each provider key exists in the registry. Raises a detailed
        error if any provider is missing.

        Raises:
            ValueError: If any provider configuration references an unregistered
                provider key. The error message includes:
                - Missing provider ID
                - Descriptions of currently registered providers
        """
        configs = self.config.get_all_register_instance_configs()
        for config in configs:
            if not self.registry.contains(config.provider_key):
                raise ValueError(cleandoc(f"""
                    Registry does not contain required Provider with id
                    '{config.id}'
                    There are following registered providers
                    {self.registry.get_registry_types_descriptions()}
                    """))