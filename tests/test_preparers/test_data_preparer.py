from unittest.mock import patch

from open_ticket_ai.src.ce.core.config.config_models import PreparerConfig
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyPreparer(Pipe):
    def __init__(self, cfg):
        super().__init__(cfg)
        self.preparer_config = cfg

    def process(self, context: PipelineContext) -> PipelineContext:
        context.data["prepared_data"] = context.data.get("key")
        return context


def test_preparer_process_updates_context():
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
