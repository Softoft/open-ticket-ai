from abc import ABC

from injector import inject

from open_ticket_ai.ce.core.config_models import OpenTicketAIConfig
from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin


class TicketSystemAdapter(DescriptionMixin, ABC):
    """
    An abstract base class for ticket system adapters.
    This class defines the
    interface that all ticket system adapters must implement.
    """

    @inject
    def __init__(self, config: OpenTicketAIConfig):
        self.config = config

    def update_ticket(self, ticket_id: str, data: dict) -> None:
        """
        Update a ticket in the ticket system.

        :param ticket_id: The ID of the ticket to update.
        :param data: A dictionary containing the data to update the ticket with.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def fetch_ticket(self, ticket_id: str) -> dict:
        """
        Fetch a ticket from the ticket system.

        :param ticket_id: The ID of the ticket to fetch.
        :return: A dictionary containing the ticket data.
        """
        raise NotImplementedError("Subclasses must implement this method.")
