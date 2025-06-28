# Dokumentation für `**/ce/core/util/**/*.py`

## Modul: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`

### <span style='color: #8E44AD;'>class</span> `RootConfig`

Wrapper-Modell, das für die Schema-Generierung verwendet wird.

---

## Modul: `open_ticket_ai\src\ce\core\util\path_util.py`

---

## Modul: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`

### <span style='color: #2980B9;'>def</span> `pretty_print_config(config: BaseModel, console: Console)`

Gibt ein Pydantic-Modell mit ``rich`` formatiert aus.
Diese Funktion konvertiert ein Pydantic-BaseModel in ein Dictionary, serialisiert es zu YAML
und gibt es mit der Syntax-Hervorhebung von rich auf der Konsole aus.

**Parameter:**

- **`config`** (`BaseModel`) - Die anzuzeigende Pydantic-Modellkonfiguration.
- **`console`** (`Console`) - Die rich-Konsoleninstanz für die Ausgabedarstellung.