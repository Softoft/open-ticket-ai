import os
import asyncio
import re
from pathlib import Path
from openai import AsyncOpenAI

"""Automatically adds long Google style docstrings to Python files using AI."""

# --- Configuration ---
BASE_PATH = Path(__file__).parent.parent.parent
EXCLUDE_DIRS = {
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "docs",
    "vitepress-atc-docs",
    ".idea",
    ".github",
    "node_modules",
}
EXCLUDE_FILES = {"__init__.py"}


class DocstringGenerator:
    """Generate docstrings for Python files using an injected AsyncOpenAI client."""

    def __init__(self, client: AsyncOpenAI, base_path: Path = BASE_PATH):
        self.client = client
        self.base_path = base_path

    def find_python_files(self) -> list[Path]:
        """Return all Python files in ``base_path`` respecting exclusion rules."""
        py_files = []
        for item in self.base_path.rglob("*.py"):
            if (
                not any(part in EXCLUDE_DIRS for part in item.parts)
                and item.name not in EXCLUDE_FILES
            ):
                py_files.append(item)
        print(f"Found {len(py_files)} Python files to process.")
        return py_files

    @staticmethod
    def clean_ai_response(response_text: str) -> str:
        """Extract Python code from a response that may contain Markdown fences."""
        code_block_pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)
        match = code_block_pattern.search(response_text)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    async def add_docstrings_to_file_content(self, file_content: str) -> str | None:
        """Send file content to the AI model and return the updated version."""
        prompt = f"""
        You are an expert Python programmer tasked with improving code documentation.
        The following is a complete Python file. Add long, descriptive docstrings
        to all classes and functions that are missing them. Use **Google style** docstrings
        and format the docstring content using Markdown.

        IMPORTANT INSTRUCTIONS:
        1.  Return the ENTIRE, complete file content with your additions.
        2.  Do NOT change any existing code logic. Only add docstrings where they are needed.
        3.  Your response must ONLY be the raw Python code for the modified file. Do not add
            any commentary, explanations or markdown fences around it.

        Here is the file content:
        ```python
        {file_content}
        ```
        """
        try:
            response = await self.client.chat.completions.create(
                model="deepseek/deepseek-r1-0528",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful Python assistant that adds docstrings to code."
                        ),
                    },
                    {"role": "user", "content": prompt},
                ],
                temperature=0.1,
            )
            new_content = response.choices[0].message.content
            return self.clean_ai_response(new_content)
        except Exception as exc:  # pragma: no cover - guard for unexpected failures
            print(f"Error calling AI model: {exc}")
            return None

    async def process_file(self, file_path: Path) -> None:
        """Process a single Python file in place."""
        print(f"-> Processing: {file_path}")
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                original_content = f.read()

            if not original_content.strip():
                print(f"   - Skipping empty file: {file_path}")
                return

            print("   - Sending to AI for docstring generation...")
            new_content = await self.add_docstrings_to_file_content(original_content)

            if new_content and new_content != original_content:
                print("   - AI returned updated content. Writing to file.")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"   - Successfully updated: {file_path}")
            elif not new_content:
                print(f"   - Failed to get a valid response from AI for {file_path}.")
            else:
                print(f"   - No changes were made by the AI for {file_path}.")
        except Exception as exc:  # pragma: no cover - safeguard around file ops
            print(f"   - Could not process file {file_path}: {exc}")

    async def run(self) -> None:
        """Run the docstring generation over all discovered Python files."""
        print("Starting docstring generation using whole-file processing...")
        py_files = self.find_python_files()

        if not py_files:
            print("No Python files found to process. Exiting.")
            return

        tasks = [self.process_file(file) for file in py_files]
        await asyncio.gather(*tasks)
        print("\nAll files processed. Docstring generation complete.")


async def main() -> None:
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
    if not api_key:
        print("Error: The 'OPEN_ROUTER_API_KEY' environment variable is not set.")
        print("Please set the variable and run the script again.")
        return

    client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1", api_key=api_key)
    generator = DocstringGenerator(client)
    await generator.run()


if __name__ == "__main__":
    asyncio.run(main())
