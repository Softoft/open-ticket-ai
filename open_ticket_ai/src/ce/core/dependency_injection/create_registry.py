# FILE_PATH: open_ticket_ai\src\ce\core\dependency_injection\create_registry.py
from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry
from open_ticket_ai.src.ce.core.config.config_models import RegistryInstanceConfig
from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance
from open_ticket_ai.src.ce.run.pipe_implementations.hf_local_ai_inference_service import \
    HFAIInferenceService
from open_ticket_ai.src.ce.run.pipe_implementations.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter


def create_registry() -> Registry:
    """Creates and configures the default class registry.

    This function initializes a `Registry` instance and registers essential classes
    required for the application's dependency injection system. The registered classes
    include integration adapters, data preparers, and AI inference services.

    The following classes are registered:
    - `OTOBOAdapter`: Handles integration with the OTOBO ticket system.
    - `SubjectBodyPreparer`: Prepares subject and body content for ticket processing.
    - `HFAIInferenceService`: Provides local AI inference using Hugging Face models.

    Returns:
        Registry: A configured registry instance with all necessary classes registered.
    """
    registry = Registry()
    registry.register_all(
        [OTOBOAdapter, SubjectBodyPreparer,
         HFAIInferenceService]
    )
    return registry
