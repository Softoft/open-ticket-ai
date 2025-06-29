# FILE_PATH: open_ticket_ai\src\ce\run\pipe_implementations\subject_body_preparer.py
from open_ticket_ai.src.ce.core.config.config_models import RegistryInstanceConfig
from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe


class SubjectBodyPreparer(Pipe):
    """A pipeline component that prepares ticket subject and body content for processing.

    This pipe extracts the subject and body fields from ticket data, repeats the subject
    a configurable number of times, and concatenates it with the body content. The prepared
    data is stored in the pipeline context for downstream processing.

    Attributes:
        preparer_config (RegistryInstanceConfig): Configuration parameters for the preparer.
    """

    def __init__(self, config: RegistryInstanceConfig):
        """Initializes the SubjectBodyPreparer with configuration.

        Args:
            config (RegistryInstanceConfig): Configuration parameters for the preparer.
        """
        super().__init__(config)
        self.preparer_config = config

    def process(self, context: PipelineContext) -> PipelineContext:
        """Processes ticket data to prepare subject and body content.

        Extracts the configured subject and body fields from context data,
        repeats the subject as specified in configuration, concatenates it with
        the body and stores the result in the configured result field.

        Args:
            context (PipelineContext): Pipeline context containing ticket data.

        Returns:
            PipelineContext: Updated context with prepared data.
        """
        subject_field = self.preparer_config.params.get("subject_field", "subject")
        body_field = self.preparer_config.params.get("body_field", "body")
        repeat_subject = int(self.preparer_config.params.get("repeat_subject", 3))
        result_field = self.preparer_config.params.get("result_field", "subject_body_combined")

        subject = context.data.get(subject_field, "")
        body = context.data.get(body_field, "")

        prepared = f"{subject} " * repeat_subject + body
        context.data[result_field] = prepared.strip()
        return context

    @staticmethod
    def get_description() -> str:
        """Provides a description of the pipe's functionality.

        Returns:
            str: Description of the pipe's purpose.
        """
        return "Prepares the subject and body of a ticket for processing by extracting relevant information."
