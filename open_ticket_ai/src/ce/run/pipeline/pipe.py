from __future__ import annotations

from abc import ABC, abstractmethod

from .context import PipelineContext


class Pipe(ABC):
    """Interface for all pipeline components."""

    @abstractmethod
    def process(self, context: PipelineContext) -> PipelineContext:
        """Process ``context`` and return it."""
        raise NotImplementedError
