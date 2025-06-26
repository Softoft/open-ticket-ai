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
    """
    Adapter for OTOBO ticket system integration.
    This class provides methods to interact with the OTOBO API.
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
            config (SystemConfig): System configuration object.
            otobo_client (OTOBOClient): Client for interacting with OTOBO API.
        """
        super().__init__(config)
        self.otobo_client = otobo_client

    async def find_tickets(self, query: dict) -> list[dict]:
        """Return all tickets matching ``query``.

        Args:
            query (dict): Search parameters for tickets.

        Returns:
            list[dict]: List of tickets matching the query.
        """
        result = await self.otobo_client.search_and_get(query=TicketSearchParams(**query))
        return [ticket.model_dump() for ticket in result.Ticket]

    async def find_first_ticket(self, query: dict) -> dict | None:
        """Return the first ticket found for ``query`` if available.

        Args:
            query (dict): Search parameters for tickets.

        Returns:
            dict | None: First matching ticket dictionary or None if none found.
        """
        result = await self.find_tickets(query)
        return result[0] if len(result) >= 1 else None

    async def update_ticket(self, ticket_id: str, data: dict) -> dict:
        """Update ``ticket_id`` with ``data`` and return the updated record.

        Args:
            ticket_id (str): ID of the ticket to update.
            data (dict): Update parameters for the ticket.

        Returns:
            dict: Updated ticket record.
        """
        update_params: TicketUpdateParams = TicketUpdateParams.model_validate({
            "TicketID": ticket_id,
            **data
        })
        result = await self.otobo_client.update_ticket(payload=update_params)
        return result.model_dump()