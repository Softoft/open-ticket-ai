import pytest
import os
import shutil
from open_ticket_ai.scripts.license_script import (
    find_start_of_code,
    update_license_in_files,
    new_license_notice,
    read_file,
    write_file
)

TEST_DIR = "test_license_files_temp"

@pytest.fixture
def setup_test_directory(tmp_path):
    """Sets up a temporary directory with various files for testing."""
    test_dir = tmp_path / TEST_DIR
    os.makedirs(test_dir, exist_ok=True)

    # File content examples
    file_contents = {
        "file_with_code.py": "print('Hello World')",
        "file_with_comments.py": "# This is a comment\n# Another comment",
        "file_with_mixed_content.py": "# Comment line\nprint('Code line')",
        "empty_file.py": "",
        "non_python_file.txt": "This is a text file.",
        "already_licensed.py": new_license_notice + "\\nprint('already licensed')"
    }

    for filename, content in file_contents.items():
        with open(test_dir / filename, "w") as f:
            f.write(content)

    # Create a subdirectory with a python file
    sub_dir = test_dir / "subdir"
    os.makedirs(sub_dir, exist_ok=True)
    with open(sub_dir / "sub_file.py", "w") as f:
        f.write("print('Hello from sub dir')")

    yield str(test_dir)

    # Teardown: Remove the temporary directory
    # shutil.rmtree(test_dir) # tmp_path fixture handles cleanup

@pytest.mark.parametrize(
    "lines, expected_index",
    [
        (["# comment1", "# comment2", "code_line"], 2),
        (["code_line", "# comment1"], 0),
        (["", "\t", "  ", "code_line"], 3),
        (["# comment", "", "code_line"], 2),
        (["# comment1", "# comment2"], 2), # Only comments
        ([], 0), # Empty list
        (["", "   "], 2), # Only whitespace
        (["\n", "code"],1)
    ]
)
def test_find_start_of_code(lines, expected_index):
    assert find_start_of_code(lines) == expected_index

def test_update_license_in_files(setup_test_directory):
    test_dir = setup_test_directory
    update_license_in_files(test_dir)

    # Check python files
    py_files_to_check = {
        "file_with_code.py": "print('Hello World')",
        "file_with_comments.py": "# This is a comment\n# Another comment",
        "file_with_mixed_content.py": "print('Code line')", # Code starts after comment
        "empty_file.py": "",
        "subdir/sub_file.py": "print('Hello from sub dir')"
    }

    for py_file, original_code_start in py_files_to_check.items():
        filepath = os.path.join(test_dir, py_file)
        lines = read_file(filepath)
        file_content = "".join(lines)
        assert file_content.startswith(new_license_notice + '\n')
        if original_code_start: # if not empty file
             # Ensure the original code (or comments if no code) is still there after the license
            assert original_code_start in file_content
        else: # For empty_file.py
            assert file_content == new_license_notice + '\n'


    # Check already licensed file (should not add another license, but replace)
    already_licensed_filepath = os.path.join(test_dir, "already_licensed.py")
    already_licensed_lines = read_file(already_licensed_filepath)
    already_licensed_content = "".join(already_licensed_lines)
    assert already_licensed_content.startswith(new_license_notice + '\n')
    assert already_licensed_content.count(new_license_notice) == 1 # Only one notice
    assert "print('already licensed')" in already_licensed_content

    # Check non-python file (should not be modified)
    non_python_filepath = os.path.join(test_dir, "non_python_file.txt")
    non_python_content = "".join(read_file(non_python_filepath))
    assert non_python_content == "This is a text file."

# Remove placeholder test
# def test_placeholder():
# assert True
