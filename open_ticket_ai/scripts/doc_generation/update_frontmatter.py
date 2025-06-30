"""Update VitePress frontmatter descriptions in Markdown files."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Dict, Tuple

import yaml

_FRONTMATTER_PATTERN = re.compile(r"^---\n(.*?)\n---\n?", re.DOTALL)


def _parse_frontmatter(content: str) -> Tuple[dict, str]:
    """Return the frontmatter and remaining Markdown body from ``content``.

    Args:
        content: The full text of a Markdown file.

    Returns:
        A tuple ``(frontmatter, body)`` where ``frontmatter`` is a dictionary of
        parsed YAML values and ``body`` is the rest of the Markdown content.
    """
    match = _FRONTMATTER_PATTERN.match(content)
    if match:
        frontmatter_text = match.group(1)
        body = content[match.end() :]
        data = yaml.safe_load(frontmatter_text) or {}
        return data, body
    return {}, content


def _dump_frontmatter(data: dict) -> str:
    """Serialize ``data`` as a YAML frontmatter block.

    Args:
        data: Dictionary containing frontmatter key-value pairs.

    Returns:
        String containing the YAML frontmatter block wrapped in '---' delimiters.
    """
    dumped = yaml.safe_dump(data).strip()
    return f"---\n{dumped}\n---\n"


def update_frontmatter(docs_path: Path, summaries: Dict[str, str]) -> None:
    """Update the ``description`` key of Markdown frontmatters.

    Iterates through provided summaries, updating each corresponding Markdown file's
    frontmatter description. Files are skipped if they don't exist.

    Args:
        docs_path: Root directory containing Markdown documentation files.
        summaries: Mapping of file paths (relative to ``docs_path``) to summary text.
                   The summary will be written to each file's frontmatter ``description`` field.

    Notes:
        - Files not found in ``docs_path`` are silently skipped.
        - Existing frontmatter is preserved except for the ``description`` field.
        - Leading newlines in the Markdown body are stripped after frontmatter.
    """
    for rel_path, summary in summaries.items():
        file_path = docs_path / rel_path
        if not file_path.is_file():
            continue

        content = file_path.read_text(encoding="utf-8")
        frontmatter, body = _parse_frontmatter(content)
        frontmatter["description"] = summary.strip()
        new_content = _dump_frontmatter(frontmatter) + body.lstrip("\n")
        file_path.write_text(new_content, encoding="utf-8")