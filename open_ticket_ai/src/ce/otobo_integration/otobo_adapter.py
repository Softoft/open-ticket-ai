"""
This module provides an adapter for integrating with the OTOBO ticket system.

The `OTOBOAdapter` class implements the `TicketSystemAdapter` interface to enable
seamless interaction with OTOBO's ticketing API. It handles operations such as:

- Searching for tickets based on custom queries
- Retrieving specific ticket details
- Updating existing ticket records

The adapter uses dependency injection for configuration and client management,
ensuring flexibility and testability.
"""

from injector import inject
from otobo import (
    OTOBOClient,
    TicketCreateParams,
    TicketSearchParams,
    TicketUpdateParams,
)
from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
)
from .unified_models import (
    SearchCriteria,
    UnifiedNote,
    UnifiedTicket,
    UnifiedQueue,
    UnifiedPriority,
    UnifiedStatus,
    UnifiedUser,
)


class OTOBOAdapter(TicketSystemAdapter):
    """Adapter for integrating with the OTOBO ticket system.

    Implements the `TicketSystemAdapter` interface to provide methods for:
    - Searching tickets using custom queries
    - Retrieving ticket details
    - Updating ticket records

    Attributes:
        otobo_client (OTOBOClient): Client instance for interacting with the OTOBO API.
    """

    @staticmethod
    def get_description() -> str:
        """Return a description of the adapter's functionality.

        Returns:
            str: A description of the OTOBO adapter.
        """
        return "Adapter for OTOBO ticket system integration, providing methods to retrieve and update tickets."

    @inject
    def __init__(self, config: SystemConfig, otobo_client: OTOBOClient):
        """Initialize the OTOBO adapter with configuration and client.

        Args:
            config (SystemConfig): System configuration object containing necessary settings.
            otobo_client (OTOBOClient): Pre-configured client for interacting with the OTOBO API.
        """
        super().__init__(config)
        self.otobo_client = otobo_client

    async def find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]:
        """Search for tickets matching the provided criteria.

        Converts the query dictionary into `TicketSearchParams` and uses the OTOBO client
        to retrieve matching tickets. Returns ticket data as dictionaries.

        Args:
            criteria: Search parameters describing the desired tickets.

        Returns:
            list[UnifiedTicket]: A list of matching tickets. Returns an empty list if none are found.

        Example:
            ```python
            await adapter.find_tickets({"Title": "Server Issue"})
            ```
            [{"TicketID": 123, "Title": "Server Issue", ...}, ...]
        """
        query: dict = {}
        if criteria.id:
            query["TicketID"] = criteria.id
        if criteria.subject:
            query["Title"] = criteria.subject

        result = await self.otobo_client.search_and_get(query=TicketSearchParams(**query))
        tickets: list[UnifiedTicket] = []
        for ticket in result.Ticket:
            tickets.append(
                UnifiedTicket(
                    id=str(ticket.TicketID),
                    subject=ticket.Title,
                    body="",
                    custom_fields={},
                    queue=UnifiedQueue(name=ticket.Queue),
                    priority=UnifiedPriority(name=ticket.Priority),
                    status=UnifiedStatus(name=ticket.State),
                    owner=UnifiedUser(name=ticket.Owner),
                    notes=[],
                )
            )
        return tickets

    async def find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None:
        """Retrieve the first ticket matching the search criteria.

        Uses `find_tickets` to get all matching tickets and returns the first result if available.

        Args:
            criteria: Search parameters formatted as a :class:`SearchCriteria` instance.

        Returns:
            Optional[UnifiedTicket]: The first matching ticket or ``None`` if nothing was found.

        Example:
            ```python
            await adapter.find_first_ticket({"State": "open"})
            ```
            {"TicketID": 456, "State": "open", ...}
        """
        result = await self.find_tickets(criteria)
        return result[0] if len(result) >= 1 else None

    async def update_ticket(self, ticket_id: str, updates: dict) -> bool:
        """Update a ticket record with new data.

        Validates and merges the ticket ID with update data into `TicketUpdateParams`,
        then sends the update request to the OTOBO API.

        Args:
            ticket_id (str): Identifier of the ticket to update.
            updates (dict): Key-value pairs representing fields to update and their new values.

        Returns:
            bool: ``True`` if the update was successful.

        Raises:
            ValidationError: If `updates` contains invalid fields or values for ticket update.

        Example:
            ```python
            success = await adapter.update_ticket("789", {"Priority": "high"})
            # success will be True if the update was successful
            ```
        """
        update_params: TicketUpdateParams = TicketUpdateParams.model_validate(
            {
                "TicketID": ticket_id,
                **updates,
            }
        )
        await self.otobo_client.update_ticket(payload=update_params)
        return True

    async def create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket:
        """Create a ticket in OTOBO from a UnifiedTicket instance.

        Converts the provided `UnifiedTicket` into `TicketCreateParams` and sends the creation request
        to the OTOBO API. The returned ticket will have the `id` field updated to the ID assigned by OTOBO.

        Args:
            ticket_data (UnifiedTicket): The ticket data to create.

        Returns:
            UnifiedTicket: The created ticket data with the `id` field updated to the new ticket ID.

        Example:
            ```python
            ticket = UnifiedTicket(subject="New Issue", ...)
            created_ticket = await adapter.create_ticket(ticket)
            print(created_ticket.id)  # Outputs the new ticket ID
            ```
        """
        payload = TicketCreateParams(
            Title=ticket_data.subject,
            Queue=ticket_data.queue.name,
            Priority=ticket_data.priority.name,
            State=ticket_data.status.name,
        )
        result = await self.otobo_client.create_ticket(payload=payload)
        return ticket_data.model_copy(update={"id": str(result.TicketID)})

    async def add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote:
        """Add a note to a ticket.

        Note: The public OTOBO client does not currently expose an endpoint for creating articles (notes).
        Therefore, this method does not actually create a note in OTOBO and instead returns the provided note.

        Args:
            ticket_id (str): The ID of the ticket to which the note should be added.
            note (UnifiedNote): The note to add.

        Returns:
            UnifiedNote: The same note that was passed in.

        Example:
            ```python
            note = UnifiedNote(content="This is a note.")
            result = await adapter.add_note("123", note)
            # `result` is the same as `note`
            ```
        """
        # The public OTOBO client does not currently expose an article creation
        # endpoint, so this implementation simply returns the provided note.
        return note