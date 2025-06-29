from __future__ import annotations

import asyncio
from pathlib import Path
from typing import Any

from openai import AsyncOpenAI


class DocumentationSummarizer:
    """Generate summaries for markdown documentation files using OpenAI."""

    def __init__(self, client: AsyncOpenAI, docs_dir: Path) -> None:
        """Initialize the summarizer.

        Args:
            client: Asynchronous OpenAI client used for API calls.
            docs_dir: Path to the directory containing markdown documentation.
        """
        self.client = client
        self.docs_dir = docs_dir

    async def summarize_file(self, path: Path, model: str) -> str:
        """Return a summary for a single markdown file.

        Args:
            path: Path to the markdown file.
            model: OpenAI model identifier.
        """
        text = path.read_text(encoding="utf-8")
        response: Any = await self.client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful assistant that summarizes documentation files."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Write a Meta SEO optimized description of this document,"
                               f"only return the summary as a plain text and nothing else"
                               f" \n{text}",
                },
            ],
            temperature=0.2,
        )
        return str(response.choices[0].message.content).strip()

    async def create_summary_dict(self, model: str) -> dict[str, str]:
        """Create a mapping of relative file paths to summaries.

        Walks ``docs_dir`` recursively, summarizing all ``.md`` files.

        Args:
            model: OpenAI model identifier used for summarization.
        """
        tasks = []
        paths: list[Path] = []
        for md_file in self.docs_dir.rglob("*.md"):
            paths.append(md_file)
            tasks.append(self.summarize_file(md_file, model))
        summaries = await asyncio.gather(*tasks)
        summary_dict = {
            str(p.relative_to(self.docs_dir)): s for p, s in zip(paths, summaries)
        }
        return summary_dict
