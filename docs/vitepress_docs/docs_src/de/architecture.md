---
title: Übersicht über die Architektur von Open Ticket AI
description: Überblick auf hoher Ebene über die Komponenten und den Datenfluss in Open Ticket AI.
---

# Architekturübersicht

Open Ticket AI basiert auf einer modularen Pipeline, die jedes Ticket in einer Reihe von klar definierten Stufen verarbeitet. Das System setzt auf Dependency Injection und Konfigurationsdateien, um diese Stufen zusammenzusetzen, was es einfach macht, einzelne Teile zu erweitern oder auszutauschen.

## Verarbeitungspipeline

Der Ticket-Verarbeitungsprozess folgt diesem Ablauf:

```
[ Incoming Ticket ]
       ↓
[ Preprocessor ] — cleans & merges subject+body
       ↓
[ Transformer Tokenizer ]
       ↓
[ Queue Classifier ] → Queue ID + confidence
       ↓
[ Priority Classifier ] → Priority score + confidence
       ↓
[ Postprocessor ] — applies thresholds, routes or flags
       ↓
[ Ticket System Adapter ] — updates ticket via REST API
```

Jeder Schritt verbraucht und produziert **Value Objects** wie `subject`, `body`, `queue_id` und `priority`. Dieser Ansatz hält die Pipeline modular und ermöglicht es, neue Schritte oder Value Objects mit minimalen Änderungen am restlichen System hinzuzufügen.

## Hauptkomponenten

- **App & Orchestrator** – Validiert die Konfiguration, plant Jobs ein und verwaltet den Gesamtprozess.
- **Fetchers** – Ruft neue Tickets von externen Systemen ab.
- **Preparers** – Transformiert Rohdaten von Tickets in eine für KI-Modelle geeignete Form.
- **AI Inference Services** – Lädt Hugging Face-Modelle und erzeugt Vorhersagen für Warteschlangen oder Prioritäten.
- **Modifiers** – Wendet die Vorhersagen über Adapter auf das Ticketsystem an.
- **Ticket System Adapters** – Bietet REST-Integrationen mit Systemen wie OTOBO.

Alle Komponenten sind in einem zentralen Dependency-Injection-Container registriert und werden über `config.yml` konfiguriert.

## Diagramme

### Anwendungs-Klassendiagramm
![Anwendungs-Klassendiagramm](/images/application_class_diagram.png)

### Übersichtsdiagramm
![Übersichtsdiagramm](/images/overview.png)

Diese Diagramme veranschaulichen, wie die Pipeline orchestriert wird und wie die einzelnen Komponenten miteinander interagieren.