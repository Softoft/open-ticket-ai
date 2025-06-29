# FILE_PATH: open_ticket_ai\scripts\doc_generation\generate_api_reference.py
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
from pathlib import Path
from typing import List, Optional, Union

from docstring_parser import Docstring, DocstringParam, DocstringRaises, DocstringReturns, parse

from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path


# --- Helper Classes for Styling and Structure ---

class DocstringStyler:
    """Provides methods to style parsed docstring components into Markdown."""

    @staticmethod
    def style_params(params: list[DocstringParam] | list[DocstringRaises], title: str) -> str:
        """Styles a list of parameters into a Markdown list."""
        if not params:
            return ""
        parts = [f"\n**{title}:**\n"]
        for param in params:
            type_name = f"`{param.type_name}`" if param.type_name else ""
            default_val = f" (default: `{param.default}`)" if param.default else ""
            description = f" - {param.description}" if param.description else ""
            parts.append(
                f"- **`{param.arg_name}`** ({type_name}){default_val}{description}",
            )
        return "\n".join(parts) + "\n"

    @staticmethod
    def style_returns(returns: Optional[DocstringReturns]) -> str:
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
        """Initializes the MarkdownVisitor instance.

        Args:
            file_path: Path to the Python source file being processed.
        """
        self.file_path = file_path
        self.markdown_parts: List[str] = []
        self.current_class_name: Optional[str] = None

    def _format_signature(self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef]) -> str:
        """
        Formats a function/method signature with type hints into a readable string.

        Args:
            node: The AST function node to format.

        Returns:
            A string representing the formatted function signature including:
            - Parameter names with type annotations
            - Positional-only, keyword-only, *args and **kwargs parameters
            - Return type annotation if present
        """
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
        """
        Parses and converts a docstring into formatted Markdown.

        Args:
            docstring_raw: The raw docstring text to process.

        Returns:
            A Markdown-formatted string containing:
            - Short description
            - Long description
            - Parameters section
            - Raises section
            - Returns section
        """
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
            f"### <span style='text-info'>class</span> `{node.name}`\n",
        )

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

    def _process_function_node(
        self, node: Union[ast.FunctionDef, ast.AsyncFunctionDef],
        is_async: bool = False
    ):
        """Processes function/method nodes into formatted Markdown documentation.

        This method handles both synchronous and asynchronous functions. It formats the function
        signature, generates a badge for methods (if inside a class), and processes the docstring.
        The output is appended to the visitor's markdown_parts.

        Args:
            node: The AST function node to process.
            is_async: Flag indicating whether the function is async.
        """
        func_name = node.name
        if func_name.startswith("_") and not func_name.startswith("__"):
            return  # Skip private methods/functions

        signature = self._format_signature(node)
        prefix: str = ('<span class="text-warning">async def</span>' if is_async
                       else "<span class='text-warning'>def</span>")

        # Method vs Function styling
        if self.current_class_name:
            badge = '<Badge type="info" text="method"/>'
            summary = f"#### {badge} {prefix} `{func_name}{signature}`"
        else:
            summary = f"### {prefix} `{func_name}{signature}`"

        doc_md = self._process_docstring(ast.get_docstring(node))

        if self.current_class_name:  # Use collapsible sections for methods
            self.markdown_parts.append(
                f"\n::: details {summary}\n{doc_md}\n:::\n",
            )
        else:  # Top-level functions are not collapsed
            self.markdown_parts.append(f"\n{summary}\n\n{doc_md}\n")

    def get_markdown(self) -> str:
        """Returns the accumulated Markdown content."""
        module_docstring = self._process_docstring(
            ast.get_docstring(ast.parse(self.file_path.read_text(encoding="utf-8"))),
        )
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
        print(f"Error parsing `{file_path}`\n\n```\n{e}\n```\n")
        return ""


def generate_markdown_for_pattern(
    src_path,
    pattern: str,
    excluded: list[str],
    output_path: Path
) -> None:
    """
    Generates Markdown documentation for all Python files matching a glob pattern.

    Args:
        excluded:
        src_path (Path): The source directory to search for Python files.
        pattern (str): The glob pattern to match Python files.
        output_path (Path): The path where the generated Markdown file will be saved.
    """
    src_path = Path(src_path)
    if not src_path.is_dir():
        raise ValueError(f"Source path `{src_path}` is not a directory.")

    all_markdown_content = [f"# Documentation for `{pattern}`\n"]
    all_python_files = list(src_path.rglob(pattern))

    # Filter out excluded files
    filtered_files: list[Path] = []
    for py_file in all_python_files:
        if any(py_file.match(exclude) for exclude in excluded):
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

    # Ensure the output directory exists, create the directory if it doesn't
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(all_markdown_content), encoding="utf-8")
    print(f"\n✅ Documentation successfully generated at: {output_path.resolve()}")


def generate_markdown(
    src_path: Path,
    patterns_to_output_map: dict[str, Path],
    excluded: list[str]
) -> None:
    """
    Generates Markdown documentation for a project based on specified patterns.

    Args:
        src_path:
        patterns_to_output_map (dict[str, Path]): A dictionary mapping glob patterns to output paths.
        excluded (list[str]): List of glob patterns to exclude from processing.
    """

    for pattern, output_path in patterns_to_output_map.items():
        print(f"📂 Processing pattern: `{pattern}`")
        generate_markdown_for_pattern(src_path, pattern, excluded, output_path)
