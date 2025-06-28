---
title: Verwendung von Open Ticket AI
description: Wie man Open Ticket AI zur Ticket-Klassifizierung ausführt und verwendet.
---

# Verwendung

Dieser Abschnitt beschreibt, wie Open Ticket AI für seine Hauptfunktion, die Klassifizierung von Tickets, ausgeführt wird.

## Inferenz ausführen

Nach der Installation und Konfiguration von Open Ticket AI können Sie den Klassifizierungsprozess mit Docker Compose starten:

```bash
docker-compose up classifier
```

Dieser Befehl startet die erforderlichen Dienste, typischerweise inklusive:

*   **Queue Worker**: Holt Tickets, verwendet das konfigurierte Modell zur Vorhersage der passenden Warteschlange und aktualisiert das Ticket in Ihrem System (z.B. verschiebt es in die vorhergesagte Warteschlange oder markiert es basierend auf Konfidenzniveaus).
*   **Priority Worker**: Ähnlich wie der Queue Worker, konzentriert sich jedoch auf die Vorhersage und Zuweisung der Ticket-Priorität.

Diese Worker überwachen kontinuierlich die eingehende Warteschlange (wie in Ihrer `config.yml` definiert) und verarbeiten neue Tickets bei Eingang.

*(Hinweis: Die genauen Servicenamen und das Verhalten können je nach Ihrer spezifischen Konfiguration und Version von Open Ticket AI variieren.)*