import asyncio
from unittest.mock import AsyncMock

import pytest
import otobo

from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter_config import OTOBOAdapterConfig


@pytest.fixture
def adapter_and_client():
    client = AsyncMock(spec=otobo.OTOBOClient)
    config = SystemConfig(provider_key="dummy", params={})
    adapter = OTOBOAdapter(config=config, otobo_client=client)
    return adapter, client


def test_config_str_and_password(monkeypatch):
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


def test_find_tickets(adapter_and_client):
    adapter, client = adapter_and_client
    tickets = [
        otobo.TicketDetailOutput(TicketID=1, Title="A", Article=[], DynamicField=[]),
        otobo.TicketDetailOutput(TicketID=2, Title="B", Article=[], DynamicField=[]),
    ]
    client.search_and_get.return_value = otobo.FullTicketSearchResponse(Ticket=tickets)

    query = {"TicketNumber": "42"}
    result = asyncio.run(adapter.find_tickets(query))

    called_params = client.search_and_get.call_args.kwargs["query"]
    assert isinstance(called_params, otobo.TicketSearchParams)
    assert called_params.TicketNumber == "42"
    assert result == [t.model_dump() for t in tickets]


def test_find_first_ticket(adapter_and_client):
    adapter, client = adapter_and_client
    tickets = [
        otobo.TicketDetailOutput(TicketID=5, Article=[], DynamicField=[])
    ]
    client.search_and_get.return_value = otobo.FullTicketSearchResponse(Ticket=tickets)
    result = asyncio.run(adapter.find_first_ticket({"TicketNumber": "5"}))
    assert result == tickets[0].model_dump()

    client.search_and_get.return_value = otobo.FullTicketSearchResponse(Ticket=[])
    result = asyncio.run(adapter.find_first_ticket({"TicketNumber": "5"}))
    assert result is None


def test_update_ticket(adapter_and_client):
    adapter, client = adapter_and_client
    update_response = type("Resp", (), {"model_dump": lambda self: {"ok": True}})()
    client.update_ticket.return_value = update_response

    result = asyncio.run(adapter.update_ticket("1", {"Ticket": {"Title": "New"}}))

    called_payload = client.update_ticket.call_args.kwargs["payload"]
    assert isinstance(called_payload, otobo.TicketUpdateParams)
    assert called_payload.TicketID == 1
    assert called_payload.Ticket.Title == "New"
    assert result == {"ok": True}
