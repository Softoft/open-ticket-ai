import os
import asyncio
import re
from openai import AsyncOpenAI
from pathlib import Path

# --- Configuration ---

# Set the base path to the root of your project
BASE_PATH = Path(__file__).parent.parent.parent
# Directories to exclude
EXCLUDE_DIRS = {
    '.venv', '__pycache__', 'build', 'dist', 'docs',
    'vitepress-atc-docs', '.idea', '.github', 'node_modules'
}
# Files to exclude
EXCLUDE_FILES = {'__init__.py'}

# Configure the OpenAI client to use OpenRouter
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_API_KEY"),
)


# --- Main Logic ---

def find_python_files(path: Path) -> list[Path]:
    """
    Recursively finds all Python files in a given path, respecting exclusion rules.
    """
    py_files = []
    for item in path.rglob('*.py'):
        if (
            not any(part in EXCLUDE_DIRS for part in item.parts) and
            item.name not in EXCLUDE_FILES
        ):
            py_files.append(item)
    print(f"Found {len(py_files)} Python files to process.")
    return py_files


def clean_ai_response(response_text: str) -> str:
    """
    Cleans the AI's response to ensure it's only valid Python code.
    It removes markdown code fences and any leading/trailing text.
    """
    # Pattern to find a python code block
    code_block_pattern = re.compile(r"```python\n(.*?)\n```", re.DOTALL)
    match = code_block_pattern.search(response_text)

    if match:
        return match.group(1).strip()

    # If no markdown block is found, assume the whole response is code
    return response_text.strip()


async def add_docstrings_to_file_content(file_content: str) -> str | None:
    """
    Sends the entire file content to an AI model to add missing docstrings.

    Args:
        file_content: A string containing the entire source code of a Python file.

    Returns:
        The updated file content with docstrings, or None if it fails.
    """
    prompt = f"""
    You are an expert Python programmer tasked with improving code documentation.
    The following is a complete Python file. Your task is to add professional,
    Google-style docstrings to all classes and functions that are missing them.

    IMPORTANT INSTRUCTIONS:
    1.  Return the ENTIRE, complete file content with your additions.
    2.  Do NOT change any existing code logic. Only add docstrings where they are needed.
    3.  Your response must ONLY be the raw Python code for the modified file. Do not add
        any commentary, explanations, or markdown formatting like ```python ... ```.

    Here is the file content:
    ```python
    {file_content}
    ```
    """
    try:
        response = await client.chat.completions.create(
            model="meta-llama/llama-3-70b-instruct",
            messages=[
                {"role": "system",
                 "content": "You are a helpful Python assistant that adds docstrings to code."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,  # Low temperature for deterministic code generation
            max_tokens=4000,  # Adjust as needed for larger files
        )
        new_content = response.choices[0].message.content
        return clean_ai_response(new_content)
    except Exception as e:
        print(f"Error calling AI model: {e}")
        return None


async def process_file(file_path: Path):
    """
    Processes a single Python file by sending it to the AI for docstring
    addition and overwriting the file with the result.

    Args:
        file_path: The path to the Python file to process.
    """
    print(f"-> Processing: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Skip files that are empty or just whitespace
        if not original_content.strip():
            print(f"   - Skipping empty file: {file_path}")
            return

        print(f"   - Sending to AI for docstring generation...")
        new_content = await add_docstrings_to_file_content(original_content)

        if new_content and new_content != original_content:
            print(f"   - AI returned updated content. Writing to file.")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"   - Successfully updated: {file_path}")
        elif not new_content:
            print(f"   - Failed to get a valid response from AI for {file_path}.")
        else:
            print(f"   - No changes were made by the AI for {file_path}.")

    except Exception as e:
        print(f"   - Could not process file {file_path}: {e}")


async def main():
    """
    Main asynchronous function to orchestrate the docstring generation process.
    """
    print("Starting docstring generation using whole-file processing...")
    py_files = find_python_files(BASE_PATH)

    if not py_files:
        print("No Python files found to process. Exiting.")
        return

    tasks = [process_file(file) for file in py_files]
    await asyncio.gather(*tasks)
    print("\nAll files processed. Docstring generation complete.")


if __name__ == "__main__":
    api_key = os.getenv("OPEN_ROUTER_API_KEY")
    if not api_key:
        print("Error: The 'OPENROUTER_API_KEY' environment variable is not set.")
        print("Please set the variable and run the script again.")
    else:
        asyncio.run(main())
