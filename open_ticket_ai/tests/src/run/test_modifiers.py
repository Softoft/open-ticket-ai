from unittest.mock import MagicMock, patch

from open_ticket_ai.src.ce.core.config.config_models import ModifierConfig
from open_ticket_ai.src.ce.run.modifiers.generic_ticket_updater import GenericTicketUpdater
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyModifier(Pipe):
    def __init__(self, cfg, ticket_system):
        super().__init__(cfg)
        self.modifier_config = cfg
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        context.data["modified"] = True
        return context


def test_modifier_initialization_calls_pretty_print():
    cfg = ModifierConfig(id="m1", provider_key="dummy")
    with patch(
        "open_ticket_ai.src.ce.core.mixins.registry_providable_instance.pretty_print_config"
    ) as pp:
        mod = DummyModifier(cfg, MagicMock())
        pp.assert_called_once()
        assert pp.call_args.args[0] is cfg
    assert mod.modifier_config is cfg


def test_generic_ticket_updater_calls_update():
    adapter = MagicMock()
    cfg = ModifierConfig(id="u1", provider_key="generic")
    updater = GenericTicketUpdater(cfg, adapter)
    ctx = PipelineContext(ticket_id="55", data={"update_data": {"Queue": "Sales"}})
    out = updater.process(ctx)
    adapter.update_ticket.assert_called_once_with("55", {"Queue": "Sales"})
    assert out is ctx
