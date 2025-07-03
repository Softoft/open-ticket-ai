---
description: Offizielle Dokumentation für die Kern-Utility-Module von OpenTicketAI.
  Erfahren Sie, wie Sie ein `config.schema.json` zur Konfigurationsvalidierung und
  Autovervollständigung generieren, und entdecken Sie weitere Python-Utilities zur
  Verwaltung von Projekteinstellungen.
---
# Dokumentation für `**/ce/core/util/**/*.py`

## Modul: `open_ticket_ai\src\ce\core\util\create_json_config_schema.py`

Modul zur Generierung des JSON-Schemas der OpenTicketAI-Konfiguration.
Dieses Modul definiert das `RootConfig`-Modell, welches ein Wrapper um das Hauptkonfigurationsmodell
`OpenTicketAIConfig` ist. Der Zweck dieses Wrappers ist es, die Generierung eines
JSON-Schemas zu erleichtern, das die gesamte Konfigurationsstruktur beschreibt.

Wenn dieses Modul als Skript ausgeführt wird, wird es:
  1. Das JSON-Schema für das `RootConfig`-Modell generieren.
  2. Das Schema in eine Datei namens `config.schema.json` im Stammverzeichnis des Projekts schreiben.

Die generierte Schemadatei kann zur Validierung von Konfigurationsdateien oder zur Bereitstellung
von Autovervollständigung und Dokumentation für die Konfiguration in Editoren verwendet werden.

### <span style='text-info'>class</span> `RootConfig`

Wrapper-Modell, das für die Schema-Generierung verwendet wird.
Diese `class` dient als Container für das Hauptkonfigurationsmodell des OpenTicketAI-Systems.
Sie ist für die Generierung von JSON-Schema-Darstellungen der Konfiguration konzipiert.

**Parameter:**

- **``open_ticket_ai``** (``OpenTicketAIConfig``) - Das Hauptkonfigurationsobjekt, das alle
Einstellungen und Parameter für das OpenTicketAI-System enthält.


---

## Modul: `open_ticket_ai\src\ce\core\util\path_util.py`



---

## Modul: `open_ticket_ai\src\ce\core\util\pretty_print_config.py`



---