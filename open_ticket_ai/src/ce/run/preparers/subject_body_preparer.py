from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


class SubjectBodyPreparer(Pipe):
    """Extract and concatenate the ticket subject and body."""

    def process(self, context: PipelineContext) -> PipelineContext:
        pass

    @staticmethod
    def get_description() -> str:
        return "Prepares the subject and body of a ticket for processing by extracting relevant information."

