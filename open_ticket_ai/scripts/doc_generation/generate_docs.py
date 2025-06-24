#!/usr/bin/env python3
"""
A script to generate beautiful Markdown documentation from Python source code.

This script uses Python's `ast` module to traverse the source code,
extracting classes, functions, and their docstrings. It then parses the
docstrings (supports Google, reStructuredText, and Numpydoc styles) and
formats the output into a clean, modern Markdown file.

Features:
-   Class and function-based structure.
-   Rich parsing of docstrings for parameters, returns, and raises sections.
-   Inclusion of type hints in signatures.
-   Modern Markdown styling with badges and collapsible sections.
-   Fully configurable via command-line arguments.
"""
import ast
import argparse
from pathlib import Path
from typing import List, Optional, Union

from docstring_parser import Docstring, parse


# --- Helper Classes for Styling and Structure ---

class DocstringStyler:
    """Provides methods to style parsed docstring components into Markdown."""

    @staticmethod
    def style_params(params: List[dict], title: str) -> str:
        """Styles a list of parameters into a Markdown list."""
        if not params:
            return ""
        parts = [f"\n**{title}:**\n"]
        for param in params:
            type_name = f"`{param.type_name}`" if param.type_name else ""
            default_val = f" (default: `{param.default}`)" if param.default else ""
            description = f" - {param.description}" if param.description else ""
            parts.append(
                f"- **`{param.arg_name}`** ({type_name}){default_val}{description}"
            )
        return "\n".join(parts) + "\n"

    @staticmethod
    def style_returns(returns: Optional[dict]) -> str:
        """Styles the returns section into Markdown."""
        if not returns:
            return ""
        type_name = f"`{returns.type_name}`" if returns.type_name else ""
        description = f" - {returns.description}" if returns.description else ""
        return f"\n**Returns:** ({type_name}){description}\n"


