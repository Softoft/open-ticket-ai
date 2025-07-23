# FILE_PATH: open_ticket_ai\src\ce\run\pipeline\pipe.py
from __future__ import annotations

from abc import ABC, abstractmethod

from pydantic import BaseModel

from open_ticket_ai.src.core.mixins.registry_providable_instance import Providable
from .context import PipelineContext
from ..config.config_models import ProvidableConfig


class Pipe[InputDataT: BaseModel, OutputDataT: BaseModel](Providable, ABC):
    """Interface for all pipeline components.

    This abstract base class defines the common interface that all pipeline
    components must implement. It inherits from `Providable`
    to enable automatic registration in a component registry and from `ABC`
    to enforce abstract method implementation.

    Subclasses must implement the `process` method to define their specific
    data transformation logic within the pipeline.

    Attributes:
        Inherits attributes from `Providable` for registry management.
        InputDataType (type[InputDataT]): The type of the input data model
            expected by this pipe component.
        OutputDataType (type[OutputDataT]): The type of the output data model
            produced by this pipe component.
    """



    InputDataType: type[InputDataT] = type[InputDataT]
    """The type annotation for the input data model used in this pipe."""

    OutputDataType: type[OutputDataT] = type[OutputDataT]
    """The type annotation for the output data model produced by this pipe."""

    def __init__(self, config: ProvidableConfig):
        """

        Args:
            config: ProvidableConfig
        """

        super().__init__(config)

    @abstractmethod
    def process(self, context: PipelineContext[InputDataT]) -> PipelineContext[OutputDataT]:
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
