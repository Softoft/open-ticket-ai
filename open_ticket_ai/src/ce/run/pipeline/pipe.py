from __future__ import annotations

from abc import ABC, abstractmethod

from .context import PipelineContext
from ...core.mixins.registry_providable_instance import RegistryProvidableInstance


class Pipe(RegistryProvidableInstance, ABC):
    """Interface for all pipeline components."""

    @abstractmethod
    def process(self, context: PipelineContext) -> PipelineContext:
        """Process ``context`` and return it."""
        pass