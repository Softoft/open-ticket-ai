import logging

import yaml
from pydantic import BaseModel
from rich.console import Console
from rich.syntax import Syntax

logger = logging.getLogger(__name__)

def pretty_print_config(config: BaseModel, console: Console):
    """Pretty print a pydantic model using ``rich``.

    This function converts a Pydantic BaseModel to a dictionary, serializes it to YAML,
    and prints it to the console using rich's syntax highlighting.

    Args:
        config (BaseModel): The Pydantic model configuration to display.
        console (Console): The rich console instance for output rendering.
    """

    # turn your BaseModel into a dict
    cfg_dict = config.model_dump()

    # render YAML
    yaml_str = yaml.safe_dump(cfg_dict, sort_keys=False)
    syntax = Syntax(yaml_str, "yaml")

    # print with rich directly (bypasses standard logger)
    console.print(syntax)