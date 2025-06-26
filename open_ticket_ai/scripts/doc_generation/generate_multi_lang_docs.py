from __future__ import annotations

import asyncio
from pathlib import Path
from typing import List

from openai import AsyncOpenAI
import tenacity
from tenacity import stop_after_attempt, wait_exponential

# TODO update, dir structure changed, other languages arent in direrct super dir but instead are in parent parent / version / lang

class Translator:
    """Translate Markdown files using an injected OpenAI client."""

    def __init__(self, client: AsyncOpenAI, base_language: str) -> None:
        """Initializes the Translator instance.

        Args:
            client: An asynchronous OpenAI client instance for API interactions.
            base_language: Language code (e.g., 'en') representing the source language of documents.
        """
        self.client = client
        self.base_language = base_language

    @tenacity.retry(
        wait=wait_exponential(multiplier=2, min=2, max=60),
        stop=stop_after_attempt(6),
    )
    async def translate_text(self, content: str, target_lang: str, model: str) -> str:
        """Translate ``content`` to ``target_lang`` using ``model``."""
        response = await self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful translator. Translate the user's markdown "
                        "into the requested language while keeping markdown and YAML "
                        "front matter intact. Only return the translated markdown dont wrap in"
                        "```de. Also Keep HTML tags, code blocks."
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
        """Translate a Markdown file into multiple languages."""
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
        """Translate all Markdown files in ``docs_dir``."""
        tasks = []
        for md_file in docs_dir.rglob("*.md"):
            tasks.append(self.process_file(md_file, docs_dir, languages, model, out_dir))
        await asyncio.gather(*tasks)