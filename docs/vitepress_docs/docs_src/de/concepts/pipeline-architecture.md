---
description: Erkunden Sie die Architektur von Open Ticket AI, einer modularen Pipeline, die Transformer-Modelle nutzt, um Support-Tickets automatisch nach Warteschlange und Priorität zu klassifizieren, Helpdesk-Workflows zu optimieren und über eine REST-API in Ticketsysteme zu integrieren.
title: Architektur von Open Ticket AI
---
# Architektur

## Pipeline & Value Objects

Das Herzstück von Open Ticket AI ist seine Verarbeitungspipeline:

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

Jede Stufe in dieser Pipeline konsumiert und produziert **Value Objects** (z.B. `subject`, `body`, `queue_id`, `priority`). Dieses Design macht die Pipeline modular und einfach erweiterbar mit benutzerdefinierten Verarbeitungsschritten oder neuen Value Objects.

## Pipeline-Komponenten

- **Pipeline** – Ein Container, der eine Sequenz von Pipes ausführt. Er steuert den
  Gesamtstatus und stoppt die Ausführung, wenn eine Pipe einen Fehler meldet.
- **Pipe** – Ein einzelner Verarbeitungsschritt, der eine `process()`-Methode implementiert.
  Pipes erben vom `Providable`-Mixin, sodass sie aus dem
  Dependency-Injection-Container erstellt werden können.
- **PipelineContext** – Ein Pydantic-`model`, das an jede Pipe übergeben wird. Es speichert die
  Ticket-ID, von Pipes erzeugte beliebige Daten und Metainformationen wie den
  aktuellen Pipeline-Status. Pipes lesen und schreiben in dieses Kontextobjekt, um
  Daten auszutauschen.

## Systemdiagramme

### Anwendungsklassendiagramm

### Übersichtsdiagramm