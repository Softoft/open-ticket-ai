import asyncio
from types import SimpleNamespace, ModuleType
from pathlib import Path
import sys

# Provide a dummy openai module if it's not installed
if "openai" not in sys.modules:
    dummy = ModuleType("openai")
    dummy.AsyncOpenAI = object
    sys.modules["openai"] = dummy

from open_ticket_ai.scripts.doc_generation.add_docstrings import DocstringGenerator


class MockClient:
    def __init__(self, response_content: str):
        async def create(**kwargs):
            self.called_with = kwargs
            return SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=response_content))]
            )

        self.chat = SimpleNamespace(completions=SimpleNamespace(create=create))


def test_add_docstrings_to_file_content(tmp_path: Path):
    """DocstringGenerator should clean the AI response and use the given client."""
    client = MockClient("""```python
print('updated')
```""")
    gen = DocstringGenerator(client, base_path=tmp_path)
    result = asyncio.run(gen.add_docstrings_to_file_content("print('original')"))

    assert result == "print('updated')"
    assert "Google style" in client.called_with["messages"][1]["content"]


def test_process_file_writes_new_content(tmp_path: Path):
    """process_file should overwrite the file with the AI response."""
    file_path = tmp_path / "example.py"
    file_path.write_text("def foo():\n    pass\n")

    new_content = """```python
def foo():
    \"\"\"Docstring\"\"\"
    pass
```"""

    client = MockClient(new_content)
    gen = DocstringGenerator(client, base_path=tmp_path)

    asyncio.run(gen.process_file(file_path))

    updated = file_path.read_text()
    assert "Docstring" in updated
    assert client.called_with is not None
