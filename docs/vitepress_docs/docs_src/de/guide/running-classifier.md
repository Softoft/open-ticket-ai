---
description: Erfahren Sie, wie Sie Open Ticket AI mit Docker Compose verwenden, um die Ticket-Klassifizierung zu automatisieren. Diese Anleitung erklärt, wie Sie Queue- und Priority-Worker ausführen, um Support-Tickets basierend auf KI-Vorhersagen intelligent weiterzuleiten und zu priorisieren.
title: Verwendung von Open Ticket AI
---
# Verwendung

Dieser Abschnitt beschreibt, wie Sie Open Ticket AI für seine Hauptfunktion ausführen: die Klassifizierung von Tickets.

## Inferenz ausführen

Sobald Open Ticket AI installiert und konfiguriert ist, können Sie den Klassifizierungsprozess mit Docker Compose starten:

```bash
docker-compose up classifier
```

Dieser Befehl startet die erforderlichen Dienste, typischerweise einschließlich:

*   **Queue Worker**: Ruft Tickets ab, verwendet das konfigurierte `model`, um die passende `queue` vorherzusagen, und aktualisiert dann das Ticket in Ihrem System (z. B. verschiebt es in die vorhergesagte `queue` oder markiert es basierend auf Konfidenzniveaus).
*   **Priority Worker**: Ähnlich wie der `Queue Worker`, konzentriert sich jedoch auf die Vorhersage und Zuweisung der Ticket-Priorität.

Diese Worker überwachen kontinuierlich die eingehende `queue` (wie in Ihrer `config.yml` definiert) und verarbeiten neue Tickets, sobald sie eintreffen.

*(Hinweis: Die genauen Dienstnamen und das Verhalten können je nach Ihrer spezifischen Konfiguration und Version von Open Ticket AI variieren.)*