# FILE_PATH: open_ticket_ai\tests\otobo_adapter_test.py
import asyncio
from unittest.mock import AsyncMock

import pytest
import otobo

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter_config import OTOBOAdapterConfig


@pytest.fixture
def adapter_and_client():
    """Fixture that provides an instance of OTOBOAdapter and a mocked OTOBOClient.

    Returns:
        tuple: A tuple containing:
            adapter (OTOBOAdapter): Configured OTOBOAdapter instance
            client (AsyncMock): Mocked OTOBOClient instance
    """
    client = AsyncMock(spec=otobo.OTOBOClient)
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



