from __future__ import annotations

from pathlib import Path

from openai import AsyncOpenAI


class ReadmeUpdater:
    """Update the AI_README file based on project documentation."""

    def __init__(self, client: AsyncOpenAI, docs_dir: Path, readme_path: Path, model: str) -> None:
        """Store dependencies for later use.

        Args:
            client: Asynchronous OpenAI client.
            docs_dir: Path to the directory containing Markdown documentation.
            readme_path: Path to the AI_README file to update.
            model: Name of the model used for text generation.
        """
        self.client = client
        self.docs_dir = docs_dir
        self.readme_path = readme_path
        self.model = model

    async def update_ai_prompt(self) -> None:
        """Generate a new README from documentation and save it."""
        docs_text: list[str] = []
        for md_file in sorted(self.docs_dir.rglob("*.md")):
            relative = md_file.relative_to(self.docs_dir)
            content = md_file.read_text(encoding="utf-8")
            docs_text.append(f"# FILE: {relative}\n{content}")
        prompt = "\n\n".join(docs_text)
        system_msg = (
            "You maintain the project summary (AI_README.md). "
            "Update it using the following documentation, paying special attention "
            "to files in the /api directory. Return only the updated README in Markdown."
        )
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
        )
        new_content = response.choices[0].message.content
        self.readme_path.write_text(new_content.strip(), encoding="utf-8")
