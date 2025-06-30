"""
This module provides a facade for generating and translating documentation.

It includes functionality to:
- Generate docstrings for Python source code using AI models
- Convert documented code into structured Markdown API references
- Translate documentation files into multiple languages

The module can be executed as a script to run the full documentation generation
and translation workflow.
"""

import asyncio
import json
import os
from pathlib import Path

from openai import AsyncOpenAI
from rich.console import Console
import typer

from open_ticket_ai.scripts import ReadmeUpdater
from open_ticket_ai.scripts.doc_generation.add_docstrings import DocstringGenerator
from open_ticket_ai.scripts.doc_generation.generate_api_reference import generate_markdown
from open_ticket_ai.scripts.doc_generation.generate_multi_lang_docs import Translator
from open_ticket_ai.scripts.doc_generation.update_frontmatter import update_frontmatter
from open_ticket_ai.scripts.documentation_summary import DocumentationSummarizer
from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path

# --- CLI Setup ---
app = typer.Typer(
    name="doc-gen",
    help="A CLI tool to automate the generation and maintenance of project documentation.",
    add_completion=False,
)
console = Console()


class DocGenerationFacade:
    """
    Facade for generating documentation from Python code.
    This class provides a simple interface to generate markdown files
    from Python source code, excluding specified directories and files.
    """

    def __init__(self, client: AsyncOpenAI) -> None:
        """Initializes the DocGenerationFacade with an AsyncOpenAI client.

        Args:
            client (AsyncOpenAI): The asynchronous OpenAI client to use for API calls.
        """
        self.client = client

    async def generate_docstrings(
        self,
        base_path: Path,
        exclude_dirs: set[str],
        exclude_files: set[str],
        model: str,
    ):
        """
        Generates docstrings for Python files in the specified directory tree.

        This method walks through the directory structure starting at `base_path`,
        processes all Python files (excluding specified directories and files), and
        adds missing docstrings using an AI model.

        Args:
            base_path: Root directory to start searching for Python files.
            exclude_dirs: Set of directory names to exclude from processing.
            exclude_files: Set of file names to exclude from processing.
            model: Identifier of the AI model to use for docstring generation.
        """
        # --- Configuration ---

        docstring_generator = DocstringGenerator(
            self.client,
            base_path,
            exclude_dirs,
            exclude_files,
            model,
        )
        await docstring_generator.run()

    def generate_markdown(
        self,
        patterns_to_output_map: dict[str, Path],
        excluded: list[str],
    ):
        """Generate markdown files from Python code based on provided patterns.

        Args:
            patterns_to_output_map: A dictionary mapping glob patterns to output file paths.
                Each pattern will be used to find matching files, and the corresponding
                output path specifies where the generated markdown should be saved.
            excluded: A list of glob patterns to exclude from processing.
        """

        generate_markdown(
            find_python_code_root_path(),
            patterns_to_output_map,
            excluded=excluded,
        )

    async def translate_docs(
        self,
        docs_dir: Path,
        base_language: str,
        languages: list[str],
        model: str,
        out_dir: Path,
    ):
        """
        Translates documentation files to multiple target languages.

        Processes all files in the source directory, translating them from the base language
        to each specified target language using an AI model.

        Args:
            docs_dir: Directory containing source documentation files.
            base_language: Language code of the source documentation (e.g., 'en').
            languages: List of target language codes to translate to.
            model: Identifier of the AI model to use for translation.
            out_dir: Output directory for translated files.
        """
        translator = Translator(self.client, base_language)
        await translator.translate_directory(docs_dir, languages, model, out_dir)


# --- Global Configurations & Instances ---
try:
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPEN_ROUTER_API_KEY environment variable not set.")
    base_url = "https://openrouter.ai/api/v1"
    client = AsyncOpenAI(api_key=api_key, base_url=base_url)
    generator = DocGenerationFacade(client)
except (ValueError, ImportError) as e:
    console.print(f"[bold red]Error initializing application: {e}[/bold red]")
    # Exit if essential configuration is missing
    raise typer.Exit(code=1) from e

root_project_path = find_python_code_root_path().parent
docs_temp_api = root_project_path / "docs" / "original_source" / "api"
docs_src_path = root_project_path / "docs" / "vitepress_docs" / "docs_src"
original_source_path = root_project_path / "docs" / "original_source"
summary_file_path = root_project_path / "docs" / "_documentation_summaries.json"

EXCLUDE_DIRS = {
    ".venv", "__pycache__", "build", "dist", "docs_temp_api",
    "vitepress-atc-docs_temp_api", ".idea", ".github", "node_modules",
}
EXCLUDE_FILES = {"__init__.py"}
DEFAULT_MODEL = "google/gemini-2.5-pro"


# --- Reusable Core Functions for CLI ---
async def _generate_reference_api_markdown(model: str):
    """Generates API reference documentation in Markdown format."""
    await generator.generate_docstrings(
        find_python_code_root_path(), EXCLUDE_DIRS, EXCLUDE_FILES, model=model,
    )
    generator.generate_markdown(
        {
            "**/ce/core/config/**/*.py": docs_temp_api / "core" / "ce_core_config.md",
            "**/ce/core/dependency_injection/**/*.py": docs_temp_api / "core" / "di.md",
            "**/ce/core/mixins/**/*.py": docs_temp_api / "core" / "mixins.md",
            "**/ce/core/util/**/*.py": docs_temp_api / "core" / "util.md",
            "**/ce/run/pipe_implementations/*.py": docs_temp_api / "run" / "pipes.md",
            "**/ce/run/pipeline/*.py": docs_temp_api / "run" / "pipeline.md",
            "**/ce/run/managers/*.py": docs_temp_api / "run" / "managers.md",
            "**/ce/ticket_system_integration/*.py": docs_temp_api / "run" / "ticket_system_integration.md",
            "**/ce/*.py": docs_temp_api / "main.md",
        },
        excluded=["**/tests/**", "**/migrations/**", "**/__init__.py"],
    )


