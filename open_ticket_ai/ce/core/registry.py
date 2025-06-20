# --- registry + decorator ---------------------------------------------
from typing import Type

from open_ticket_ai.ce.core.mixins.description_mixin import DescriptionMixin
from open_ticket_ai.ce.run.ai_models.base_ai_model import BaseAIModel
from open_ticket_ai.ce.run.ai_models.hf_ai_model import HFAIModel
from open_ticket_ai.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.ce.run.attribute_predictors.priority_predictor import PriorityPredictor
from open_ticket_ai.ce.run.attribute_predictors.queue_predictor import QueuePredictor
from open_ticket_ai.ce.run.fetchers.basic_ticket_fetcher import BasicTicketFetcher
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.ce.run.modifiers.priority_modifier import PriorityModifier
from open_ticket_ai.ce.run.modifiers.queue_modifier import QueueModifier
from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.ce.run.preparers.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.ce.ticket_system_integration.otobo.otobo_adapter import OTOBOAdapter
from open_ticket_ai.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter

TICKET_SYSTEM_ADAPTER_REGISTRY: dict[str, Type[TicketSystemAdapter]] = {
    "otobo": OTOBOAdapter
}

FETCHER_REGISTRY: dict[str, Type[DataFetcher]] = {
    "basic_ticket_fetcher": BasicTicketFetcher
}
PREPARER_REGISTRY: dict[str, Type[DataPreparer]] = {
    "subject_body_preparer": SubjectBodyPreparer
}
ATTRIBUTE_PREDICTOR_REGISTRY: dict[str, Type[AttributePredictor]] = {
    "priority_predictor": PriorityPredictor,
    "queue_predictor": QueuePredictor
}
MODEL_REGISTRY: dict[str, Type[BaseAIModel]] = {
    "hf_ai_model": HFAIModel
}
MODIFIER_REGISTRY: dict[str, Type[Modifier]] = {
    "priority_modifier": PriorityModifier,
    "queue_modifier": QueueModifier
}


def get_merged_registry() -> dict[str, Type[DescriptionMixin]]:
    """
    Merges all registries into a single dictionary.
    """
    merged_registry = {
                          **TICKET_SYSTEM_ADAPTER_REGISTRY,
        **FETCHER_REGISTRY,
        **PREPARER_REGISTRY,
        **ATTRIBUTE_PREDICTOR_REGISTRY,
        **MODEL_REGISTRY,
        **MODIFIER_REGISTRY
    }
    return merged_registry

def does_registry_contain(key: str):
    return key in get_merged_registry()

def get_available_types():
    """
    Returns a list of all registered types.
    """
    return list(get_merged_registry().keys())

def get_registry_types_descriptions():
    """
    Returns a dictionary of all registered types and their descriptions.
    """
    return {key: value.get_description() for key, value in get_merged_registry().items()}