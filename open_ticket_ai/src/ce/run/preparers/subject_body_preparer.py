from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


class SubjectBodyPreparer(Pipe):
    """Extract and concatenate the ticket subject and body."""

    def __init__(self, config: RegistryInstanceConfig):
        super().__init__(config)
        self.preparer_config = config

    def process(self, context: PipelineContext) -> PipelineContext:
        subject_field = self.preparer_config.params.get("subject_field", "subject")
        body_field = self.preparer_config.params.get("body_field", "body")
        repeat_subject = int(self.preparer_config.params.get("repeat_subject", 1))

        subject = context.data.get(subject_field, "")
        body = context.data.get(body_field, "")

        prepared = f"{subject} " * repeat_subject + body
        context.data["prepared_data"] = prepared.strip()
        return context

    @staticmethod
    def get_description() -> str:
        return "Prepares the subject and body of a ticket for processing by extracting relevant information."

