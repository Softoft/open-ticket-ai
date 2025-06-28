# Dokumentation für `**/ce/core/dependency_injection/**/*.py`

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\abstract_container.py`



---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\container.py`



---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\create_registry.py`



### <span class='text-warning'>def</span> `create_registry() -> Registry`

Erstellt und konfiguriert die standardmäßige Klassen-Registry.
Diese Funktion initialisiert eine `Registry`-Instanz und registriert wesentliche Klassen,
die für das Dependency-Injection-System der Anwendung erforderlich sind. Die registrierten Klassen
umfassen Integrationsadapter, Datenaufbereiter und KI-Inferenzdienste.

Die folgenden Klassen werden registriert:
- `OTOBOAdapter`: Übernimmt die Integration mit dem OTOBO-Ticketsystem.
- `SubjectBodyPreparer`: Bereitet Betreff- und Textinhalte für die Ticketverarbeitung vor.
- `HFAIInferenceService`: Stellt lokale KI-Inferenz mithilfe von Hugging-Face-Modellen bereit.

**Rückgabe:** (`Registry`) - Eine konfigurierte Registry-Instanz, bei der alle notwendigen Klassen registriert sind.



---

## Modul: `open_ticket_ai\src\ce\core\dependency_injection\registry.py`



---