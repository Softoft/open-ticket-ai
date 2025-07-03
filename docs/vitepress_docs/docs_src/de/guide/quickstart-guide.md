---
description: Installieren und starten Sie Open Ticket AI schnell mit Docker Compose. Diese Schritt-für-Schritt-Anleitung zeigt Ihnen, wie Sie die Standard-Worker für die automatisierte Ticketverarbeitung konfigurieren und starten.
title: Open Ticket AI Schnellstart
---
# Schnellstart

Befolgen Sie diese Schritte, um Open Ticket AI mit der Beispielkonfiguration auszuführen.

1. **Repository klonen**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```
2. **Beispielkonfiguration kopieren**
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```
   Passen Sie die `config.yml` mit der URL und den Zugangsdaten Ihres Ticketsystems an.
3. **Dienste starten**
   ```bash
   docker-compose up -d --build
   ```
4. **Logs überwachen (optional)**
   ```bash
   docker-compose logs -f
   ```

Die Warteschlangen- und Prioritäts-Worker beginnen automatisch mit der Verarbeitung von Tickets gemäß Ihrer Konfiguration.