import logging

from injector import inject
from rich.console import Console

from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.core.util.pretty_print_config import pretty_print_config


class RegistryProvidableInstance:

    @inject
    def __init__(self, config: RegistryInstanceConfig, console: Console | None = None):
        """Store the configuration and pretty print it."""
        self.console = console or Console()
        self.config = config
        logger = logging.getLogger(__name__)
        logger.info(f"Initializing {self.__class__.__name__} with config:")
        self._pretty_print()

    def _pretty_print(self):
        """Pretty print the configuration of the class."""
        pretty_print_config(self.config, self.console)

    @classmethod
    def get_provider_key(cls) -> str:
        """
        Return the provider key for the class.

        This key is used to register and retrieve instances from the registry.
        """
        return cls.__name__

    @staticmethod
    def get_description() -> str:
        """Return a human readable description for the class."""
        return "No description provided."
