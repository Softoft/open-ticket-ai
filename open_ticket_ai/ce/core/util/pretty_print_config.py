import logging

import yaml
from pydantic import BaseModel
from rich.console import Console
from rich.syntax import Syntax

logger = logging.getLogger(__name__)
console = Console()


def pretty_print_config(config: BaseModel):
    """Pretty print a pydantic model using ``rich``."""

    # turn your BaseModel into a dict
    cfg_dict = config.model_dump()

    # render YAML
    yaml_str = yaml.safe_dump(cfg_dict, sort_keys=False)
    syntax = Syntax(yaml_str, "yaml")

    # print with rich directly (bypasses standard logger)
    console.print(syntax)