async def _create_documentation_summaries(model: str) -> dict:
    """Creates summaries for documentation files."""
    summarizer = DocumentationSummarizer(client, original_source_path)
    summaries = await summarizer.create_summary_dict(model=model)
    summary_file_path.write_text(json.dumps(summaries, indent=2), encoding="utf-8")
    return summaries


def _add_frontmatter_meta_seo_descriptions(summaries: dict):
    """Updates the frontmatter of Markdown files with SEO descriptions."""
    update_frontmatter(original_source_path, summaries)


async def _translate_to_multi_lang_docs(model: str):
    """Translates documentation files to multiple languages."""
    await generator.translate_docs(
        original_source_path, "en", ["en", "de"], model, docs_src_path,
    )


async def _update_ai_readme(model: str):
    """Updates the AI-generated README file."""
    updater = ReadmeUpdater(
        client,
        docs_src_path / "en",
        root_project_path / "AI_README.md",
        model=model,
    )
    await updater.update_ai_prompt()


# --- CLI Commands ---
@app.command(name="api-docs")
def generate_api_docs_command(
    model: str = typer.Option(
        DEFAULT_MODEL, "--model", "-m", help="AI model for docstring generation.",
    )
):
    """Generates docstrings and converts them to API reference markdown files."""
    console.print(f"Generating API docs using [bold cyan]{model}[/bold cyan]...")
    asyncio.run(_generate_reference_api_markdown(model))
    console.print("[bold green]✅ API reference documentation generated.[/bold green]")


@app.command(name="create-summaries")
def create_summaries_command(
    model: str = typer.Option(
        DEFAULT_MODEL, "--model", "-m", help="AI model for creating summaries.",
    )
):
    """Creates SEO-optimized summaries for all documentation files."""
    console.print(f"Creating summaries using [bold cyan]{model}[/bold cyan]...")
    asyncio.run(_create_documentation_summaries(model))
    console.print(f"[bold green]✅ Summaries created and saved to {summary_file_path}[/bold green]")


@app.command(name="add-frontmatter")
def add_frontmatter_command():
    """Adds SEO descriptions from the summary file to docs frontmatter."""
    if not summary_file_path.exists():
        console.print(f"[bold red]Error: Summary file not found at {summary_file_path}[/bold red]")
        console.print("Please run the 'create-summaries' command first.")
        raise typer.Exit(1)

    console.print("Loading summaries and adding to frontmatter...")
    summaries = json.loads(summary_file_path.read_text(encoding="utf-8"))
    _add_frontmatter_meta_seo_descriptions(summaries)
    console.print("[bold green]✅ Frontmatter updated successfully.[/bold green]")


@app.command(name="translate")
def translate_command(
    model: str = typer.Option(
        DEFAULT_MODEL, "--model", "-m", help="AI model for translation.",
    )
):
    """Translates documentation into multiple languages (en, de)."""
    console.print(f"Translating docs using [bold cyan]{model}[/bold cyan]...")
    asyncio.run(_translate_to_multi_lang_docs(model))
    console.print("[bold green]✅ Documentation translated successfully.[/bold green]")


@app.command(name="update-readme")
def update_readme_command(
    model: str = typer.Option(
        DEFAULT_MODEL, "--model", "-m", help="AI model to update the README.",
    )
):
    """Updates the main AI_README.md file based on current docs."""
    console.print(f"Updating AI_README.md using [bold cyan]{model}[/bold cyan]...")
    asyncio.run(_update_ai_readme(model))
    console.print("[bold green]✅ AI_README.md updated successfully.[/bold green]")


@app.command(name="all")
def run_all_pipeline(
    model: str = typer.Option(
        DEFAULT_MODEL, "--model", "-m", help="AI model to use for all steps.",
    )
):
    """Runs the entire documentation generation and translation pipeline."""
    console.rule(f"[bold yellow]🚀 Starting Full Documentation Pipeline ({model}) 🚀[/bold yellow]")

    # 1. Generate API Docs
    console.print("\n[bold]Step 1 of 5: Generating API Docs...[/bold]")
    asyncio.run(_generate_reference_api_markdown(model))
    console.print("[green]✅ API docs generated.[/green]")

    # 2. Create Summaries
    console.print("\n[bold]Step 2 of 5: Creating Documentation Summaries...[/bold]")
    summaries = asyncio.run(_create_documentation_summaries(model))
    console.print("[green]✅ Summaries created.[/green]")

    # 3. Add Frontmatter
    console.print("\n[bold]Step 3 of 5: Adding Frontmatter to Docs...[/bold]")
    _add_frontmatter_meta_seo_descriptions(summaries)
    console.print("[green]✅ Frontmatter updated.[/green]")

    # 4. Translate Docs
    console.print("\n[bold]Step 4 of 5: Translating Documentation...[/bold]")
    asyncio.run(_translate_to_multi_lang_docs(model))
    console.print("[green]✅ Docs translated.[/green]")

    # 5. Update README
    console.print("\n[bold]Step 5 of 5: Updating AI README...[/bold]")
    asyncio.run(_update_ai_readme(model))
    console.print("[green]✅ AI README updated.[/green]")

    console.rule("[bold green]🎉 Documentation Pipeline Finished Successfully! 🎉[/bold green]")


if __name__ == "__main__":
    app()