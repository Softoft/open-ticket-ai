# FILE_PATH: open_ticket_ai\scripts\update_file_path_comments.py
#!/usr/bin/env python3
"""Utility to update FILE_PATH comments in Python files.

This script walks through all Python files in a given directory tree
(excluding ``__init__.py`` files). For each file it removes any lines
starting with ``# FILE_PATH:`` and inserts a new comment as the very
first line with the relative path of the file to the project root.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path

FILE_PATH_PATTERN = re.compile(r"^\s*#\s*FILE_PATH:.*$")


def update_file(file_path: Path, project_root: Path) -> None:
    """Update the FILE_PATH comment of ``file_path``.

    Existing comments that match the ``FILE_PATH_PATTERN`` are removed and a
    single line ``# FILE_PATH: <relative>`` is inserted at the top of the file.
    """
    lines = file_path.read_text().splitlines()
    cleaned = [line for line in lines if not FILE_PATH_PATTERN.match(line)]
    relative = file_path.relative_to(project_root)
    cleaned.insert(0, f"# FILE_PATH: {relative}")
    file_path.write_text("\n".join(cleaned) + "\n")


def process_directory(directory: Path) -> None:
    """Process all Python files under ``directory``."""
    project_root = find_python_code_root_path().parent
    for py_file in directory.rglob("*.py"):
        if py_file.name == "__init__.py":
            continue
        update_file(py_file, project_root)


def main() -> None:
    process_directory(find_python_code_root_path())


if __name__ == "__main__":
    main()
