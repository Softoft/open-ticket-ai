from __future__ import annotations

from pathlib import Path

import tomli


class VersionManager:
    """Handle versioning logic for documentation generation."""

    def __init__(self, pyproject_path: Path, docs_root: Path) -> None:
        """Initialize with paths to ``pyproject.toml`` and docs root."""
        self.pyproject_path = pyproject_path
        self.docs_root = docs_root

    def get_project_version(self) -> str:
        """Return the project version defined in ``pyproject.toml``."""
        try:
            with self.pyproject_path.open("rb") as f:
                data = tomli.load(f)
            return str(data["project"]["version"])
        except FileNotFoundError as exc:
            raise FileNotFoundError(
                f"pyproject.toml not found at {self.pyproject_path}"
            ) from exc
        except KeyError as exc:
            raise KeyError(
                "Version not found in pyproject.toml under [project]['version']"
            ) from exc
        except Exception as exc:  # pragma: no cover - unexpected errors
            raise RuntimeError(f"Failed to parse {self.pyproject_path}: {exc}") from exc

    def prepare_version_directory(self, base_lang: str = "en") -> Path:
        """Create and return the docs directory for the current version."""
        version = self.get_project_version()
        target = self.docs_root / base_lang / f"v{version}"
        if target.exists():
            print(f"Documentation directory already exists: {target}")
            raise FileExistsError(
                f"Documentation for version {version} already exists at {target}"
            )
        target.mkdir(parents=True, exist_ok=False)
        return target
