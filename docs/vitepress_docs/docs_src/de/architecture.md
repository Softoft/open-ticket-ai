---
description: Erkunden Sie die technische Architektur von Open Ticket AI. Erfahren Sie, wie die modulare Daten-Pipeline, Dependency Injection und Hugging-Face-Modelle eine intelligente Ticket-Klassifizierung und -Weiterleitung für Helpdesk-Systeme wie OTOBO ermöglichen.
title: Architekturübersicht von Open Ticket AI
---
# Architekturübersicht

Open Ticket AI läuft als Hintergrunddienst, der über die Kommandozeile gestartet wird. Die Architektur basiert auf einer modularen Pipeline, die jedes Ticket in einer Reihe von klar definierten Stufen verarbeitet. Dependency Injection und eine zentrale Konfigurationsdatei (`config.yml`) steuern, welche Komponenten verwendet werden, was die Erweiterung oder den Austausch einzelner Teile vereinfacht.

## Einstiegspunkt der Anwendung

Starten Sie die Anwendung mit:

```bash
python -m open_ticket_ai.src.ce.main start
```

Dieser Befehl initialisiert den Dependency-Injection-Container, erstellt das `App`-Objekt und startet die Hauptverarbeitungsschleife.

## Ausführungsablauf

1. `main.py` konfiguriert das Logging und erstellt einen `DIContainer`.
2. Der Container lädt die `config.yml` und erstellt alle konfigurierten Komponenten.
3. Die `App` validiert die Konfiguration und delegiert an den `Orchestrator`.
4. Der `Orchestrator` liest die Pipeline-Definitionen und plant sie mithilfe der `schedule`-Bibliothek.
5. Jede geplante Pipeline fragt den Helpdesk periodisch nach neuen Tickets ab und verarbeitet diese.

## Verarbeitungs-Pipeline

Die Ticket-Verarbeitungs-Pipeline sieht wie folgt aus:

```mermaid
flowchart TB
    Start([Start])
    Sched[Scheduler löst **Orchestrator** für eine Pipeline aus]
    Start --> Sched

    subgraph "Pipeline-Ausführung"
        direction TB

        BF[Erste Pipe (**BasicTicketFetcher**) wird aufgerufen]
        Sched --> BF

        subgraph "TicketSystemAdapter"
            direction TB
            Fetch[Aufruf der `fetch()`-Methode<br/>Kommuniziert mit externer Ticket-System REST API]
        end
        BF --> Fetch

        Fetch --> Decision{Ticket-Daten empfangen?}

        Decision -- Ja --> Context[**PipelineContext** erstellen und füllen<br/>(enthält ticket_id, data)]
        Context --> SB[Context an **SubjectBodyPreparer** übergeben<br/>Daten werden für die KI transformiert]
        SB --> AI[Context an **HFAIInferenceService** übergeben<br/>KI-Vorhersage wird zum Context hinzugefügt]
        AI --> SF[Context an **SetFieldFromModelOutput** übergeben<br/>Vorhersage wird in eine Anweisung zur Feldaktualisierung umgewandelt (z.B. `{'Queue': 'Sales'}`)]
        SF --> GT[Context an letzte Pipe (**GenericTicketUpdater**) übergeben]

        subgraph "TicketSystemAdapter"
            direction TB
            Update[Aufruf von `update()` mit Daten aus dem Context<br/>Kommuniziert mit externer Ticket-System REST API]
        end
        GT --> Update

        Update --> Complete[Pipeline für dieses Ticket ist abgeschlossen]
        Decision -- Nein --> EndNo[Pipeline endet]
    end

    Complete --> Stop([Stopp])
    EndNo --> Stop

```

Jeder Schritt konsumiert und produziert **Value Objects** wie `subject`, `body`, `queue_id` und `priority`. Dieser Ansatz hält die Pipeline modular und ermöglicht das Hinzufügen neuer Schritte oder Value Objects mit minimalen Änderungen am Rest des Systems.

## Hauptkomponenten

- **App & Orchestrator** – Validieren die Konfiguration, planen Jobs und verwalten die Gesamtschleife.
- **Fetchers** – Rufen neue Tickets von externen Systemen ab.
- **Preparers** – Wandeln rohe Ticket-Daten in eine für KI-Modelle geeignete Form um.
- **AI Inference Services** – Laden Hugging-Face-Modelle und erzeugen Vorhersagen für Queue oder Priorität.
- **Modifiers** – Wenden die Vorhersagen über Adapter wieder auf das Ticketsystem an.
- **Ticket System Adapters** – Stellen REST-Integrationen mit Systemen wie OTOBO bereit.

Alle Komponenten werden in einem zentralen Dependency-Injection-Container registriert und über die `config.yml` konfiguriert.

## Diagramme

### Anwendungs-Klassendiagramm
![Anwendungs-Klassendiagramm](../../public/images/application_class_diagram.png)

### Übersichtsdiagramm
![Übersichtsdiagramm](../../public/images/overview.png)

Diese Diagramme veranschaulichen, wie die Pipeline orchestriert wird und wie die einzelnen Komponenten miteinander interagieren.

---