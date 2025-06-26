from __future__ import annotations

from abc import ABC, abstractmethod

from .context import PipelineContext
from ...core.mixins.registry_providable_instance import RegistryProvidableInstance


class Pipe(RegistryProvidableInstance, ABC):
    """Interface for all pipeline components.

    This abstract base class defines the common interface that all pipeline
    components must implement. It inherits from `RegistryProvidableInstance`
    to enable automatic registration in a component registry and from `ABC`
    to enforce abstract method implementation.

    Subclasses must implement the `process` method to define their specific
    data transformation logic within the pipeline.

    Attributes:
        Inherits attributes from `RegistryProvidableInstance` for registry management.
    """

    @abstractmethod
    def process(self, context: PipelineContext) -> PipelineContext:
        """Process a pipeline context object and return the modified context.

        This method defines the core processing logic for a pipeline component.
        It takes a `PipelineContext` object containing shared pipeline state,
        performs transformations or operations on this context, and returns the
        updated context for the next component in the pipeline.

        Args:
            context: The current pipeline context containing shared state data.

        Returns:
            The updated `PipelineContext` object after processing.

        Raises:
            Implementation-specific exceptions may be raised by subclasses to
            indicate processing errors or invalid states.
        """
        pass