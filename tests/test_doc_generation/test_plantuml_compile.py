from pathlib import Path

from open_ticket_ai.scripts.doc_generation.generate_docs import compile_plantuml_diagrams


def test_compile_plantuml_diagrams(tmp_path: Path):
    puml = tmp_path / "diagram.puml"
    puml.write_text("@startuml\na -> b\n@enduml")

    compile_plantuml_diagrams(str(tmp_path))

    assert (tmp_path / "diagram.png").is_file()


def test_compile_plantuml_diagrams_missing_dir(tmp_path: Path):
    missing = tmp_path / "does_not_exist"
    # Should not raise
    compile_plantuml_diagrams(str(missing))
    assert not missing.exists()

