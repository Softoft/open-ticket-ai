```de
---
title: Übersicht der Open Ticket AI-Architektur
description: Überblick über die Komponenten und den Datenfluss in Open Ticket AI.
---

# Architekturübersicht

Open Ticket AI basiert auf einer modularen Pipeline, die jedes Ticket durch eine Reihe klar definierter Stufen verarbeitet. Das System nutzt Dependency Injection und Konfigurationsdateien, um diese Stufen zusammenzusetzen, was das Erweitern oder Austauschen einzelner Komponenten erleichtert.

## Verarbeitungspipeline

Die Ticketverarbeitungspipeline sieht folgendermaßen aus:

```
[ Incoming Ticket ]
       ↓
[ Preprocessor ] — reinigt & vereinigt Betreff+Textkörper
       ↓
[ Transformer Tokenizer ]
       ↓
[ Queue Classifier ] → Warteschlangen-ID + Konfidenz
       ↓
[ Priority Classifier ] → Prioritätswert + Konfidenz
       ↓
[ Postprocessor ] — wendet Schwellenwerte an, leitet weiter oder markiert
       ↓
[ Ticket System Adapter ] — aktualisiert Ticket via REST API
```

Jeder Schritt verarbeitet und erzeugt **Value Objects** wie `subject`, `body`, `queue_id` und `priority`. Dieser Ansatz hält die Pipeline modular und ermöglicht das Hinzufügen neuer Schritte oder Value Objects mit minimalen Änderungen am restlichen System.

## Hauptkomponenten

- **App & Orchestrator** – Validiert Konfigurationen, plant Jobs und verwaltet den Gesamtprozess.
- **Fetchers** – Ruft neue Tickets aus externen Systemen ab.
- **Preparers** – Transformiert Rohdaten von Tickets in eine für KI-Modelle geeignete Form.
- **AI Inference Services** – Lädt Hugging Face-Modelle und erzeugt Vorhersagen für Warteschlangen oder Prioritäten.
- **Modifiers** – Wendet Vorhersagen über Adapter auf das Ticketsystem an.
- **Ticket System Adapters** – Bietet REST-Integrationen mit Systemen wie OTOBO.

Alle Komponenten sind in einem zentralen Dependency Injection-Container registriert und über `config.yml` konfiguriert.

## Diagramme

### Anwendungsklassendiagramm
![Application Class Diagram](/images/application_class_diagram.png)

### Übersichtsdiagramm
![Overview Diagram](/images/overview.png)

Diese Diagramme veranschaulichen, wie die Pipeline orchestriert wird und wie die Komponenten miteinander interagieren.

---```