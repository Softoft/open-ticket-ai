import inspect

import pytest

from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
)
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import (
    OTOBOAdapter,
)
from open_ticket_ai.src.ce.core.config.config_models import SystemConfig
from otobo import OTOBOClient, OTOBOClientConfig, AuthData


class DummyClient(OTOBOClient):
    def __init__(self):
        super().__init__(
            OTOBOClientConfig(
                base_url="http://x",
                service="GenericTicketConnector",
                auth=AuthData(UserLogin="", Password=""),
                operations={},
            )
        )


@pytest.fixture
def adapter():
    return OTOBOAdapter(SystemConfig(id="d", provider_key="d"), DummyClient())


def test_adapter_is_abstract():
    assert inspect.isabstract(TicketSystemAdapter)
    methods = ["find_tickets", "find_first_ticket", "create_ticket", "update_ticket", "add_note"]
    for m in methods:
        assert getattr(TicketSystemAdapter, m)


def test_otobo_adapter_implements_interface(adapter):
    for m in [
        "find_tickets",
        "find_first_ticket",
        "create_ticket",
        "update_ticket",
        "add_note",
    ]:
        assert callable(getattr(adapter, m))
