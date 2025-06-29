# In a new or existing enums file, e.g., ce/run/pipeline/status.py
from enum import Enum, auto

class PipelineStatus(Enum):
    RUNNING = auto()
    SUCCESS = auto()
    STOPPED = auto() # Controlled stop by a pipe
    FAILED = auto()  # An unexpected error occurred
