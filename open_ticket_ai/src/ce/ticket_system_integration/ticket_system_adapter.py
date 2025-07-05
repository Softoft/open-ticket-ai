# FILE_PATH: open_ticket_ai\src\ce\ticket_system_integration\ticket_system_adapter.py
from abc import ABC, abstractmethod

from injector import inject

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import (
    Providable,
)
from .unified_models import (
    SearchCriteria,
    UnifiedNote,
    UnifiedTicket,
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
    async def update_ticket(self, ticket_id: str, updates: dict) -> bool:
        """Update a ticket in the system.

        This method must be implemented by concrete adapters to handle updating
        ticket attributes in the target ticketing system. It should support partial
        updates and return the updated ticket representation.

        Args:
            ticket_id: Unique identifier of the ticket to update.
            updates: Dictionary of attributes to update on the ticket.

        Returns:
            bool: ``True`` if the update succeeded, otherwise ``False``.
        """
        pass

    @abstractmethod
    async def find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]:
        """Search for tickets matching ``criteria``.

        This method must be implemented by concrete adapters to perform
        complex searches against the target ticketing system. The query
        structure is adapter-specific but should support common filtering
        and search operations.

        Args:
            criteria: Parameters defining which tickets to search for.

        Returns:
            list[UnifiedTicket]:
                A list of tickets that match the criteria.
                Returns an empty list if no matches are found.
        """
        pass

    @abstractmethod
    async def find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None:
        """Return the first ticket that matches ``criteria`` if any.

        This is a convenience method that should return the first matching
        ticket from a search operation. It should optimize for performance
        by limiting results internally.

        Args:
            criteria: Parameters defining which ticket to search for.

        Returns:
            Optional[UnifiedTicket]:
                The first matching ticket or ``None`` if no tickets match.
        """
        pass

    @abstractmethod
    async def create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket:
        """Create a new ticket in the system.

        This method must be implemented by concrete adapters to handle ticket creation
        in the target ticketing system. The ticket data is provided in a unified format.

        Args:
            ticket_data (UnifiedTicket): 
                The ticket data to create. Contains all necessary fields in a 
                system-agnostic format.

        Returns:
            UnifiedTicket: 
                The created ticket object with system-generated identifiers and fields.
        """
        pass

    @abstractmethod
    async def add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote:
        """Add a note to an existing ticket.

        This method must be implemented by concrete adapters to attach notes/comments
        to tickets in the target system. The note content is provided in a unified format.

        Args:
            ticket_id (str): 
                Unique identifier of the target ticket.
            note (UnifiedNote): 
                The note content and metadata to add.

        Returns:
            UnifiedNote: 
                The added note object with system-generated metadata (e.g., timestamp, ID).
        """
        pass