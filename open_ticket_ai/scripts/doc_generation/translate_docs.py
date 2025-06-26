from __future__ import annotations

import argparse
import asyncio
import os
from pathlib import Path
from typing import List

from openai import AsyncOpenAI

API_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "meta-llama/llama-3-70b-instruct"
DEFAULT_LANGUAGES = ["de", "en"]


class Translator:
    """Translate Markdown files using an injected OpenAI client."""

    def __init__(self, client: AsyncOpenAI) -> None:
        self.client = client

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
                        "front matter intact."
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
        for md_file in docs_dir.rglob("*.md"):
            await self.process_file(md_file, docs_dir, languages, model, out_dir)


async def main() -> None:
    """CLI entry point for translating a directory of Markdown files."""
    parser = argparse.ArgumentParser(description="Translate Markdown documentation")
    parser.add_argument("--docs-dir", default="vitepress-atc-docs", help="Directory containing markdown docs")
    parser.add_argument("--languages", default=",".join(DEFAULT_LANGUAGES), help="Comma separated target languages")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="OpenRouter model to use")
    parser.add_argument("--out-dir", default="translated-docs", help="Base output directory for translations")

    args = parser.parse_args()
    api_key = os.environ.get("OPEN_ROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = AsyncOpenAI(base_url=API_URL, api_key=api_key)
    translator = Translator(client)

    docs_dir = Path(args.docs_dir)
    out_dir = Path(args.out_dir)
    languages = [l.strip() for l in args.languages.split(",") if l.strip()]
    await translator.translate_directory(docs_dir, languages, args.model, out_dir)


if __name__ == "__main__":
    asyncio.run(main())

