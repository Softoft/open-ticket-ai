import ast
import os
from pathlib import Path

import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
API_KEY = os.environ.get("OPENROUTER_API_KEY")
MODEL = os.environ.get("OPENROUTER_MODEL", "openrouter/openai/gpt-3.5-turbo")

PROMPT = (
    "Add or update Python docstrings in Google style for all functions, classes,"
    " and modules in the following code. Only add or change docstrings; do not"
    " modify any executable code or formatting. Return only the complete modified"
    " Python file without surrounding explanations."
)

def call_llm(code: str) -> str:
    """Call OpenRouter API with ``code`` and return the modified code."""
    if API_KEY is None:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": f"{PROMPT}\n```python\n{code}\n```"},
        ],
    }
    resp = requests.post(API_URL, headers=headers, json=data, timeout=60)
    resp.raise_for_status()
    content = resp.json()["choices"][0]["message"]["content"]
    return cleanup_llm_output(content)

def cleanup_llm_output(text: str) -> str:
    """Remove markdown code fences from ``text`` if present."""
    lines = text.strip().splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines)

def strip_docstrings(source: str) -> str:
    """Return ``ast.dump`` of ``source`` with all docstrings removed."""
    tree = ast.parse(source)

    def _strip(node: ast.AST) -> None:
        if isinstance(
            node,
            (
                ast.Module,
                ast.ClassDef,
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            ),
        ):
            if (
                node.body
                and isinstance(node.body[0], ast.Expr)
                and isinstance(getattr(node.body[0], "value", None), ast.Constant)
                and isinstance(node.body[0].value.value, str)
            ):
                node.body.pop(0)
        for child in ast.iter_child_nodes(node):
            _strip(child)

    _strip(tree)
    return ast.dump(tree, include_attributes=False)

def docstrings_only_changed(old: str, new: str) -> bool:
    """Return ``True`` if ``old`` and ``new`` differ only in docstrings."""
    return strip_docstrings(old) == strip_docstrings(new)

def process_file(path: Path) -> None:
    """Process a single file ``path``."""
    original = path.read_text()
    try:
        updated = call_llm(original)
    except Exception as exc:
        print(f"Failed to process {path}: {exc}")
        return
    if docstrings_only_changed(original, updated):
        path.write_text(updated)
        print(f"Docstrings updated in {path}")
    else:
        print(f"Non-docstring changes detected in {path}; keeping original")

def main() -> None:
    base_dir = Path(__file__).resolve().parents[2]
    for py_file in base_dir.rglob("*.py"):
        if py_file.resolve() == Path(__file__).resolve():
            continue
        process_file(py_file)

if __name__ == "__main__":
    main()
