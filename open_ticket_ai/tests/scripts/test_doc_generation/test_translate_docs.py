import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from open_ticket_ai.scripts.doc_generation.translate_docs import Translator


@pytest.mark.asyncio
async def test_translate_text_calls_client():
    client = Mock()
    client.chat = Mock()
    client.chat.completions = Mock()
    client.chat.completions.create = AsyncMock(
        return_value=Mock(choices=[Mock(message=Mock(content="translated"))])
    )

    translator = Translator(client)
    result = await translator.translate_text("hello", "de", "test-model")

    assert result == "translated"
    client.chat.completions.create.assert_called_once()


@pytest.mark.asyncio
async def test_process_file_writes_translated_content(tmp_path: Path):
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    md_file = src_dir / "doc.md"
    md_file.write_text("---\ntitle: Test\n---\n\ncontent", encoding="utf-8")

    out_dir = tmp_path / "out"

    translator = Translator(Mock())
    translator.translate_text = AsyncMock(return_value="---\ntitle: Test\n---\n\nübersetzt")

    await translator.process_file(md_file, src_dir, ["de"], "model", out_dir)

    out_file = out_dir / "de" / "doc.md"
    assert out_file.exists()
    assert out_file.read_text(encoding="utf-8") == "---\ntitle: Test\n---\n\nübersetzt"
    translator.translate_text.assert_awaited_once_with("---\ntitle: Test\n---\n\ncontent", "de", "model")
