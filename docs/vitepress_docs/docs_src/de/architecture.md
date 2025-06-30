---
description: Erkunden Sie die technische Architektur von Open Ticket AI. Erfahren Sie, wie die modulare Daten-Pipeline und die Hugging Face-Modelle eine intelligente Ticket-Klassifizierung und -Weiterleitung ermöglichen.
title: Open Ticket AI Architekturübersicht
---
# Architekturübersicht

Open Ticket AI basiert auf einer modularen Pipeline, die jedes Ticket durch eine Reihe klar definierter Stufen verarbeitet. Das System nutzt Dependency Injection und Konfigurationsdateien, um diese Stufen zusammenzusetzen, was es einfach macht, einzelne Teile zu erweitern oder zu ersetzen.

## Verarbeitungs-Pipeline

Die Ticket-Verarbeitungs-Pipeline sieht wie folgt aus:

```
[ Eingehendes Ticket ]
       ↓
[ Präprozessor ] — bereinigt & verbindet subject+body
       ↓
[ Transformer Tokenizer ]
       ↓
[ Queue-Klassifikator ] → Queue-ID + Konfidenz
       ↓
[ Prioritäts-Klassifikator ] → Prioritäts-Score + Konfidenz
       ↓
[ Postprozessor ] — wendet Schwellenwerte an, leitet weiter oder markiert
       ↓
[ Ticketsystem-Adapter ] — aktualisiert Ticket über REST API
```

Jeder Schritt konsumiert und produziert **Value Objects** wie `subject`, `body`, `queue_id` und `priority`. Dieser Ansatz hält die Pipeline modular und ermöglicht das Hinzufügen neuer Schritte oder Value Objects mit minimalen Änderungen am Rest des Systems.

## Hauptkomponenten

- **App & Orchestrator** – Validieren die Konfiguration, planen Jobs und verwalten die Gesamtschleife.
- **Fetcher** – Rufen neue Tickets von externen Systemen ab.
- **Preparer** – Transformieren rohe Ticketdaten in eine für KI-Modelle geeignete Form.
- **AI Inference Services** – Laden Hugging Face-Modelle und erzeugen Queue- oder Prioritätsvorhersagen.
- **Modifier** – Wenden die Vorhersagen über Adapter wieder auf das Ticketsystem an.
- **Ticketsystem-Adapter** – Stellen REST-Integrationen mit Systemen wie OTOBO bereit.

Alle Komponenten werden in einem zentralen Dependency-Injection-Container registriert und über `config.yml` konfiguriert.

## Diagramme

### Anwendungs-Klassendiagramm
![Anwendungs-Klassendiagramm](../../public/images/application_class_diagram.png)

### Übersichtsdiagramm
![Übersichtsdiagramm](../../public/images/overview.png)

Diese Diagramme veranschaulichen, wie die Pipeline orchestriert wird und wie die einzelnen Komponenten miteinander interagieren.

---