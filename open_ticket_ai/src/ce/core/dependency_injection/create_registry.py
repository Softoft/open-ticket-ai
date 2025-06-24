from open_ticket_ai.src.ce.core import Registry
from open_ticket_ai.src.ce.run.ai_models.hf_local_ai_inference_service import HFAIInferenceService
from open_ticket_ai.src.ce.run.attribute_predictors.priority_predictor import PriorityPredictor
from open_ticket_ai.src.ce.run.attribute_predictors.queue_predictor import QueuePredictor
from open_ticket_ai.src.ce.run.fetchers.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.src.ce.run.modifiers.priority_modifier import PriorityModifier
from open_ticket_ai.src.ce.run.modifiers.queue_modifier import QueueModifier
from open_ticket_ai.src.ce.run.preparers.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter


def create_registry() -> Registry:
    """Create the default class registry."""

    registry = Registry()
    registry.register_all(
        [OTOBOAdapter, BasicTicketFetcher, SubjectBodyPreparer,
         PriorityPredictor, QueuePredictor,
         HFAIInferenceService, PriorityModifier, QueueModifier]
    )
    return registry
