---
title: Open Ticket AI installieren
description: Schritt-für-Schritt-Anleitung zur Installation von Open Ticket AI.
---

# Installation

Befolgen Sie diese Schritte, um Open Ticket AI zu installieren:

1.  **Das Repository klonen**
    ```bash
    git clone https://github.com/your-org/open-ticket-ai.git
    cd open-ticket-ai
    ```

2.  **Eine `config.yml` erstellen**
    Details zum Einrichten dieser Datei finden Sie in der Dokumentation zur.

3.  **Mit Docker Compose starten**
    Dieser Befehl erstellt die notwendigen Docker-Images und startet die Anwendungsdienste im Detached-Modus.
    ```bash
    docker-compose up -d --build
    ```

4.  **Logs überwachen**
    Sie können die Logs der laufenden Dienste überwachen, um sicherzustellen, dass alles korrekt startet.
    ```bash
    docker-compose logs -f
    ```
