---
title: Open Ticket AI Architektur
description: Erfahren Sie mehr über die Architektur von Open Ticket AI.
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

## Systemdiagramme
