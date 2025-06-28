---
title: Entwicklerinformationen
description: Entwicklerinformationen für die ATC Community Edition
---
# Entwicklerinformationen für die ATC Community Edition

## Überblick

Die ATC Community Edition ist eine On-Premise-Lösung zur automatisierten Klassifizierung von Support-Tickets. Die aktuelle MVP-Version wird über eine YAML-Konfigurationsdatei gesteuert und per CLI gestartet. Es gibt keine REST API zum Hochladen von Trainingsdaten oder zum Auslösen eines Trainingslaufs.

## Softwarearchitektur

Die Anwendung besteht im Wesentlichen aus den folgenden Paketen:

* **core** – Basisklassen, Konfigurationsmodelle und Hilfsfunktionen.
* **run** – enthält die Pipeline für die Ticket-Klassifizierung.
* **ticket\_system\_integration** – Adapter für verschiedene Ticketsysteme.
* **main.py** – CLI-Einstiegspunkt, der den Scheduler und den Orchestrator startet.

Der Orchestrator führt konfigurierbare `AttributePredictors` aus, die sich aus `DataFetcher`, `DataPreparer`, `AIInferenceService` und `Modifier` zusammensetzen. Alle Komponenten werden in der `config.yml` definiert und beim Programmstart validiert.

Ein Beispielbefehl zum Starten der Anwendung:

```bash
python -m open_ticket_ai.src.ce.main start
```

## Training eigener Modelle

Ein direktes Training über die Anwendung ist im MVP nicht vorgesehen. Vortrainierte Modelle können in der Konfiguration angegeben und verwendet werden. Wenn ein Modell angepasst oder neu erstellt werden muss, muss dies außerhalb der Anwendung geschehen.

## Erweiterung

Benutzerdefinierte Fetcher, Preparer, KI-Services oder Modifier können als Python-Klassen implementiert und über die Konfiguration registriert werden. Dank Dependency Injection können neue Komponenten einfach integriert werden.

## Zusammenfassung

Die ATC Community Edition bietet in ihrer MVP-Version einen lokal ausgeführten Workflow zur automatischen Ticket-Klassifizierung. Alle Einstellungen werden über YAML-Dateien verwaltet; es ist keine REST API verfügbar. Für das Training müssen externe Prozesse oder Skripte verwendet werden.