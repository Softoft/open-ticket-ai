# FILE_PATH: open_ticket_ai\src\ce\core\util\pretty_print_config.py
"""Module for pretty printing configuration objects.

This module provides functionality to display Pydantic configuration models in a
nicely formatted and syntax highlighted way using the `rich` library. It converts
Pydantic models to YAML format and applies syntax highlighting for improved readability.

Features:
- Converts Pydantic `BaseModel` instances to dictionaries
- Serializes configuration data to YAML format
- Applies YAML syntax highlighting using `rich`
- Prints highlighted output to console
"""

import logging

import yaml
from pydantic import BaseModel
from rich.console import Console
from rich.syntax import Syntax

logger = logging.getLogger(__name__)

def pretty_print_config(config: BaseModel, console: Console):
    """Pretty print a pydantic model using `rich`.

    This function converts a Pydantic `BaseModel` to a dictionary, serializes it to YAML,
    and prints it to the console using `rich`'s syntax highlighting. The output is formatted
    with YAML syntax highlighting for improved readability.

    The process involves:
        1. Converting the Pydantic model to a dictionary using `model_dump()`
        2. Serializing the dictionary to a YAML string
        3. Creating a rich `Syntax` object with YAML highlighting
        4. Printing the highlighted YAML to the console

    Note that this function bypasses standard logging and outputs directly to the console
    using `rich`'s printing capabilities for optimal formatting.

    Args:
        config (`BaseModel`): The Pydantic model configuration to display.
        console (`Console`): The rich console instance for output rendering.
    """

    # turn your BaseModel into a dict
    cfg_dict = config.model_dump()

    # render YAML
    yaml_str = yaml.safe_dump(cfg_dict, sort_keys=False)
    syntax = Syntax(yaml_str, "yaml")

    # print with rich directly (bypasses standard logger)
    console.print(syntax)
