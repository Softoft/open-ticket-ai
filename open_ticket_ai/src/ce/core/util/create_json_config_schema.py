import json

from pydantic import BaseModel

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path


class RootConfig(BaseModel):
    """Wrapper model used for schema generation.

    This class serves as a container for the main configuration model of the OpenTicketAI system.
    It is designed to be used for generating JSON schema representations of the configuration.

    Attributes:
        open_ticket_ai (OpenTicketAIConfig): The main configuration object containing all
            settings and parameters for the OpenTicketAI system.
    """

    open_ticket_ai: OpenTicketAIConfig


if __name__ == '__main__':
    """Generates JSON schema for RootConfig and writes it to config.schema.json."""
    schema: dict = RootConfig.model_json_schema()
    project_root_dir = find_python_code_root_path()
    with open(project_root_dir / "config.schema.json", "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)