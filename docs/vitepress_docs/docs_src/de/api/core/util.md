# Dokumentation für `**/ce/core/util/**/*.py`

## Modul: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`

Modul zur Generierung des JSON-Schemas der OpenTicketAI-Konfiguration.
Dieses Modul definiert das `RootConfig`-`model`, welches ein Wrapper um das Hauptkonfigurationsmodell `OpenTicketAIConfig` ist. Der Zweck dieses Wrappers ist es, die Erstellung eines JSON-Schemas zu erleichtern, das die gesamte Konfigurationsstruktur beschreibt.

Wenn dieses Modul als Skript ausgeführt wird, wird es:
  1. Das JSON-Schema für das `RootConfig`-`model` generieren.
  2. Das Schema in eine Datei namens `config.schema.json` im Stammverzeichnis des Projekts schreiben.

Die generierte Schemadatei kann verwendet werden, um Konfigurationsdateien zu validieren oder um Autovervollständigung und Dokumentation für die Konfiguration in Editoren bereitzustellen.

### <span style='text-info'>class</span> `RootConfig`

Wrapper-`model`, das für die Schema-Generierung verwendet wird.
Diese `class` dient als Container für das Hauptkonfigurationsmodell des OpenTicketAI-Systems.
Sie ist dafür konzipiert, JSON-Schema-Darstellungen der Konfiguration zu generieren.

**Parameter:**

- **`open_ticket_ai`** (`OpenTicketAIConfig`) - Das Hauptkonfigurationsobjekt, das alle Einstellungen und Parameter für das OpenTicketAI-System enthält.


---

## Modul: `open_ticket_ai\src\ce\core\util\path_util.py`



---

## Modul: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`

Modul zur formatierten Ausgabe (`pretty printing`) von Konfigurationsobjekten.
Dieses Modul bietet Funktionalität, um Pydantic-Konfigurationsmodelle mithilfe der `rich`-Bibliothek schön formatiert und mit Syntaxhervorhebung darzustellen. Es konvertiert Pydantic-Modelle in das YAML-Format und wendet zur besseren Lesbarkeit eine Syntaxhervorhebung an.

Funktionen:
- Konvertiert Pydantic `BaseModel`-Instanzen in Dictionaries
- Serialisiert Konfigurationsdaten in das YAML-Format
- Wendet YAML-Syntaxhervorhebung mit `rich` an
- Gibt die hervorgehobene Ausgabe auf der Konsole aus


### <span class='text-warning'>def</span> `pretty_print_config(config: BaseModel, console: Console)`

Formatierte Ausgabe (`pretty print`) eines Pydantic-`model`s mithilfe von `rich`.
Diese Funktion konvertiert ein Pydantic `BaseModel` in ein Dictionary, serialisiert es in YAML und gibt es mithilfe der Syntaxhervorhebung von `rich` auf der Konsole aus. Die Ausgabe wird zur besseren Lesbarkeit mit YAML-Syntaxhervorhebung formatiert.

Der Prozess umfasst:
    1. Konvertieren des Pydantic-`model`s in ein Dictionary mit `model_dump()`
    2. Serialisieren des Dictionaries in einen YAML-String
    3. Erstellen eines `rich` `Syntax`-Objekts mit YAML-Hervorhebung
    4. Ausgeben des hervorgehobenen YAMLs auf der Konsole

Beachten Sie, dass diese Funktion das Standard-Logging umgeht und für eine optimale Formatierung direkt über die Ausgabefunktionen von `rich` auf der Konsole ausgibt.

**Parameter:**

- **`config`** (``BaseModel``) - Die anzuzeigende Pydantic-`model`-Konfiguration.
- **`console`** (``Console``) - Die `rich`-Konsoleninstanz für die Darstellung der Ausgabe.



---