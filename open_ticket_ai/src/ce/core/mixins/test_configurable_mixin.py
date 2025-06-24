import logging
from unittest.mock import patch

import pytest
from pydantic import BaseModel

from open_ticket_ai.src.ce.core.mixins.configurable_mixin import ConfigurableMixin


class DummyConfig(BaseModel):
    param_a: str
    param_b: int


class MyConfigurableClass(ConfigurableMixin):
    def __init__(self, config: DummyConfig):
        super().__init__(config)


def test_configurable_mixin_logs_config():
    """
    Tests that ConfigurableMixin logs the class name and configuration
    during initialization.
    """
    test_config = DummyConfig(param_a="test_value", param_b=123)

    with patch.object(logging.getLogger("open_ticket_ai.src.ce.core.mixins.configurable_mixin"), "info") as mock_log_info, \
         patch("open_ticket_ai.src.ce.core.mixins.configurable_mixin.pretty_print_config") as mock_pretty_print:

        MyConfigurableClass(config=test_config)

        assert mock_log_info.call_count == 1
        mock_log_info.assert_any_call("Initializing MyConfigurableClass with config:")
        mock_pretty_print.assert_called_once_with(test_config)


def test_configurable_mixin_requires_config():
    """
    Tests that ConfigurableMixin (or a class using it) raises an error
    if config is not provided, as per its __init__ signature.
    """
    with pytest.raises(TypeError) as excinfo:
        MyConfigurableClass()  # type: ignore

    assert "'config'" in str(excinfo.value)

class AnotherConfigurable(ConfigurableMixin):
    pass # No __init__ here, relies on Mixin's if not overridden


def test_configurable_mixin_init_without_explicit_super_call():
    """
    Tests a class that inherits ConfigurableMixin but doesn't explicitly call super().__init__
    in its own __init__. This scenario might not be typical for this mixin
    but tests resilience.
    """
    class MinimalConfigurable(ConfigurableMixin):
        def __init__(self, config: DummyConfig):
            # Forgetting super().__init__(config)
            # This test expects the mixin's __init__ NOT to be called.
            # If the mixin's __init__ was essential for some internal state setup
            # beyond logging, this test would need to verify that state.
            # However, current ConfigurableMixin only logs.
            pass

    test_config = DummyConfig(param_a="minimal", param_b=0)
    with patch.object(logging.getLogger("open_ticket_ai.src.ce.core.mixins.configurable_mixin"), "info") as mock_log_info:
        MinimalConfigurable(config=test_config)
        mock_log_info.assert_not_called()


class ConfigurableWithOwnInitLogic(ConfigurableMixin):
    def __init__(self, config: DummyConfig, extra_param: str):
        super().__init__(config)
        self.extra_param = extra_param
        self.config_snapshot = config # Storing for later verification

def test_configurable_mixin_with_subclass_init_logic():
    """
    Tests that ConfigurableMixin works correctly when the subclass has its
    own __init__ logic and calls super().__init__ correctly.
    """
    test_config = DummyConfig(param_a="subclass_test", param_b=456)
    extra_value = "extra_data"

    with patch.object(logging.getLogger("open_ticket_ai.src.ce.core.mixins.configurable_mixin"), "info") as mock_log_info, \
         patch("open_ticket_ai.src.ce.core.mixins.configurable_mixin.pretty_print_config") as mock_pretty_print:

        instance = ConfigurableWithOwnInitLogic(config=test_config, extra_param=extra_value)

        mock_log_info.assert_any_call("Initializing ConfigurableWithOwnInitLogic with config:")
        mock_pretty_print.assert_called_once_with(test_config)
        assert instance.extra_param == extra_value
        assert instance.config_snapshot == test_config
