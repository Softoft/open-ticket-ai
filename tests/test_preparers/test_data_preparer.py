import pytest
from unittest.mock import patch

from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.src.ce.core.config.config_models import PreparerConfig

class DummyPreparer(DataPreparer):
    def prepare(self, data: dict) -> str:
        return f"processed {data['key']}"


def test_data_preparer_cannot_instantiate_abstract(config=None):
    cfg = PreparerConfig(id='p1', provider_key='dummy')
    with pytest.raises(TypeError):
        DataPreparer(cfg)


def test_data_preparer_init_and_prepare():
    cfg = PreparerConfig(id='p2', provider_key='dummy', params={'x': 1})
    with patch('open_ticket_ai.src.ce.core.mixins.configurable_mixin.pretty_print_config') as pp:
        preparer = DummyPreparer(cfg)
        pp.assert_called_once_with(cfg)
    assert preparer.preparer_config == cfg
    assert DummyPreparer.get_description() == 'No description provided.'
    assert preparer.prepare({'key': 'value'}) == 'processed value'
