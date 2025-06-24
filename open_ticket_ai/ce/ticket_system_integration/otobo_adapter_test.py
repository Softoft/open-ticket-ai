import pytest

from open_ticket_ai.ce.ticket_system_integration.otobo_adapter_config import OTOBOAdapterConfig


@pytest.fixture
def system():

    return OTOBOAdapterConfig(
        url="https://otobo.example.com",
        username="root@",
        password="test_password",
        ticket_id=12345,
    )