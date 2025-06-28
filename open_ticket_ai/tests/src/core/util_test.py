"""Tests for the `core.util` module.

This module contains unit tests for the utility functions and configuration handling
in the `core.util` module of the `open_ticket_ai` project.

The tests are organized into three main sections:

1. **Tests for `path_util.find_project_root`**:
   - Verifies that the project root is correctly identified.
   - Checks error handling when the project name is invalid.

2. **Tests for `pretty_print_config.pretty_print_config`**:
   - Ensures that the configuration is printed in the expected YAML format.

3. **Tests for `create_json_config_schema`**:
   - Validates the structure of the generated JSON schema.
   - Checks that the schema file is correctly written to the filesystem.

These tests use `pytest` and rely on fixtures for temporary directories and environment patching.
"""
import json
import runpy
from types import SimpleNamespace
from pathlib import Path

import pytest
import yaml
from rich.syntax import Syntax

from open_ticket_ai.src.ce.core.util import path_util, pretty_print_config, create_json_config_schema
from pydantic import BaseModel


class DummyModel(BaseModel):
    """A dummy Pydantic model for testing purposes.

    Attributes:
        foo (int): An integer attribute for testing.
        bar (str): A string attribute for testing.
    """
    foo: int
    bar: str


# --- Tests for path_util.find_project_root ---

def test_find_project_root_returns_project_directory():
    """Tests that find_project_root correctly identifies the project root directory.

    Verifies:
        - The found directory has the expected name
        - The current test file resides within the found directory
        - The expected config file exists in the root directory
    """
    project_root = path_util.find_python_code_root_path()
    assert project_root.name == "open_ticket_ai"
    # verify that this test file resides inside the found project root
    assert Path(__file__).resolve().is_relative_to(project_root)
    assert (project_root / "config.yml").exists()


def test_find_project_root_invalid_name_raises():
    """Tests that find_project_root raises FileNotFoundError with invalid project name.

    Verifies:
        - FileNotFoundError is raised when an invalid project name is provided.
    """
    with pytest.raises(FileNotFoundError):
        path_util.find_python_code_root_path("does_not_exist")


# --- Tests for pretty_print_config.pretty_print_config ---

def test_pretty_print_config_outputs_yaml():
    """Tests that pretty_print_config outputs configuration as expected YAML.

    Verifies:
        - Output contains exactly one element
        - Output element is a Syntax object
        - Output YAML matches the expected serialized configuration
    """
    printed = []
    fake_console = SimpleNamespace(print=lambda x: printed.append(x))

    cfg = DummyModel(foo=1, bar="baz")
    pretty_print_config.pretty_print_config(cfg, fake_console)

    assert len(printed) == 1
    arg = printed[0]
    assert isinstance(arg, Syntax)
    expected_yaml = yaml.safe_dump(cfg.model_dump(), sort_keys=False)
    assert arg.code == expected_yaml


# --- Tests for create_json_config_schema ---

def test_root_config_schema_contains_open_ticket_ai():
    """Tests that the generated JSON schema contains the expected 'open_ticket_ai' property.

    Verifies:
        - The 'open_ticket_ai' property exists in the schema's properties.
    """
    schema = create_json_config_schema.RootConfig.model_json_schema()
    assert "open_ticket_ai" in schema.get("properties", {})


def test_schema_file_written(tmp_path, monkeypatch):
    """Tests that the JSON schema file is correctly generated and written.

    Args:
        tmp_path: Pytest fixture for temporary directory
        monkeypatch: Pytest fixture for modifying environment

    Verifies:
        - Output file exists in expected location
        - Output file contains the expected 'open_ticket_ai' property
    """
    monkeypatch.setattr(path_util, "find_project_root", lambda project_name="open_ticket_ai": tmp_path)
    runpy.run_module(create_json_config_schema.__name__, run_name="__main__")

    out_file = tmp_path / "config.schema.json"
    assert out_file.exists()
    data = json.loads(out_file.read_text())
    assert "open_ticket_ai" in data.get("properties", {))