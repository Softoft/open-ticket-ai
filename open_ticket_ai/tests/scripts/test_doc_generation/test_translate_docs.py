"""This module contains unit tests for the Translator class used in generating multi-language documentation.

The tests cover:
- The translation of text using an external API client.
- The processing of Markdown files to generate translated versions.
"""
import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from open_ticket_ai.scripts.doc_generation.generate_multi_lang_docs import Translator


@pytest.mark.asyncio
async def test_translate_text_calls_client():
    """Tests that Translator.translate_text correctly interacts with the OpenAI client.

    This test verifies:
    1. The method properly calls the OpenAI chat completions API
    2. The API response is correctly processed to extract translated content
    3. The returned value matches the expected translation
    4. The API client is called exactly once with proper arguments

    Mocks:
    - Creates a mock OpenAI client with chained attributes
    - Configures async completions.create method to return a fixed response
    """
    client = Mock()
    client.chat = Mock()
    client.chat.completions = Mock()
    client.chat.completions.create = AsyncMock(
        return_value=Mock(choices=[Mock(message=Mock(content="translated"))])
    )

    result = await translator.translate_text("hello", "de", "test-model")

    assert result == "translated"
    client.chat.completions.create.assert_called_once()


@pytest.mark.asyncio
async def test_process_file_writes_translated_content(tmp_path: Path):
    """Tests end-to-end file processing workflow of Translator.process_file.

    Verifies:
    1. Creates source Markdown file with front matter and content
    2. Mocks translation to return expected German output
    3. Checks translated file is created in correct output directory
    4. Validates file content matches expected translation
    5. Confirms translate_text was called with proper arguments

    Args:
        tmp_path: Pytest fixture providing temporary directory path

    File Structure:
    - Creates src/doc.md with test content
    - Processes file for German translation
    - Expects output in out/de/doc.md
    """
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    md_file = src_dir / "doc.md"
    md_file.write_text("---\ntitle: Test\n---\n\ncontent", encoding="utf-8")

    out_dir = tmp_path / "out"

    translator.translate_text = AsyncMock(return_value="---\ntitle: Test\n---\n\nübersetzt")

    await translator.process_file(md_file, src_dir, ["de"], "model", out_dir)

    out_file = out_dir / "de" / "doc.md"
    assert out_file.exists()
    assert out_file.read_text(encoding="utf-8") == "---\ntitle: Test\n---\n\nübersetzt"
    translator.translate_text.assert_awaited_once_with("---\ntitle: Test\n---\n\ncontent", "de", "model")