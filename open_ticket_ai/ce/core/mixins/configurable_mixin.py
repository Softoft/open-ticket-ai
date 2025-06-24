import logging

from pydantic import BaseModel

from open_ticket_ai.ce.core.util.pretty_print_config import pretty_print_config


class ConfigurableMixin:
    """
    Mixin class to provide a method for getting the configuration of a class.
    """

    def __init__(self, config: BaseModel):
        """Store the configuration and pretty print it."""

        logger = logging.getLogger(__name__)
        logger.info(f"Initializing {self.__class__.__name__} with config:")
        pretty_print_config(config)
