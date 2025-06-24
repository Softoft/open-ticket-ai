from abc import ABC, abstractmethod

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig


class TicketSystemAdapter(RegistryInstanceConfig, ABC):
    """
    An abstract base class for ticket system adapters.
    This class defines the
    interface that all ticket system adapters must implement.
    """

    @inject
    def __init__(self, config: SystemConfig):
        """Initialize the adapter with system configuration."""

        super().__init__(config)
        self.config = config

    @abstractmethod
    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        """Update a ticket in the system.

        Args:
            ticket_id: Ticket identifier.
            data: Attributes to update.

        Returns:
            Optional[dict]: Updated ticket information.
        """
        pass

    @abstractmethod
    async def find_tickets(self, query: dict) -> list[dict]:
        """Search for tickets matching ``query``.

        Args:
            query: Search parameters for the ticket system.

        Returns:
            list[dict]: Matching tickets.
        """
        pass

    @abstractmethod
    async def find_first_ticket(self, query: dict) -> dict | None:
        """Return the first ticket that matches ``query`` if any."""
        pass
