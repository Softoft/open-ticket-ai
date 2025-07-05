---
description: Erkunden Sie die Architektur von Open Ticket AI, einer modularen Pipeline, die Transformer-Modelle nutzt, um Support-Tickets automatisch nach Warteschlange und Priorität zu klassifizieren. Dies optimiert Helpdesk-Workflows und integriert sich über eine REST-API in Ticketsysteme.
title: Open Ticket AI Architektur
---
# Architektur

## Pipeline & Value Objects

Der Kern von Open Ticket AI ist seine Verarbeitungspipeline:

```
[ Eingehendes Ticket ]
       ↓
[ Preprocessor ] — bereinigt & führt Betreff+Text zusammen
       ↓
[ Transformer Tokenizer ]
       ↓
[ Queue Classifier ] → Queue-ID + Konfidenz
       ↓
[ Priority Classifier ] → Prioritäts-Score + Konfidenz
       ↓
[ Postprocessor ] — wendet Schwellenwerte an, leitet weiter oder markiert
       ↓
[ Ticket System Adapter ] — aktualisiert Ticket über REST API
```

Jede Stufe in dieser Pipeline konsumiert und produziert **Value Objects** (z. B. `subject`, `body`, `queue_id`, `priority`). Dieses Design macht die Pipeline modular und einfach durch benutzerdefinierte Verarbeitungsschritte oder neue Value Objects erweiterbar.

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