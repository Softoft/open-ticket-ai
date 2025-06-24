from __future__ import annotations

from .pipe import Pipe
from .context import PipelineContext
from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier


class DataPreparerPipe(Pipe):
    """Adapter to use a :class:`DataPreparer` as a pipeline pipe."""

    def __init__(self, preparer: DataPreparer):
        self.preparer = preparer

    def process(self, context: PipelineContext) -> PipelineContext:
        context.prepared_data = self.preparer.prepare(context.data)
        return context


class AIInferencePipe(Pipe):
    """Adapter to run an :class:`AIInferenceService` in the pipeline."""

    def __init__(self, ai_service: AIInferenceService):
        self.ai_service = ai_service

    def process(self, context: PipelineContext) -> PipelineContext:
        context.model_result = self.ai_service.generate_response(context.prepared_data)
        return context


class ModifierPipe(Pipe):
    """Final pipe applying a :class:`Modifier`."""

    def __init__(self, modifier: Modifier):
        self.modifier = modifier

    def process(self, context: PipelineContext) -> PipelineContext:
        self.modifier.modify(ticket_id=context.ticket_id, model_result=context.model_result)
        return context
