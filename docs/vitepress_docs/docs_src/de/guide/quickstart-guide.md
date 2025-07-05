---
description: Installieren und starten Sie Open Ticket AI schnell mit Docker Compose. Diese Schritt-für-Schritt-Anleitung zeigt Ihnen, wie Sie die Standard-Worker für die automatisierte Ticketverarbeitung konfigurieren und starten.
title: Open Ticket AI Schnellstart
---
# Schnellstart

Befolgen Sie diese Schritte, um Open Ticket AI mit der Beispielkonfiguration auszuführen.

1. **Klonen Sie das Repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```
2. **Kopieren Sie die Beispielkonfiguration**
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```
   Passen Sie die `config.yml` mit der URL und den Anmeldeinformationen Ihres Ticketsystems an.
3. **Starten Sie die Dienste**
   ```bash
   docker-compose up -d --build
   ```
4. **Überwachen Sie die Logs (optional)**
   ```bash
   docker-compose logs -f
   ```

Die Queue- und Priority-Worker beginnen automatisch mit der Verarbeitung von Tickets gemäß Ihrer Konfiguration.