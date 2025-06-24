import os
import subprocess
import sys


def generate_markdown_docs(module_name: str, output_dir: str = "docs"):
    """
    Generates Markdown documentation from Python docstrings using pdoc.

    This script takes a Python module name as input and generates Markdown
    files for each submodule and class, placing them in the specified
    output directory.

    Prerequisites:
        - Python 3.x
        - pdoc3 library (`pip install pdoc3`)

    Usage:
        python generate_docs.py <module_name> [output_directory]

    Examples:
        1. Generate documentation for a module named 'my_package' and
           output to the default 'docs/' directory:
           ```bash
           python generate_docs.py my_package
           ```

        2. Generate documentation for 'my_package' and output to a
           custom directory named 'api_docs/':
           ```bash
           python generate_docs.py my_package api_docs
           ```

        3. If 'my_package' is not in the current directory, ensure it's
           in your PYTHONPATH:
           ```bash
           export PYTHONPATH=$PYTHONPATH:/path/to/my_package_parent_dir
           python generate_docs.py my_package
           ```

    The script will create the output directory if it doesn't exist.
    The generated Markdown files will be placed directly into the
    specified output directory. For example, if `module_name` is `my_package`
    and `output_dir` is `docs`, and `my_package` has `utils.py`, then
    `docs/utils.md` will be created.

    Args:
        module_name: The name of the Python module/package to document.
                     This module must be importable (i.e., in PYTHONPATH).
        output_dir: The directory where the Markdown files will be saved.
                    Defaults to "docs".

    Raises:
        RuntimeError: If pdoc fails to generate the documentation.
        FileNotFoundError: If the specified module cannot be found.
    """
    print(f"Generating Markdown documentation for '{module_name}'...")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Try to import the module to check if it exists and is importable
        __import__(module_name)
    except ImportError:
        raise FileNotFoundError(
            f"Module '{module_name}' not found or not in PYTHONPATH. "
            "Please ensure the module is installed or its path is in PYTHONPATH."
        )

    # --- Using --pdf to capture Markdown output ---
    print(f"Generating Markdown for '{module_name}' using 'pdoc --pdf ...'")

    # Determine the path for the output .md file
    # For a package, pdoc --pdf documents the package and its submodules recursively into one stream.
    # So, we'll name the output file after the package.
    # If module_name is a path like "my_package/my_module.py", extract "my_module"
    if os.path.isfile(module_name) and module_name.endswith(".py"):
        base_name = os.path.splitext(os.path.basename(module_name))[0]
        # However, pdoc usually takes import paths, not file paths.
        # For simplicity, we'll assume module_name is an importable name.
        # If it's a package, pdoc handles it. If it's a module, pdoc handles it.
        markdown_file_name = f"{base_name}.md"
    else: # It's likely a package name
        markdown_file_name = f"{module_name}.md"

    markdown_output_file = os.path.join(output_dir, markdown_file_name)


    pdoc_command = [
        sys.executable,
        "-m",
        "pdoc",
        module_name,
        "--pdf",  # This flag tells pdoc to output Markdown to stdout
    ]

    try:
        # Ensure the current directory is in PYTHONPATH for pdoc to find the module
        env = os.environ.copy()
        current_dir = os.getcwd()
        # Add current directory to PYTHONPATH, which is where example_package resides
        env["PYTHONPATH"] = f"{current_dir}{os.pathsep}{env.get('PYTHONPATH', '')}"

        print(f"Running command: {' '.join(pdoc_command)}")
        print(f"Using PYTHONPATH: {env.get('PYTHONPATH')}")

        process = subprocess.run(
            pdoc_command,
            capture_output=True,
            text=True,
            check=True,
            env=env, # Pass the modified environment
        )

        # Write the captured stdout (which is Markdown) to the file
        with open(markdown_output_file, "w", encoding="utf-8") as f:
            f.write(process.stdout)

        print(f"Successfully generated Markdown documentation: {markdown_output_file}")
        if process.stderr:
            print(f"pdoc stderr (warnings etc.):\n{process.stderr}")


    except subprocess.CalledProcessError as e:
        error_message = f"pdoc failed with error code {e.returncode}.\n"
        error_message += f"Stdout: {e.stdout}\n"
        error_message += f"Stderr: {e.stderr}"
        raise RuntimeError(error_message)
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_docs.py <module_name> [output_directory]")
        print("\nExample: python generate_docs.py my_package")
        print("Example: python generate_docs.py my_package custom_docs_folder")
        sys.exit(1)

    module_to_doc = sys.argv[1]
    docs_output_dir = "docs"
    if len(sys.argv) > 2:
        docs_output_dir = sys.argv[2]

    try:
        generate_markdown_docs(module_to_doc, docs_output_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)
