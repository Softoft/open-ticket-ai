# FILE_PATH: open_ticket_ai\scripts\doc_generation\generate_multi_lang_docs.py
from __future__ import annotations

import asyncio
from pathlib import Path
from typing import List

import tenacity
from openai import AsyncOpenAI
from tenacity import stop_after_attempt, wait_exponential

# TODO update, dir structure changed, other languages arent in direrct super dir but instead are in parent parent / version / lang

class Translator:
    """Translate Markdown files using an injected OpenAI client."""

    def __init__(
        self,
        client: AsyncOpenAI,
        base_language: str,
        translation_file_path: Path = None
    ) -> None:
        """Initializes the Translator instance.

        Args:
            client: An asynchronous OpenAI client instance for API interactions.
            base_language: Language code (e.g., 'en') representing the source language of documents.
            translation_file_path: Path to a file containing the translation instruction for the system prompt.
                If not provided, defaults to "translation_instruction.txt" in the same directory as this module.
        """
        if translation_file_path is None:
            translation_file_path = Path(__file__).parent / "translation_instruction.txt"
        self.client = client
        self.base_language = base_language
        self.translation_instruction = translation_file_path.read_text(encoding="utf-8").strip()

    @tenacity.retry(
        wait=wait_exponential(multiplier=2, min=2, max=60),
        stop=stop_after_attempt(6),
    )
    async def translate_text(self, content: str, target_lang: str, model: str) -> str:
        """Translates Markdown content to a target language using OpenAI's API.

        This method uses exponential backoff and retries up to 6 times on failure.

        Args:
            content: The Markdown text to translate.
            target_lang: Target language code (e.g., 'es' for Spanish).
            model: OpenAI model identifier to use for translation.

        Returns:
            The translated Markdown content as a string.

        Raises:
            tenacity.RetryError: If all retry attempts fail.
        """
        response = await self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        self.translation_instruction
                    ),
                },
                {
                    "role": "user",
                    "content": f"Translate the following markdown to {target_lang}:\n\n{content}",
                },
            ],
            temperature=0.2,
        )
        return response.choices[0].message.content

    async def process_file(
        self,
        path: Path,
        root: Path,
        languages: List[str],
        model: str,
        out_dir: Path,
    ) -> None:
        """Processes a single Markdown file for translation into multiple languages.

        For each target language:
        1. Reads the source Markdown file
        2. Translates content (skips translation for base language)
        3. Writes translated content to appropriate output path

        Args:
            path: Absolute path to the source Markdown file.
            root: Root directory of the documentation source tree.
            languages: List of target language codes to translate into.
            model: OpenAI model identifier for translation.
            out_dir: Base output directory for translated files.
        """
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root)
        for lang in languages:
            if lang == self.base_language:
                translated = text
            else:
                translated = await self.translate_text(text, lang, model)
            out_file = out_dir / lang / relative
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(translated, encoding="utf-8")
            print(f"Wrote {out_file}")

    async def translate_directory(
        self,
        docs_dir: Path,
        languages: List[str],
        model: str,
        out_dir: Path,
    ) -> None:
        """Translates an entire directory of Markdown files concurrently.

        Walks through all `.md` files in `docs_dir`, creates translation tasks
        for each file, and processes them asynchronously.

        Args:
            docs_dir: Directory containing source Markdown files.
            languages: List of target language codes for translation.
            model: OpenAI model identifier for translation.
            out_dir: Base output directory for translated files.
        """
        tasks = []
        for md_file in docs_dir.rglob("*.md"):
            tasks.append(self.process_file(md_file, docs_dir, languages, model, out_dir))
        await asyncio.gather(*tasks)
