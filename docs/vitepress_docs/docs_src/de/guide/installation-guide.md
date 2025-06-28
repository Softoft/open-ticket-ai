---
title: Installation von Open Ticket AI
description: Schritt-für-Schritt-Anleitung zur Installation von Open Ticket AI.
---

# Installation

Folgen Sie diesen Schritten, um Open Ticket AI zu installieren:

1.  **Repository klonen**
    ```bash
    git clone https://github.com/your-org/open-ticket-ai.git
    cd open-ticket-ai
    ```

2.  **`config.yml` erstellen**
    Details zur Einrichtung dieser Datei finden Sie in der [Konfigurationsdokumentation](../reference/configuration-reference.md).

3.  **Mit Docker Compose starten**
    Dieser Befehl erstellt die erforderlichen Docker-Images und startet die Anwendungsdienste im Hintergrundmodus.
    ```bash
    docker-compose up -d --build
    ```

4.  **Logs überwachen**
    Sie können die Logs der laufenden Dienste überwachen, um sicherzustellen, dass alles korrekt startet.
    ```bash
    docker-compose logs -f
    ```