# FILE_PATH: open_ticket_ai\src\ce\ticket_system_integration\otobo_adapter.py
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
from otobo import OTOBOClient, TicketSearchParams, TicketUpdateParams

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
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

    async def find_tickets(self, query: dict) -> list[dict]:
        """Search for tickets matching the provided query parameters.

        Converts the query dictionary into `TicketSearchParams` and uses the OTOBO client
        to retrieve matching tickets. Returns ticket data as dictionaries.

        Args:
            query (dict): Search parameters formatted as key-value pairs. Should align with
                `TicketSearchParams` field names.

        Returns:
            list[dict]: List of dictionaries representing ticket records. Returns an empty list
                if no tickets match.

        Example:
            >>> await adapter.find_tickets({"Title": "Server Issue"})
            [{"TicketID": 123, "Title": "Server Issue", ...}, ...]
        """
        result = await self.otobo_client.search_and_get(query=TicketSearchParams(**query))
        return [ticket.model_dump() for ticket in result.Ticket]

    async def find_first_ticket(self, query: dict) -> dict | None:
        """Retrieve the first ticket matching the query parameters.

        Uses `find_tickets` to get all matching tickets and returns the first result if available.

        Args:
            query (dict): Search parameters formatted as key-value pairs.

        Returns:
            dict | None: Dictionary representing the first matching ticket record. Returns `None`
                if no tickets match the query.

        Example:
            >>> await adapter.find_first_ticket({"State": "open"})
            {"TicketID": 456, "State": "open", ...}
        """
        result = await self.find_tickets(query)
        return result[0] if len(result) >= 1 else None

    async def update_ticket(self, ticket_id: str, data: dict) -> dict:
        """Update a ticket record with new data.

        Validates and merges the ticket ID with update data into `TicketUpdateParams`,
        then sends the update request to the OTOBO API.

        Args:
            ticket_id (str): Identifier of the ticket to update.
            data (dict): Key-value pairs representing fields to update and their new values.

        Returns:
            dict: Dictionary representing the updated ticket record.

        Raises:
            ValidationError: If `data` contains invalid fields or values for ticket update.

        Example:
            >>> await adapter.update_ticket("789", {"Priority": "high"})
            {"TicketID": "789", "Priority": "high", ...}
        """
        update_params: TicketUpdateParams = TicketUpdateParams.model_validate({
            "TicketID": ticket_id,
            **data
        })
        result = await self.otobo_client.update_ticket(payload=update_params)
        return result.model_dump()
