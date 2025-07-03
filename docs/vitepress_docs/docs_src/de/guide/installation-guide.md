---
description: Erfahren Sie mit dieser Schritt-für-Schritt-Anleitung, wie Sie Open Ticket AI mit Docker Compose installieren. Folgen Sie den Anweisungen, um das Repository zu klonen, eine Konfiguration zu erstellen und die Anwendung bereitzustellen.
title: Installation von Open Ticket AI
---
# Installation

Die empfohlene Methode zur Bereitstellung von Open Ticket AI ist über Docker Compose.

1. **Stellen Sie sicher, dass Docker und Docker Compose auf Ihrem Server installiert sind**.
2. **Klonen Sie das Repository**
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```
3. **Erstellen Sie eine Konfiguration**
   Kopieren Sie die Beispielkonfiguration und passen Sie sie für Ihre Umgebung an:
   ```bash
   cp docs/original_source/_config_examples/queue_priority_local_config.yml config.yml
   ```
4. **Starten Sie die Dienste**
   Erstellen und starten Sie die Container im Hintergrund:
   ```bash
   docker-compose up -d --build
   ```
5. **Überwachen Sie die Protokolle (optional)**
   ```bash
   docker-compose logs -f
   ```