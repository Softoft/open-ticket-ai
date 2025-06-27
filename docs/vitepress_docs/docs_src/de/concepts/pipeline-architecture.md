```markdown
---
title: Open Ticket AI-Architektur
description: Erfahren Sie mehr über die Architektur von Open Ticket AI.
---

# Architektur

## Pipeline & Wertobjekte

Der Kern von Open Ticket AI ist die Verarbeitungspipeline:

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
![Anwendungsklassendiagramm](/images/application_class_diagram.png)

### Übersichtsdiagramm
![Übersichtsdiagramm](/images/overview.png)
```

**Übersetzungshinweise:**
1. **Frontmatter:** Schlüssel unverändert, Werte idiomatisch übersetzt ("Architektur", "Erfahren Sie mehr über...")
2. **Technische Begriffe:** "Value Objects" als "Wertobjekte" übersetzt (Standardterminologie im Software-Design)
3. **Codeblöcke:** Vollständig unverändert übernommen (inkl. englischer Kommentare)
4. **Bildbeschriftungen:** "Application Class Diagram" → "Anwendungsklassendiagramm", "Overview Diagram" → "Übersichtsdiagramm"
5. **Pfade:** Bild-URLs (`/images/...`) original belassen
6. **Stil:** Dokumentationston mit präzisen Fachbegriffen ("Verarbeitungspipeline", "benutzerdefinierte Verarbeitungsschritte")