from abc import ABC, abstractmethod

from injector import inject

from open_ticket_ai.ce.core.config_models import SystemConfig
from open_ticket_ai.ce.core.mixins.configurable_mixin import ConfigurableMixin
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class TicketSystemAdapter(ConfigurableMixin, DescriptionMixin, ABC):
    """
    An abstract base class for ticket system adapters.
    This class defines the
    interface that all ticket system adapters must implement.
    """

    @inject
    def __init__(self, config: SystemConfig):
        super().__init__(config)
        self.config = config

    @abstractmethod
    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        """
        Update a ticket in the ticket system.

        :param ticket_id: The ID of the ticket to update.
        :param data: A dictionary containing the data to update the ticket with.
        """
        pass

    @abstractmethod
    async def find_tickets(self, query: dict) -> list[dict]:
        """
        Search for tickets in the ticket system.

        :param query: A dictionary containing the search parameters.
        :return: A list of dictionaries containing the matching tickets.
        """
        pass

    @abstractmethod
    async def find_first_ticket(self, query: dict) -> dict | None:
        """
        Find the first ticket matching the search query.

        :param query: The search parameters to filter tickets.
        :return: The first matching ticket or None if no tickets found.
        """
        pass
