from unittest.mock import MagicMock

from open_ticket_ai.src.ce.core.config.config_models import FetcherConfig
from open_ticket_ai.src.ce.run.fetchers.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyFetcher(Pipe):
    def __init__(self, cfg, ticket_system):
        super().__init__(cfg)
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        context.data["dummy"] = True
        return context


def test_dummy_fetcher_process_populates_context():
    cfg = FetcherConfig(id="d1", provider_key="dummy")
    fetcher = DummyFetcher(cfg, MagicMock())
    ctx = PipelineContext(ticket_id="42")
    result = fetcher.process(ctx)
    assert result.data["dummy"] is True


def test_basic_ticket_fetcher_fetches_ticket():
    adapter = MagicMock()
    adapter.find_first_ticket.return_value = {"TicketID": "42", "subject": "Hello"}
    cfg = FetcherConfig(id="b1", provider_key="basic")
    fetcher = BasicTicketFetcher(cfg, adapter)
    ctx = PipelineContext(ticket_id="42")
    out = fetcher.process(ctx)
    adapter.find_first_ticket.assert_called_once_with({"TicketID": "42"})
    assert out.data["TicketID"] == "42"


def test_basic_ticket_fetcher_description():
    cfg = FetcherConfig(id="b1", provider_key="basic")
    fetcher = BasicTicketFetcher(cfg, MagicMock())
    assert "Basic ticket fetcher" in fetcher.get_description()
