from open_ticket_ai.ce.core.registry import Registry
from open_ticket_ai.ce.run.ai_models.hf_local_ai_inference_service import HFAIInferenceService
from open_ticket_ai.ce.run.attribute_predictors.priority_predictor import PriorityPredictor
from open_ticket_ai.ce.run.attribute_predictors.queue_predictor import QueuePredictor
from open_ticket_ai.ce.run.fetchers.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.ce.run.modifiers.priority_modifier import PriorityModifier
from open_ticket_ai.ce.run.modifiers.queue_modifier import QueueModifier
from open_ticket_ai.ce.run.preparers.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.ce.ticket_system_integration.otobo.otobo_adapter import OTOBOAdapter


def create_registry() -> Registry:
    registry = Registry()
    registry.register_all(
        [OTOBOAdapter, BasicTicketFetcher, SubjectBodyPreparer,
         PriorityPredictor, QueuePredictor,
         HFAIInferenceService, PriorityModifier, QueueModifier]
    )
    return registry
