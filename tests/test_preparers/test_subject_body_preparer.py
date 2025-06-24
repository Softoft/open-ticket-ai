from unittest.mock import patch

from open_ticket_ai.src.ce.run.preparers.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.src.ce.core.config.config_models import PreparerConfig


def test_subject_body_preparer_description_and_prepare():
    cfg = PreparerConfig(id='sb', provider_key='subject-body')
    with patch('open_ticket_ai.src.ce.core.mixins.configurable_mixin.pretty_print_config') as pp:
        preparer = SubjectBodyPreparer(cfg)
        pp.assert_called_once_with(cfg)
    assert SubjectBodyPreparer.get_description() == (
        "Prepares the subject and body of a ticket for processing by extracting relevant information."
    )
    assert preparer.prepare() is None
