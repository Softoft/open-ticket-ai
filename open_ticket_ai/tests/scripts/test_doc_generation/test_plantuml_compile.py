from pathlib import Path

from open_ticket_ai.scripts.doc_generation.generate_api_reference import compile_plantuml_diagrams


def test_compile_plantuml_diagrams_missing_dir(tmp_path: Path):
    """Tests the behavior of compile_plantuml_diagrams when given a non-existent directory.

    This test verifies that the function handles missing directories gracefully by:
    1. Not raising any exceptions when called with a non-existent path
    2. Ensuring the directory remains non-existent after the function call

    Args:
        tmp_path: A pytest fixture providing a temporary directory path object.
    """
    missing = tmp_path / "does_not_exist"
    # Should not raise
    compile_plantuml_diagrams(str(missing))
    assert not missing.exists()
