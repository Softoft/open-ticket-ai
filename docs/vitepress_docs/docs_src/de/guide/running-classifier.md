---
title: Verwendung von Open Ticket AI
description: Wie man Open Ticket AI zur Ticket-Klassifizierung ausführt und verwendet.
---

# Verwendung

Dieser Abschnitt beschreibt, wie man Open Ticket AI für seine Hauptfunktion ausführt: die Klassifizierung von Tickets.

## Inferenz ausführen

Sobald Open Ticket AI installiert und konfiguriert ist, können Sie den Klassifizierungsprozess mit Docker Compose starten:

```bash
docker-compose up classifier
```

Dieser Befehl startet die erforderlichen Dienste, typischerweise einschließlich:

*   **Queue Worker**: Ruft Tickets ab, verwendet das konfigurierte Modell, um die passende Warteschlange vorherzusagen, und aktualisiert dann das Ticket in Ihrem System (z. B. verschiebt es in die vorhergesagte Warteschlange oder markiert es basierend auf Konfidenzniveaus).
*   **Priority Worker**: Ähnlich wie der Queue Worker, konzentriert sich aber auf die Vorhersage und Zuweisung der Ticket-Priorität.

Diese Worker überwachen kontinuierlich die eingehende Warteschlange (wie in Ihrer `config.yml` definiert) und verarbeiten neue Tickets, sobald sie eintreffen.

*(Hinweis: Die genauen Dienstnamen und das Verhalten können je nach Ihrer spezifischen Konfiguration und Version von Open Ticket AI variieren.)*