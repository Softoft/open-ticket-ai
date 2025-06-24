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
        return "Adapter for OTOBO ticket system integration, providing methods to retrieve and update tickets."

    @inject
    def __init__(self, config: SystemConfig, otobo_client: OTOBOClient):
        """Create a new adapter instance."""

        super().__init__(config)
        self.otobo_client = otobo_client

    async def find_tickets(self, query: dict) -> list[dict]:
        """Return all tickets matching ``query``."""

        result = await self.otobo_client.search_and_get(query=TicketSearchParams(**query))
        return [ticket.model_dump() for ticket in result.Ticket]

    async def find_first_ticket(self, query: dict) -> dict | None:
        """Return the first ticket found for ``query`` if available."""

        result = await self.find_tickets(query)
        return result[0] if len(result) >= 1 else None

    async def update_ticket(self, ticket_id: str, data: dict) -> dict:
        """Update ``ticket_id`` with ``data`` and return the updated record."""

        update_params: TicketUpdateParams = TicketUpdateParams.model_validate({
            "TicketID": ticket_id,
            **data
        })
        result = await self.otobo_client.update_ticket(payload=update_params)
        return result.model_dump()
