from pathlib import Path


def find_python_code_root_path(project_name: str = 'open_ticket_ai') -> Path:
    """Search parent directories for the project root.

    This function traverses upwards from the current file's directory to locate
    the root directory of the project identified by the given name.

    Args:
        project_name: The name of the project root directory to find.
            Defaults to 'open_ticket_ai'.

    Returns:
        Path: The absolute path to the project root directory.

    Raises:
        FileNotFoundError: If the project root directory cannot be found in any
            parent directories.
    """

    start_path = Path(__file__).resolve()
    for parent in [start_path, *start_path.parents]:
        if parent.name == project_name:
            return parent
    raise FileNotFoundError(f"Project folder '{project_name}' not found in parents of {start_path}")
