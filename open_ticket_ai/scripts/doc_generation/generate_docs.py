#!/usr/bin/env python3
import ast
from pathlib import Path


def _format_args(args_node: ast.arguments) -> str:
    """Formats an ast.arguments node into a string like (arg1, arg2, kwarg=None)."""
    args = []
    # Positional and keyword-only arguments before *args
    pos_args_count = len(args_node.posonlyargs) + len(args_node.args)
    defaults_start = pos_args_count - len(args_node.defaults)

    # Positional-only args
    for i, arg in enumerate(args_node.posonlyargs):
        if i >= defaults_start:
            default = ast.unparse(args_node.defaults[i - defaults_start])
            args.append(f"{arg.arg}={default}")
        else:
            args.append(arg.arg)

    # Add / to indicate end of positional-only
    if args_node.posonlyargs:
        args.append('/')

    # Regular args
    for i, arg in enumerate(args_node.args):
        default_idx = i + len(args_node.posonlyargs) - defaults_start
        if default_idx >= 0:
            default = ast.unparse(args_node.defaults[default_idx])
            args.append(f"{arg.arg}={default}")
        else:
            args.append(arg.arg)

    # *args
    if args_node.vararg:
        args.append(f"*{args_node.vararg.arg}")

    # Keyword-only args
    if args_node.kwonlyargs:
        if not args_node.vararg:
            args.append('*')
        for i, arg in enumerate(args_node.kwonlyargs):
            if args_node.kw_defaults[i] is not None:
                default = ast.unparse(args_node.kw_defaults[i])
                args.append(f"{arg.arg}={default}")
            else:
                args.append(arg.arg)

    # **kwargs
    if args_node.kwarg:
        args.append(f"**{args_node.kwarg.arg}")

    return f"({', '.join(args)})"


def parse_python_file(file_path: Path) -> str:
    """
    Parses a single Python file and returns its documentation in Markdown format.

    Args:
        file_path (Path): The path to the Python file.

    Returns:
        str: A string containing the Markdown documentation.
    """
    try:
        with open(file_path, encoding="utf-8") as source_file:
            source_code = source_file.read()
        tree = ast.parse(source_code)
    except Exception as e:
        return f"### Error parsing `{file_path}`\n\n```\n{e}\n```\n\n"

    markdown_parts = []

    # Module-level docstring
    module_docstring = ast.get_docstring(tree)
    if module_docstring:
        markdown_parts.append(f"{module_docstring}\n")

    # Iterate through top-level nodes (classes and functions)
    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            markdown_parts.append(f"### `class {node.name}`\n")
            class_docstring = ast.get_docstring(node)
            if class_docstring:
                markdown_parts.append(f"{class_docstring}\n")

            # Find methods within the class
            for method_node in node.body:
                if isinstance(method_node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    is_async = "async " if isinstance(method_node, ast.AsyncFunctionDef) else ""
                    method_name = method_node.name
                    args_str = _format_args(method_node.args)
                    markdown_parts.append(f"#### `{is_async}def {method_name}{args_str}`\n")

                    method_docstring = ast.get_docstring(method_node)
                    if method_docstring:
                        markdown_parts.append(f"```text\n{method_docstring}\n```\n")

        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            is_async = "async " if isinstance(node, ast.AsyncFunctionDef) else ""
            func_name = node.name
            args_str = _format_args(node.args)
            markdown_parts.append(f"### `{is_async}def {func_name}{args_str}`\n")

            func_docstring = ast.get_docstring(node)
            if func_docstring:
                markdown_parts.append(f"```text\n{func_docstring}\n```\n")

    return "\n".join(markdown_parts)


def generate_documentation(src_dir: str, output_file: str = "documentation.md",
                           title: str = "Project Documentation",
                           excluded_patterns: list[str] = None) -> None:
    """
    Generates Markdown documentation from Python docstrings in a directory.

    Args:
        src_dir (str): The source directory to scan for Python files.
        output_file (str): The name of the output Markdown file.
        title (str): The main title for the documentation file.
        :param excluded_patterns:
    """
    excluded_patterns = excluded_patterns or []
    src_path = Path(src_dir)
    if not src_path.is_dir():
        print(f"Error: Source directory '{src_path}' not found.")
        return

    output_path = Path(output_file)

    all_markdown_content = [f"# {title}\n"]

    # Use rglob to recursively find all .py files
    python_files = sorted(list(src_path.rglob("*.py")))

    filtered_files = []
    for py_file in python_files:
        # Check if the file should be excluded
        if any(py_file.match(pattern) for pattern in excluded_patterns):
            print(f"Excluding: {py_file.relative_to(src_path.parent)}")
            continue
        filtered_files.append(py_file)

    for py_file in filtered_files:
        # Get a relative path for cleaner headings
        relative_path = py_file.relative_to(src_path.parent)
        print(f"Processing: {relative_path}")
        all_markdown_content.append(f"## Module: `{relative_path}`\n")
        file_markdown = parse_python_file(py_file)
        all_markdown_content.append(file_markdown)
        all_markdown_content.append("\n---\n")

    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(all_markdown_content))
        print(f"\n✅ Documentation successfully generated at: {output_path.resolve()}")
    except IOError as e:
        print(f"\n❌ Error writing to file '{output_path}': {e}")


if __name__ == "__main__":
    # --- Configuration ---
    # 1. Set the path to the directory you want to document.
    #    For example, 'my_project' or '.' for the current directory.
    SOURCE_DIRECTORY = "../../../open_ticket_ai/src"

    # 2. Set the desired name for the output documentation file.
    OUTPUT_FILE = "documentation.md"

    # 3. Set the main title for your documentation.
    DOC_TITLE = "Project Documentation"
    # ---------------------

    # Run the documentation generator with the settings above.
    generate_documentation(
        src_dir=SOURCE_DIRECTORY,
        output_file=OUTPUT_FILE,
        title=DOC_TITLE,
        excluded_patterns=["*.test.py", "*.spec.py", "tests/", "docs/", "scripts/", "**/__init__.py"]
    )
