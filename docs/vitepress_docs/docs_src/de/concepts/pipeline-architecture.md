---
title: Open Ticket AI-Architektur
description: Erfahren Sie mehr über die Architektur von Open Ticket AI.
---

# Architektur

## Pipeline & Wertobjekte

Der Kern von Open Ticket AI ist seine Verarbeitungspipeline:

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

Jede Stufe dieser Pipeline verarbeitet und erzeugt **Wertobjekte** (z. B. `subject`, `body`, `queue_id`, `priority`). Dieser Entwurf macht die Pipeline modular und einfach um benutzerdefinierte Verarbeitungsschritte oder neue Wertobjekte erweiterbar.

## Systemdiagramme

### Anwendungsklassendiagramm
![Application Class Diagram](/images/application_class_diagram.png)

### Übersichtsdiagramm
![Overview Diagram](/images/overview.png)