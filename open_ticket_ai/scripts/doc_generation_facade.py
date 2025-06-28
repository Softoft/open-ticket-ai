import asyncio
import os
from pathlib import Path

from openai import AsyncOpenAI

from open_ticket_ai.scripts.doc_generation.add_docstrings import DocstringGenerator
from open_ticket_ai.scripts.doc_generation.generate_api_reference import generate_markdown
from open_ticket_ai.scripts.doc_generation.generate_multi_lang_docs import Translator
from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path


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
            model
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


api_key = os.getenv("OPEN_ROUTER_API_KEY")
base_url = "https://openrouter.ai/api/v1"
client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url,
)
generator = DocGenerationFacade(client)
root_project_path = find_python_code_root_path().parent

docs_temp_api = root_project_path / "docs" / "original_source" / "api"

EXCLUDE_DIRS = {
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "docs_temp_api",
    "vitepress-atc-docs_temp_api",
    ".idea",
    ".github",
    "node_modules",
}
EXCLUDE_FILES = {"__init__.py"}


async def generate_reference_api_markdown():
    """
    Generates API reference documentation in Markdown format.

    This function:
    1. Adds docstrings to Python files in the project
    2. Converts the documented code into structured Markdown files
    3. Organizes output by module/functionality categories

    Output files are saved in a temporary directory for API documentation.
    """
    await generator.generate_docstrings(
        find_python_code_root_path(),
        EXCLUDE_DIRS,
        EXCLUDE_FILES,
        model="deepseek/deepseek-r1-0528",
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


async def translate_to_multi_lang_docs():
    """
    Translates documentation files to multiple languages.

    Processes documentation files in the source directory, translating them from
    English to specified target languages. Outputs translated files to the Vitepress
    documentation source directory.
    """
    await generator.translate_docs(
        root_project_path / "docs" / "original_source",
        "en",
        ["en", "de"],
        "deepseek/deepseek-r1-0528",
        root_project_path / "docs" / "vitepress_docs" / "docs_src",
    )


if __name__ == '__main__':
    asyncio.run(generate_reference_api_markdown())
    asyncio.run(translate_to_multi_lang_docs())
