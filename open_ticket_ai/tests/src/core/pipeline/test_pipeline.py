import random

from pydantic import BaseModel
import pytest

from open_ticket_ai.src.core.config.config_models import PipelineConfig, ProvidableConfig, SchedulerConfig
from open_ticket_ai.src.core.pipeline.context import PipelineContext
from open_ticket_ai.src.core.pipeline.meta_info import MetaInfo
from open_ticket_ai.src.core.pipeline.pipe import Pipe
from open_ticket_ai.src.core.pipeline.pipeline import Pipeline
from open_ticket_ai.src.core.pipeline.status import PipelineStatus


# Dummy data model for testing
class DummyData(BaseModel):
    value: int


class IncrementPipe(Pipe[DummyData, DummyData]):
    InputDataType = DummyData
    OutputDataType = DummyData

    def __init__(self, config: ProvidableConfig = None):
        """

        Args:
            config:
        """
        super().__init__(config)

    def process(self, context):
        context.data.value += 1
        return context


class StopPipe(Pipe[DummyData, DummyData]):
    InputDataType = DummyData
    OutputDataType = DummyData

    def process(self, context):
        context.data.value += 1
        context.stop_pipeline()
        return context


class ErrorPipe(Pipe[DummyData, DummyData]):
    InputDataType = DummyData
    OutputDataType = DummyData

    def process(self, context):
        raise RuntimeError("Test error")


def test_meta_info_defaults():
    mi = MetaInfo()
    assert mi.status == PipelineStatus.RUNNING
    assert mi.error_message is None
    assert mi.failed_pipe is None


def test_context_stop_pipeline():
    ctx = PipelineContext(data=DummyData(value=0), meta_info=MetaInfo())
    ctx.stop_pipeline()
    assert ctx.meta_info.status == PipelineStatus.STOPPED


# Fixture for a dummy PipelineConfig
@pytest.fixture
def create_pipeline_config():
    return lambda pipes: PipelineConfig(
            id="test_pipeline",
            params={},
            provider_key="test_provider",
            schedule=SchedulerConfig(
                    interval=20,
                    unit="minutes",
            ),
            pipe_ids=pipes,
    )


@pytest.fixture
def create_increment_pipe():

    return lambda: IncrementPipe(
            ProvidableConfig(
                    id="increment" + str(random.randint(1, 1000)),
                    params={},
                    provider_key="increment_provider" + str(random.randint(1, 1000)),
            ),
    )


@pytest.fixture
def create_stop_pipe():
    return lambda: StopPipe(
            ProvidableConfig(
                    id="stop" + str(random.randint(1, 1000)),
                    params={},
                    provider_key="stop_provider" + str(random.randint(1, 1000)),
            ),
    )


@pytest.fixture
def create_error_pipe():
    return lambda: ErrorPipe(
            ProvidableConfig(
                    id="error" + str(random.randint(1, 1000)),
                    params={},
                    provider_key="error_provider" + str(random.randint(1, 1000)),
            ),
    )


# Test successful execution of multiple pipe_ids
def test_pipeline_success_execution(create_pipeline_config, create_increment_pipe):
    pipes = [
        create_increment_pipe(),
        create_increment_pipe(),
        create_increment_pipe(),
    ]
    pipeline = Pipeline(create_pipeline_config(pipes))
    ctx = PipelineContext(data=DummyData(value=0), meta_info=MetaInfo())
    result = pipeline.execute(ctx)
    assert result.data.value == 3
    assert result.meta_info.status == PipelineStatus.SUCCESS


# Test that initial SUCCESS status still runs
def test_pipeline_initial_success_status(create_pipeline_config):
    create_pipeline_config.pipes = [IncrementPipe(create_pipeline_config)]
    pipeline = Pipeline(create_pipeline_config)
    mi = MetaInfo(status=PipelineStatus.SUCCESS)
    ctx = PipelineContext(data=DummyData(value=0), meta_info=mi)
    result = pipeline.execute(ctx)
    assert result.data.value == 1
    assert result.meta_info.status == PipelineStatus.SUCCESS


# Test controlled stop by a pipe
def test_pipeline_stop_request(create_pipeline_config):
    create_pipeline_config.pipes = [
        IncrementPipe(create_pipeline_config),
        StopPipe(create_pipeline_config),
        IncrementPipe(create_pipeline_config),
    ]
    pipeline = Pipeline(create_pipeline_config)
    ctx = PipelineContext(data=DummyData(value=0), meta_info=MetaInfo())
    result = pipeline.execute(ctx)
    assert result.data.value == 2
    assert result.meta_info.status == PipelineStatus.STOPPED


# Test exception handling and metadata on failure
def test_pipeline_failure_handling(create_pipeline_config):
    create_pipeline_config.pipes = [
        IncrementPipe(create_pipeline_config),
        ErrorPipe(create_pipeline_config),
        IncrementPipe(create_pipeline_config),
    ]
    pipeline = Pipeline(create_pipeline_config)
    ctx = PipelineContext(data=DummyData(value=0), meta_info=MetaInfo())
    result = pipeline.execute(ctx)
    assert result.data.value == 1
    assert result.meta_info.status == PipelineStatus.FAILED
    assert result.meta_info.failed_pipe == "ErrorPipe"
    assert "Test error" in result.meta_info.error_message


# Test that process() delegates to execute()
def test_pipeline_process_alias(create_pipeline_config):
    pipes = [IncrementPipe(create_pipeline_config)]
    pipeline = Pipeline(create_pipeline_config, pipes)
    ctx1 = PipelineContext(data=DummyData(value=10), meta_info=MetaInfo())
    res_exec = pipeline.execute(ctx1)
    ctx2 = PipelineContext(data=DummyData(value=10), meta_info=MetaInfo())
    res_proc = pipeline.process(ctx2)
    assert res_proc.data.value == res_exec.data.value
    assert res_proc.meta_info.status == res_exec.meta_info.status


# Test that non-runnable initial statuses do not execute pipe_ids
def test_pipeline_non_runnable_initial_status(create_pipeline_config):
    pipes = [IncrementPipe(create_pipeline_config)]
    pipeline = Pipeline(create_pipeline_config, pipes)
    for status in [PipelineStatus.STOPPED, PipelineStatus.FAILED]:
        mi = MetaInfo(status=status)
        ctx = PipelineContext(data=DummyData(value=5), meta_info=mi)
        result = pipeline.execute(ctx)
        assert result.data.value == 5
        assert result.meta_info.status == status
