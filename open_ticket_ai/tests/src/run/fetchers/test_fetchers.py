import pytest

from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.fetchers.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.src.ce.core.config.config_models import FetcherConfig


class DummyFetcher(DataFetcher):
    """Simple concrete implementation for testing."""

    def fetch_data(self, *args, **kwargs):
        return {"args": args, "kwargs": kwargs}


def test_data_fetcher_is_abstract():
    cfg = FetcherConfig(provider_key="dummy", id="f1")
    with pytest.raises(TypeError):
        DataFetcher(cfg)


def test_data_fetcher_init_stores_config():
    cfg = FetcherConfig(provider_key="dummy", id="f1")
    fetcher = DummyFetcher(cfg)
    assert fetcher.fetcher_config is cfg


def test_data_fetcher_default_description():
    cfg = FetcherConfig(provider_key="dummy", id="f1")
    fetcher = DummyFetcher(cfg)
    assert fetcher.get_description() == "No description provided."


def test_dummy_fetcher_fetch_data_returns_dict():
    cfg = FetcherConfig(provider_key="dummy", id="f1")
    fetcher = DummyFetcher(cfg)
    result = fetcher.fetch_data(1, key="value")
    assert result == {"args": (1,), "kwargs": {"key": "value"}}


def test_basic_ticket_fetcher_description():
    cfg = FetcherConfig(provider_key="basic", id="basic1")
    fetcher = BasicTicketFetcher(cfg)
    expected = (
        "Basic ticket fetcher that retrieves ticket data from a source. "
        "It is a placeholder for a more complex implementation."
    )
    assert fetcher.get_description() == expected


def test_basic_ticket_fetcher_fetch_data_returns_none():
    cfg = FetcherConfig(provider_key="basic", id="basic1")
    fetcher = BasicTicketFetcher(cfg)
    assert fetcher.fetch_data() is None
