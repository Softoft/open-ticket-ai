from unittest.mock import patch

from open_ticket_ai.src.ce.core.config.config_models import PreparerConfig
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyPreparer(Pipe):
    """A dummy implementation of a Pipe for testing preparer functionality.

    This class simulates a preparer step in the pipeline by copying a value
    from the context data under a specific key.

    Attributes:
        preparer_config (PreparerConfig): Configuration settings for the preparer.
    """

    def __init__(self, cfg):
        """Initializes the DummyPreparer with the given configuration.

        Args:
            cfg (PreparerConfig): Configuration object for the preparer.
        """
        super().__init__(cfg)
        self.preparer_config = cfg

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes pipeline context by copying data to 'prepared_data' field.

        Copies the value from context.data['key'] to context.data['prepared_data'].

        Args:
            context (PipelineContext): The pipeline context containing ticket data.

        Returns:
            PipelineContext: The updated context with 'prepared_data' added.
        """
        context.data["prepared_data"] = context.data.get("key")
        return context


def test_preparer_process_updates_context():
    """Tests that DummyPreparer correctly updates context data.

    Verifies:
        1. The preparer's configuration is properly printed during initialization
        2. The process method correctly copies 'key' value to 'prepared_data'
    """
    cfg = PreparerConfig(id="p1", provider_key="dummy")
    with patch(
        "open_ticket_ai.src.ce.core.mixins.registry_providable_instance.pretty_print_config"
    ) as pp:
        preparer = DummyPreparer(cfg)
        pp.assert_called_once()
        assert pp.call_args.args[0] is cfg
    ctx = PipelineContext(ticket_id="1", data={"key": "value"})
    out = preparer.process(ctx)
    assert out.data["prepared_data"] == "value"