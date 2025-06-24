import abc

from open_ticket_ai.src.ce.run.ai_models.ai_inference_service import AIInferenceService
from open_ticket_ai.src.ce.run.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.src.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.src.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.src.ce.run.preparers.data_preparer import DataPreparer
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import (
    TicketSystemAdapter,
)


class AbstractContainer(abc.ABC):
    """Abstract interface for dependency containers."""
    @abc.abstractmethod
    def get_system(self) -> TicketSystemAdapter:
        """Return the configured ticket system adapter."""
        pass

    @abc.abstractmethod
    def get_fetcher(self, fetcher_key: str) -> DataFetcher:
        """Return a data fetcher by ID."""
        pass

    @abc.abstractmethod
    def get_preparer(self, preparer_key: str) -> DataPreparer:
        """Return a data preparer by ID."""
        pass

    @abc.abstractmethod
    def get_ai_inference_service(self, model_key: str) -> AIInferenceService:
        """Return an AI inference service by ID."""
        pass

    @abc.abstractmethod
    def get_modifier(self, modifier_key: str) -> Modifier:
        """Return a modifier by ID."""
        pass

    @abc.abstractmethod
    def get_predictor(self, predictor_key: str) -> AttributePredictor:
        """Return an attribute predictor by ID."""
        pass
