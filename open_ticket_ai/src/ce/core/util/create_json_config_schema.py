import json

from pydantic import BaseModel

from open_ticket_ai.src.ce.core.config.config_models import OpenTicketAIConfig
from open_ticket_ai.src.ce.core.util.path_util import find_project_root


class RootConfig(BaseModel):
    """Wrapper model used for schema generation."""

    open_ticket_ai: OpenTicketAIConfig


if __name__ == '__main__':
    schema: dict = RootConfig.model_json_schema()
    project_root_dir = find_project_root()
    with open(project_root_dir / "config.schema.json", "w", encoding="utf-8") as f:
        json.dump(schema, f, indent=2)
