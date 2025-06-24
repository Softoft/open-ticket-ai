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
    foo: int
    bar: str


# --- Tests for path_util.find_project_root ---

def test_find_project_root_returns_project_directory():
    project_root = path_util.find_project_root()
    assert project_root.name == "open_ticket_ai"
    # verify that this test file resides inside the found project root
    assert Path(__file__).resolve().is_relative_to(project_root)
    assert (project_root / "config.yml").exists()


def test_find_project_root_invalid_name_raises():
    with pytest.raises(FileNotFoundError):
        path_util.find_project_root("does_not_exist")


# --- Tests for pretty_print_config.pretty_print_config ---

def test_pretty_print_config_outputs_yaml():
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
    schema = create_json_config_schema.RootConfig.model_json_schema()
    assert "open_ticket_ai" in schema.get("properties", {})


def test_schema_file_written(tmp_path, monkeypatch):
    monkeypatch.setattr(path_util, "find_project_root", lambda project_name="open_ticket_ai": tmp_path)
    runpy.run_module(create_json_config_schema.__name__, run_name="__main__")

    out_file = tmp_path / "config.schema.json"
    assert out_file.exists()
    data = json.loads(out_file.read_text())
    assert "open_ticket_ai" in data.get("properties", {})
