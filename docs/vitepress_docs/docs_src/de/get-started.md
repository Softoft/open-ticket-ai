---
description: Erfahren Sie, wie Sie Open Ticket AI mit Docker Compose schnell installieren und ausführen. Diese Anleitung bietet einfache Einrichtungsanweisungen für die Integration mit Ihrem OTRS-, OTOBO- oder Znuny-Helpdesk über Web Services.
title: Erste Schritte
---
# Installation

1. **Klonen Sie das Repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```

2. **Kopieren Sie die Beispielkonfiguration**
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```

3. **Erstellen und starten Sie die Dienste**
   ```bash
   docker-compose up -d --build
   ```

Open Ticket AI kommuniziert mit Ihrem Ticketsystem über Web Services; es gibt keine externe API.

# Ticketsystem-Integration

Derzeit sind Integrationen für **OTRS**, **OTOBO** und **Znuny** verfügbar. Die Einrichtung ist für alle drei Systeme identisch:

1. Konfigurieren Sie die erforderlichen Web Services in Ihrem Ticketsystem.
2. Erstellen Sie einen dedizierten Benutzer oder Agenten für den Zugriff durch Open Ticket AI.
3. Richten Sie die Integration auf die URL und die Anmeldeinformationen dieses Web Service-Benutzers aus.

Detaillierte Anweisungen finden Sie in den entsprechenden Anleitungen für die ersten Schritte für Ihr Ticketsystem.