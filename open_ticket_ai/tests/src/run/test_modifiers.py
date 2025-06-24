from unittest.mock import patch

import pytest

from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.src.ce.run.modifiers.priority_modifier import PriorityModifier
from open_ticket_ai.src.ce.run.modifiers.queue_modifier import QueueModifier
from open_ticket_ai.src.ce.core.config.config_models import ModifierConfig


class DummyModifier(Modifier):
    def modify(self, original_data: dict, model_result: str | int):
        return "dummy"


def test_modifier_initialization_calls_pretty_print():
    cfg = ModifierConfig(id="test", provider_key="dummy", params={})
    with patch("open_ticket_ai.src.ce.core.mixins.configurable_mixin.pretty_print_config") as mock_pp:
        mod = DummyModifier(cfg)
        assert mod.modifier_config is cfg
        mock_pp.assert_called_once_with(cfg)


@pytest.mark.parametrize("result", ["High", 1])
def test_priority_modifier_modify_returns_value(result):
    cfg = ModifierConfig(id="m1", provider_key="prio", params={})
    mod = PriorityModifier(cfg)
    assert mod.modify("T42", result) == result


def test_priority_modifier_description():
    text = PriorityModifier.get_description()
    assert "Modifies the priority" in text
    assert "string (e.g., 'High', 'Medium', 'Low')" in text


@pytest.mark.parametrize("queue", ["Support", "Sales"])
def test_queue_modifier_modify_returns_value(queue):
    cfg = ModifierConfig(id="m2", provider_key="queue", params={})
    mod = QueueModifier(cfg)
    assert mod.modify("T99", queue) == queue


def test_queue_modifier_description():
    text = QueueModifier.get_description()
    assert "Modifies the queue" in text
    assert "queue name" in text
