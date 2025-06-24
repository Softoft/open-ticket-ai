import logging

from injector import inject
from pydantic import BaseModel
from rich.console import Console

from open_ticket_ai.src.ce.core.util.pretty_print_config import pretty_print_config


class ConfigurableMixin:
    """
    Mixin class to provide a method for getting the configuration of a class.
    """

    @inject
    def __init__(self, config: BaseModel, console: Console | None = None):
        """Store the configuration and pretty print it."""
        self.console = console or Console()
        self.config = config
        logger = logging.getLogger(__name__)
        logger.info(f"Initializing {self.__class__.__name__} with config:")
        pretty_print_config(config)

    def _pretty_print(self):
        """Pretty print the configuration of the class."""

