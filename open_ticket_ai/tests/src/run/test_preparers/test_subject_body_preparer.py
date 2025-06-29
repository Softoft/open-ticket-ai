# FILE_PATH: open_ticket_ai\tests\src\run\test_preparers\test_subject_body_preparer.py
from unittest.mock import patch

from open_ticket_ai.src.ce.core.config.config_models import PreparerConfig
from open_ticket_ai.src.ce.run.pipe_implementations.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext


def test_subject_body_preparer_process_concatenates_fields():
    """Tests the SubjectBodyPreparer's process method.

    This test verifies that:
    1. During initialization, the preparer calls pretty_print_config with its config
    2. The process method correctly concatenates 'subject' and 'body' fields from context data
    """
    cfg = PreparerConfig(id="sb", provider_key="subject-body", params={})
    with patch(
        "open_ticket_ai.src.ce.core.mixins.registry_providable_instance.pretty_print_config"
    ) as pp:
        preparer = SubjectBodyPreparer(cfg)
        pp.assert_called_once()
        assert pp.call_args.args[0] is cfg
    ctx = PipelineContext(ticket_id="1", data={"subject": "Hello", "body": "World"})
    result = preparer.process(ctx)
    assert result.data["prepared_data"] == "Hello World"
