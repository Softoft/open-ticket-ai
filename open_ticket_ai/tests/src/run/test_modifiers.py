# FILE_PATH: open_ticket_ai\tests\src\run\test_modifiers.py
from unittest.mock import MagicMock, patch

from open_ticket_ai.src.ce.core.config.config_models import ModifierConfig
from open_ticket_ai.src.ce.run.pipe_implementations.generic_ticket_updater import \
    GenericTicketUpdater
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


class DummyModifier(Pipe):
    """A dummy modifier class for testing purposes.

    This modifier sets a flag in the pipeline context to indicate modification.

    Attributes:
        modifier_config: Configuration for the modifier.
        ticket_system: The ticket system interface.
    """

    def __init__(self, cfg, ticket_system):
        """Initializes the DummyModifier instance.

        Args:
            cfg: Configuration object for the modifier.
            ticket_system: The ticket system interface to use.
        """
        super().__init__(cfg)
        self.modifier_config = cfg
        self.ticket_system = ticket_system

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes the pipeline context by setting a modification flag.

        Args:
            context: The pipeline context containing ticket data.

        Returns:
            The modified pipeline context.
        """
        context.data["modified"] = True
        return context


def test_modifier_initialization_calls_pretty_print():
    """Tests that modifier initialization calls the pretty print function.

    Verifies that during initialization of a modifier, the configuration
    pretty print function is called exactly once with the correct config.
    """
    cfg = ModifierConfig(id="m1", provider_key="dummy")
    with patch(
        "open_ticket_ai.src.ce.core.mixins.registry_providable_instance.pretty_print_config"
    ) as pp:
        mod = DummyModifier(cfg, MagicMock())
        pp.assert_called_once()
        assert pp.call_args.args[0] is cfg
    assert mod.modifier_config is cfg


def test_generic_ticket_updater_calls_update():
    """Tests that GenericTicketUpdater correctly calls the adapter's update method.

    Verifies that when processing a context with update data, the adapter's
    update_ticket method is called with the correct ticket ID and data.
    """
    adapter = MagicMock()
    cfg = ModifierConfig(id="u1", provider_key="generic")
    updater = GenericTicketUpdater(cfg, adapter)
    ctx = PipelineContext(ticket_id="55", data={"update_data": {"Queue": "Sales"}})
    out = updater.process(ctx)
    adapter.update_ticket.assert_called_once_with("55", {"Queue": "Sales"})
    assert out is ctx
