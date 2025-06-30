---
description: Entdecken Sie die Architektur von Open Ticket AI, einer modularen Pipeline, die Transformer-Modelle verwendet, um Support-Tickets automatisch nach Warteschlange und Priorität zu verarbeiten und zu klassifizieren und so die Arbeitsabläufe im Helpdesk zu optimieren.
title: Open Ticket AI Architektur
---
# Architektur

## Pipeline & Value Objects

Der Kern von Open Ticket AI ist seine Verarbeitungspipeline:

```
[ Eingehendes Ticket ]
       ↓
[ Vorverarbeiter ] — bereinigt & verbindet Betreff+Text
       ↓
[ Transformer Tokenizer ]
       ↓
[ Warteschlangen-Klassifikator ] → Warteschlangen-ID + Konfidenz
       ↓
[ Prioritäts-Klassifikator ] → Prioritäts-Score + Konfidenz
       ↓
[ Nachverarbeiter ] — wendet Schwellenwerte an, leitet weiter oder markiert
       ↓
[ Ticketsystem-Adapter ] — aktualisiert Ticket via REST API
```

Jede Stufe in dieser Pipeline konsumiert und produziert **Value Objects** (z. B. `subject`, `body`, `queue_id`, `priority`). Dieses Design macht die Pipeline modular und einfach erweiterbar mit benutzerdefinierten Verarbeitungsschritten oder neuen Value Objects.

## Systemdiagramme

### Anwendungs-Klassendiagramm
![Anwendungs-Klassendiagramm](/images/application_class_diagram.png)

### Übersichtsdiagramm
![Übersichtsdiagramm](/images/overview.png)