# FILE_PATH: open_ticket_ai\tests\src\run\fetchers\test_fetchers.py
from unittest.mock import MagicMock

from open_ticket_ai.src.ce.core.config.config_models import FetcherConfig
from open_ticket_ai.src.ce.run.pipe_implementations.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyFetcher(Pipe):
    """A dummy fetcher for testing purposes.

    This fetcher does not fetch any real data but simply sets a dummy flag in the context.
    """

    def __init__(self, cfg, ticket_system):
        """Initializes the DummyFetcher.

        Args:
            cfg: The configuration for the fetcher.
            ticket_system: A mock ticket system object for testing.
        """
        super().__init__(cfg)
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes the pipeline context by setting a dummy flag.

        Args:
            context: The pipeline context.

        Returns:
            PipelineContext: The updated pipeline context with a dummy flag set to True.
        """
        context.data["dummy"] = True
        return context


def test_dummy_fetcher_process_populates_context():
    """Tests the `DummyFetcher.process` method.

    This test verifies that the `DummyFetcher` correctly sets a dummy flag in the pipeline context.

    Steps:
    1. Initialize a `DummyFetcher` with mock configuration and ticket system
    2. Create a pipeline context with a dummy ticket ID
    3. Process the context through the fetcher
    4. Verify the context contains the expected 'dummy' flag with True value

    This ensures the dummy fetcher behaves as expected for testing purposes.
    """
    cfg = FetcherConfig(id="d1", provider_key="dummy")
    fetcher = DummyFetcher(cfg, MagicMock())
    ctx = PipelineContext(ticket_id="42")
    result = fetcher.process(ctx)
    assert result.data["dummy"] is True


def test_basic_ticket_fetcher_fetches_ticket():
    """Tests the `BasicTicketFetcher.process` method.

    This test verifies that the `BasicTicketFetcher` correctly:
    - Retrieves ticket data using the adapter
    - Populates the pipeline context with ticket information

    Steps:
    1. Create a mock adapter that returns predefined ticket data
    2. Initialize the fetcher with configuration and mock adapter
    3. Create pipeline context with a ticket ID
    4. Process context through the fetcher
    5. Verify adapter was called with correct parameters
    6. Verify context contains expected ticket data

    This ensures the basic ticket fetcher properly integrates with the ticket system adapter.
    """
    adapter = MagicMock()
    adapter.find_first_ticket.return_value = {"TicketID": "42", "subject": "Hello"}
    cfg = FetcherConfig(id="b1", provider_key="basic")
    fetcher = BasicTicketFetcher(cfg, adapter)
    ctx = PipelineContext(ticket_id="42")
    out = fetcher.process(ctx)
    adapter.find_first_ticket.assert_called_once_with({"TicketID": "42"})
    assert out.data["TicketID"] == "42"


def test_basic_ticket_fetcher_description():
    """Tests the `BasicTicketFetcher.get_description` method.

    This test verifies that the fetcher provides an appropriate description string.

    Steps:
    1. Initialize the fetcher with mock configuration and adapter
    2. Retrieve the description string
    3. Verify the description contains expected keywords

    This ensures the fetcher correctly identifies itself in pipeline documentation.
    """
    cfg = FetcherConfig(id="b1", provider_key="basic")
    fetcher = BasicTicketFetcher(cfg, MagicMock())
    assert "Basic ticket fetcher" in fetcher.get_description()
