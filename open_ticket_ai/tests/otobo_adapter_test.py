# FILE_PATH: open_ticket_ai\tests\otobo_adapter_test.py
import dataclasses
from unittest.mock import AsyncMock

from otobo import OTOBOClient, OTOBOClientConfig
import pytest

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter_config import OTOBOAdapterConfig


@dataclasses.dataclass
class MockedTicket:
    """Mocked ticket data structure for testing purposes.

    This class is used to simulate a ticket object with essential attributes.
    It is primarily used in unit tests to verify the behavior of the OTOBOAdapter.
    """
    id: str
    title: str
    description: str
    status: str
    priority: str
    queue: str


TICKETS = [
    MockedTicket(
        id="1",
        title="Test Ticket 1",
        description="Description 1",
        status="open",
        priority="high",
        queue="default",
    ),
    MockedTicket(
        id="2",
        title="Test Ticket 2",
        description="Description 2",
        status="closed",
        priority="low",
        queue="default",
    ),
    MockedTicket(
        id="3",
        title="Test Ticket 3",
        description="Description 3",
        status="open",
        priority="medium",
        queue="default",
    ),
    MockedTicket(
        id="4",
        title="Test Ticket 4",
        description="Description 4",
        status="open",
        priority="medium",
        queue="misc",
    ),
]


class MockedOTOBOClient(OTOBOClient):
    """Mocked OTOBOAdapter for testing purposes.

    This class is used to create an instance of OTOBOAdapter with a mocked OTOBOClient.
    It allows testing without requiring a real OTOBO server connection.
    """

    @staticmethod
    def get_description() -> str:
        return "Mocked OTOBO adapter for testing purposes."

    def __init__(
        self,
        ticket_data: list[MockedTicket]
    ):
        super().__init__(
            OTOBOClientConfig(
                base_url="https://mocked.otobo.example.com",
                service="GenericTicketConnector",
                auth=None,
                operations={
                    "search": "/search",
                    "update": "/update",
                    "get": "/get",
                },
            ),
        )
        self.ticket_data = ticket_data

    async def search_and_get(self, query):
        return

    async def update_ticket(self, payload):
        return await super().update_ticket(payload)


@pytest.fixture
def adapter_and_client():
    """Fixture that provides an instance of OTOBOAdapter and a mocked OTOBOClient.

    Returns:
        tuple: A tuple containing:
            adapter (OTOBOAdapter): Configured OTOBOAdapter instance
            client (AsyncMock): Mocked OTOBOClient instance
    """
    client = MockedOTOBOClient(TICKETS)
    config = SystemConfig(id="dummy", provider_key="dummy", params={})
    adapter = OTOBOAdapter(config=config, otobo_client=client)
    return adapter, client


def test_config_str_and_password(monkeypatch):
    """Test OTOBOAdapterConfig string representation and password retrieval from environment.

    Verifies:
        1. The __str__ method excludes the password value
        2. Password is correctly retrieved from environment variable
    """
    monkeypatch.setenv("OTOBO_PASS", "s3cret")
    cfg = OTOBOAdapterConfig(
        server_address="https://otobo.example.com",
        webservice_name="GenericTicketConnector",
        search_operation_url="/search",
        update_operation_url="/update",
        get_operation_url="/get",
        username="root",
        password_env_var="OTOBO_PASS",
    )
    expected = (
        "OTOBOServerConfig(server_address=https://otobo.example.com, "
        "webservice_name=GenericTicketConnector, search_operation_url=/search, "
        "update_operation_url=/update, get_operation_url=/get, username=root)"
    )
    assert str(cfg) == expected
    assert cfg.password == "s3cret"


def test_config_password_missing_env(monkeypatch):
    """Test OTOBOAdapterConfig raises error when password environment variable is missing.

    Verifies:
        Accessing password property raises ValueError when env var doesn't exist
    """
    monkeypatch.delenv("MISSING_ENV", raising=False)
    cfg = OTOBOAdapterConfig(
        server_address="s",
        webservice_name="w",
        search_operation_url="s",
        update_operation_url="u",
        get_operation_url="g",
        username="user",
        password_env_var="MISSING_ENV",
    )
    with pytest.raises(ValueError):
        _ = cfg.password
