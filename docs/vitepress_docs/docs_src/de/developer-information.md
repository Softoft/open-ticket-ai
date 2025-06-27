---
title: Entwicklerinformationen
description: Entwicklerinformationen für die ATC Community Edition
---
:::warning
Die ATC CE ist noch nicht veröffentlicht.
:::

# Entwicklerinformationen für die ATC Community Edition

## Überblick

Die ATC Community Edition ist eine On-Premise-Lösung zur automatisierten
Klassifizierung von Support-Tickets. Die aktuelle MVP-Version wird über eine
YAML-Konfigurationsdatei gesteuert und per CLI gestartet. Es existiert keine
REST API für das Hochladen von Trainingsdaten oder das Anstoßen eines
Trainingslaufes.

## Softwarearchitektur

Die Anwendung besteht im Wesentlichen aus folgenden Paketen:

- **core** – Basisklassen, Konfigurationsmodelle und Hilfsfunktionen.
- **run** – enthält die Pipeline zur Klassifizierung von Tickets.
- **ticket_system_integration** – Adapter für unterschiedliche Ticketsysteme.
- **main.py** – CLI-Einstiegspunkt, der den Scheduler und den Orchestrator startet.

Der Orchestrator führt konfigurierbare `AttributePredictors` aus. Diese setzen
sich aus `DataFetcher`, `DataPreparer`, `AIInferenceService` und `Modifier`
zusammen. Alle Komponenten werden in `config.yml` definiert und beim
Programmstart validiert.

Ein Beispielaufruf zum Starten der Applikation:

```bash
python -m open_ticket_ai.src.ce.main start
```

## Training eigener Modelle

Ein direktes Training über die Anwendung ist im MVP nicht vorgesehen.
Bereits trainierte Modelle können in der Konfiguration eingetragen und
verwendet werden. Soll ein Modell angepasst oder neu erstellt werden,
muss dies außerhalb der Applikation erfolgen.

## Erweiterung

Eigene Fetcher, Preparer, AI-Services oder Modifier können als Python-Klassen
implementiert und über die Konfiguration registriert werden. Dank Dependency
Injection lassen sich neue Komponenten einfach integrieren.

## Zusammenfassung

Die ATC Community Edition bietet in der MVP-Version einen lokal ausgeführten
Workflow zur automatischen Ticketklassifizierung. Alle Einstellungen erfolgen
über YAML-Dateien; eine REST API steht nicht zur Verfügung. Für das Training
müssen externe Prozesse oder Skripte verwendet werden.