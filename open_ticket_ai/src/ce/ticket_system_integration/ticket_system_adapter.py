# FILE_PATH: open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py
from abc import ABC, abstractmethod

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import (
    Providable,
)


class TicketSystemAdapter(Providable, ABC):
    """
    An abstract base class for ticket system adapters.

    This class defines the interface that all concrete ticket system adapters must
    implement to interact with different ticketing systems. It provides common
    configuration handling through dependency injection and requires subclasses
    to implement core ticket operations.

    Attributes:
        config (SystemConfig): System configuration object containing adapter settings.
    """

    @inject
    def __init__(self, config: SystemConfig):
        """Initialize the adapter with system configuration.

        This constructor is automatically injected with the system configuration
        using the dependency injection framework. It initializes the adapter
        with the provided configuration and ensures proper setup of inherited
        components.

        Args:
            config (SystemConfig): The system configuration object containing
                all necessary settings and parameters for the adapter.
        """

        super().__init__(config)
        self.config = config

    @abstractmethod
    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        """Update a ticket in the system.

        This method must be implemented by concrete adapters to handle updating
        ticket attributes in the target ticketing system. It should support partial
        updates and return the updated ticket representation.

        Args:
            ticket_id: Unique identifier of the ticket to update.
            data: Dictionary of attributes to update on the ticket.

        Returns:
            Optional[dict]:
                The updated ticket object as a dictionary if successful,
                or None if the update failed or the ticket wasn't found.
        """
        pass

    @abstractmethod
    async def find_tickets(self, query: dict) -> list[dict]:
        """Search for tickets matching ``query``.

        This method must be implemented by concrete adapters to perform
        complex searches against the target ticketing system. The query
        structure is adapter-specific but should support common filtering
        and search operations.

        Args:
            query: Dictionary representing the search parameters and filters.

        Returns:
            list[dict]:
                A list of ticket objects (as dictionaries) that match the query.
                Returns an empty list if no matches are found.
        """
        pass

    @abstractmethod
    async def find_first_ticket(self, query: dict) -> dict | None:
        """Return the first ticket that matches ``query`` if any.

        This is a convenience method that should return the first matching
        ticket from a search operation. It should optimize for performance
        by limiting results internally.

        Args:
            query: Dictionary representing the search parameters and filters.

        Returns:
            Optional[dict]:
                The first matching ticket object as a dictionary,
                or None if no tickets match the query.
        """
        pass