class MarkdownVisitor(ast.NodeVisitor):
    """
    An AST visitor that traverses a Python file and builds a Markdown documentation string.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.markdown_parts: List[str] = []
        self.current_class_name: Optional[str] = None

    def _format_signature(self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> str:
        """Formats a function/method signature, including type hints."""
        args_list = []
        # Process positional and regular arguments
        for arg in node.args.posonlyargs + node.args.args:
            arg_str = arg.arg
            if arg.annotation:
                arg_str += f": {ast.unparse(arg.annotation)}"
            args_list.append(arg_str)
        # *args
        if node.args.vararg:
            args_list.append(f"*{node.args.vararg.arg}")
        # Keyword-only args
        if node.args.kwonlyargs:
            if not node.args.vararg:
                args_list.append('*')
            for kw_arg in node.args.kwonlyargs:
                kw_arg_str = kw_arg.arg
                if kw_arg.annotation:
                    kw_arg_str += f": {ast.unparse(kw_arg.annotation)}"
                args_list.append(kw_arg_str)
        # **kwargs
        if node.args.kwarg:
            args_list.append(f"**{node.args.kwarg.arg}")

        signature = f"({', '.join(args_list)})"
        if node.returns:
            signature += f" -> {ast.unparse(node.returns)}"
        return signature

    def _process_docstring(self, docstring_raw: Optional[str]):
        """Parses a docstring and formats it into Markdown."""
        if not docstring_raw:
            return ""

        docstring: Docstring = parse(docstring_raw)
        parts = [f"{docstring.short_description}\n"]
        if docstring.long_description:
            parts.append(f"{docstring.long_description}\n")

        parts.append(DocstringStyler.style_params(docstring.params, "Parameters"))
        parts.append(DocstringStyler.style_params(docstring.raises, "Raises"))
        parts.append(DocstringStyler.style_returns(docstring.returns))

        return "".join(parts)

    def visit_ClassDef(self, node: ast.ClassDef):
        """Processes a class definition."""
        self.current_class_name = node.name
        self.markdown_parts.append(
            f"### <span style='color: #8E44AD;'>class</span> `{node.name}`\n")

        class_doc_md = self._process_docstring(ast.get_docstring(node))
        if class_doc_md:
            self.markdown_parts.append(class_doc_md)

        self.generic_visit(node)  # Visit methods inside the class
        self.current_class_name = None

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Processes a function or method definition."""
        self._process_function_node(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Processes an async function or method definition."""
        self._process_function_node(node, is_async=True)

    def _process_function_node(self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef],
                               is_async: bool = False):
        """Shared logic for processing sync and async functions."""
        func_name = node.name
        if func_name.startswith("_") and not func_name.startswith("__"):
            return  # Skip private methods/functions

        signature = self._format_signature(node)
        prefix = "<span style='color: #2980B9;'>async def</span>" if is_async else "<span style='color: #2980B9;'>def</span>"

        # Method vs Function styling
        if self.current_class_name:
            badge = "<span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span>"
            summary = f"#### {badge} {prefix} `{func_name}{signature}`"
        else:
            summary = f"### {prefix} `{func_name}{signature}`"

        doc_md = self._process_docstring(ast.get_docstring(node))

        if self.current_class_name:  # Use collapsible sections for methods
            self.markdown_parts.append(
                f"\n<details>\n<summary>{summary}</summary>\n\n{doc_md}\n</details>\n")
        else:  # Top-level functions are not collapsed
            self.markdown_parts.append(f"\n{summary}\n\n{doc_md}\n")

    def get_markdown(self) -> str:
        """Returns the accumulated Markdown content."""
        module_docstring = self._process_docstring(
            ast.get_docstring(ast.parse(self.file_path.read_text(encoding="utf-8"))))
        return module_docstring + "\n" + "\n".join(self.markdown_parts)


def parse_python_file(file_path: Path) -> str:
    """Parses a Python file and returns its documentation in Markdown."""
    try:
        source_code = file_path.read_text(encoding="utf-8")
        tree = ast.parse(source_code)
        visitor = MarkdownVisitor(file_path)
        visitor.visit(tree)
        return visitor.get_markdown()
    except Exception as e:
        return f"### ⚠️ Error parsing `{file_path}`\n\n```\n{e}\n```\n"


# --- Main Generation Logic ---

def main():
    """Main function to run the documentation generator."""
    parser = argparse.ArgumentParser(
        description="Generate Markdown documentation from Python source code.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "src_dir",
        type=str,
        help="Source directory to scan for Python files."
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="DOCUMENTATION.md",
        help="Path to the output Markdown file. (default: DOCUMENTATION.md)"
    )
    parser.add_argument(
        "--title", "-t",
        type=str,
        default="Project Documentation",
        help="Main title for the documentation file. (default: Project Documentation)"
    )
    parser.add_argument(
        "--exclude", "-e",
        nargs='*',
        default=["**/__init__.py", "**/tests/*", "**/.*"],
        help="Glob patterns to exclude files/directories. (default: '**/__init__.py' '**/tests/*' '**/.*')"
    )
    args = parser.parse_args()

    src_path = Path(args.src_dir)
    if not src_path.is_dir():
        print(f"❌ Error: Source directory '{src_path}' not found.")
        return

    all_markdown_content = [f"# {args.title}\n"]
    all_python_files = list(src_path.rglob("*.py"))

    # Filter out excluded files
    filtered_files = []
    for py_file in all_python_files:
        if any(py_file.match(pattern) for pattern in args.exclude):
            continue
        filtered_files.append(py_file)

    sorted_files = sorted(filtered_files)

    for py_file in sorted_files:
        relative_path = py_file.relative_to(src_path.parent)
        print(f"📄 Processing: {relative_path}")
        all_markdown_content.append(f"## Module: `{relative_path}`\n")
        file_markdown = parse_python_file(py_file)
        all_markdown_content.append(file_markdown)
        all_markdown_content.append("\n---\n")

    try:
        Path(args.output).write_text("\n".join(all_markdown_content), encoding="utf-8")
        print(f"\n✅ Documentation successfully generated at: {Path(args.output).resolve()}")
    except IOError as e:
        print(f"\n❌ Error writing to file '{args.output}': {e}")


if __name__ == "__main__":
    main()
