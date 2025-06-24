import os

directory_path = "src"

new_license_notice = """# Copyright (c) 2024 by Softoft, Tobias Bueck Einzelunternehmen
# This code is part of the "OTOBO - AI Ticket Classification - Basic" and is governed
# by its license agreement. Full license in LICENSE_DE.md / LICENSE_EN.md. This code cannot be copied and/or distributed
# without the express permission of Softoft, Tobias Bueck Einzelunternehmen.
"""


def find_start_of_code(lines):
    """Return the index of the first non-comment line."""
    for i, line in enumerate(lines):
        if line.strip() and not line.strip().startswith("#"):
            return i
    return len(lines)


def read_file(filepath):
    """Read all lines from ``filepath``."""
    with open(filepath) as file:
        return file.readlines()


def write_file(filepath, lines):
    """Write ``lines`` to ``filepath``."""
    with open(filepath, "w") as file:
        file.writelines(lines)


def update_license_in_files(directory):
    """Insert the license notice at the top of all ``.py`` files."""
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if not filename.endswith(".py"):
                continue
            filepath = os.path.join(subdir, filename)
            lines = read_file(filepath)
            start_of_code = find_start_of_code(lines)
            updated_lines = [new_license_notice + "\n"] + lines[start_of_code:]
            write_file(filepath, updated_lines)
            print(f"Updated license in {filepath}")


if __name__ == "__main__":
    update_license_in_files(directory_path)
