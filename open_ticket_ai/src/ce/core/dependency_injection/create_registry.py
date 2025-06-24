from open_ticket_ai.src.ce.core.dependency_injection.registry import Registry
from open_ticket_ai.src.ce.core.mixins.registry_instance_config import RegistryInstanceConfig
from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import \
    RegistryProvidableInstance
from open_ticket_ai.src.ce.run.ai_models.hf_local_ai_inference_service import HFAIInferenceService
from open_ticket_ai.src.ce.run.preparers.subject_body_preparer import SubjectBodyPreparer
from open_ticket_ai.src.ce.ticket_system_integration.otobo_adapter import OTOBOAdapter


def create_registry() -> Registry:
    """Create the default class registry."""
    super_class = RegistryProvidableInstance
    registry = Registry()
    registry.register_all(
        [OTOBOAdapter, SubjectBodyPreparer,
         HFAIInferenceService]
    )
    return registry
