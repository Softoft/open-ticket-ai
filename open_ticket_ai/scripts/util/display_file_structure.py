from io import StringIO
from pathlib import Path
from pathspec import PathSpec
from pathspec.patterns import GitWildMatchPattern
from pathspec.util import normalize_file
from rich.tree import Tree
from rich import console, print
from rich.console import Console
from open_ticket_ai.src.ce.core.util.path_util import find_python_code_root_path


def load_gitignore(base_path: Path) -> PathSpec:
    gitignore = base_path / ".gitignore"
    if not gitignore.exists():
        return PathSpec.from_lines(GitWildMatchPattern, [])
    lines = gitignore.read_text().splitlines()
    return PathSpec.from_lines(GitWildMatchPattern, lines)


def build_tree(base_path: Path, spec: PathSpec, tree: Tree, relative_path=""):
    for path in sorted(base_path.iterdir()):
        rel_path = normalize_file((Path(relative_path) / path.name).as_posix())
        if spec.match_file(rel_path):
            continue
        if path.is_dir():
            branch = tree.add(f"{path.name}")
            build_tree(path, spec, branch, rel_path)
        else:
            tree.add(path.name)

def get_tree_str(tree: Tree) -> str:
    buf = StringIO()
    console = Console(file=buf, force_terminal=True, width=120)
    console.print(tree)
    return buf.getvalue()

def display_dir_tree(path_str: str):
    base_path = Path(path_str).resolve()
    spec = load_gitignore(base_path)
    tree = Tree(f"{base_path.name}")
    build_tree(base_path, spec, tree)
    return get_tree_str(tree)


if __name__ == "__main__":
    print(display_dir_tree(find_python_code_root_path().parent))
