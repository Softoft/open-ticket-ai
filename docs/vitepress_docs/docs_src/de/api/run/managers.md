---
description: Erkunden Sie die OpenTicketAI `Orchestrator`-Klasse, eine Kernkomponente zur Automatisierung
  von Ticketverarbeitungs-Workflows. Dieses Python-Modul verwaltet den gesamten Lebenszyklus
  von Pipelines, einschließlich der Instanziierung über Dependency Injection, der Verarbeitung
  einzelner Tickets und der geplanten Ausführung für eine kontinuierliche Automatisierung.
---
# Dokumentation für `**/ce/run/managers/*.py`

## Modul: `open_ticket_ai\src\ce\run\managers\orchestrator.py`

Orchestrierungs-Hilfsprogramme der obersten Ebene.

### <span style='text-info'>class</span> `Orchestrator`

Orchestriert die Ausführung von Ticketverarbeitungs-Pipelines.
Diese Klasse verwaltet den Lebenszyklus von Pipelines, einschließlich:
- Instanziierung der Pipeline über Dependency Injection
- Verarbeitung einzelner Tickets
- Geplante Ausführung von Pipelines

**Parameter:**

- **`config`** () - Konfigurationseinstellungen für den Orchestrator
- **`container`** () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt
- **`_logger`** () - Logger-Instanz für Orchestrierungsoperationen
- **`_pipelines`** () - Dictionary, das Pipeline-IDs auf Pipeline-Instanzen abbildet


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: OpenTicketAIConfig, container: AbstractContainer)`
Initialisiert den Orchestrator mit Konfiguration und DI-Container.

**Parameter:**

- **`config`** () - Konfigurationseinstellungen für den Orchestrator.
- **`container`** () - Dependency-Injection-Container, der Pipeline-Instanzen bereitstellt.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `process_ticket(self, ticket_id: str, pipeline: Pipeline) -> PipelineContext`
Führt eine Pipeline für ein bestimmtes Ticket aus.
Erstellt einen Verarbeitungskontext und führt die angegebene Pipeline aus, um
das gegebene Ticket zu verarbeiten. Dies ist die Kernmethode für die Verarbeitung einzelner Tickets.

**Parameter:**

- **`ticket_id`** () - Eindeutiger Bezeichner des zu verarbeitenden Tickets.
- **`pipeline`** () - Auszuführende Pipeline-Instanz.

**Rückgabe:** (`PipelineContext`) - Der Ausführungskontext, der Ergebnisse und den Zustand
nach der Pipeline-Ausführung enthält.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `build_pipelines(self) -> None`
Instanziiert alle konfigurierten Pipeline-Objekte.
Verwendet den Dependency-Injection-Container, um Pipeline-Instanzen
basierend auf der Konfiguration zu erstellen. Füllt die interne Pipeline-Registry
mit Zuordnungen von Pipeline-IDs zu Instanzen.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `set_schedules(self) -> None`
Konfiguriert die geplante Ausführung für alle Pipelines.
Führt die folgenden Operationen aus:
1. Erstellt Pipelines, falls diese noch nicht instanziiert sind
2. Konfiguriert die periodische Ausführung für jede Pipeline gemäß ihrer
   Zeitplankonfiguration unter Verwendung der `schedule`-Bibliothek

Die Zeitplanung verwendet die folgenden Konfigurationsparameter:
- interval: Numerischer Intervallwert
- unit: Zeiteinheit (z. B. Minuten, Stunden, Tage)

Hinweis:
- Verwendet das `schedule.every(interval).unit`-Muster für die Zeitplanung
- Übergibt bei geplanten Ausführungen einen leeren ticket_id-Kontext

:::


---