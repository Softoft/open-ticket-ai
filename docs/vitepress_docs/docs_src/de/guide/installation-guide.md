---
description: Installieren Sie Open Ticket AI mit unserer offiziellen Anleitung. Lernen Sie, wie Sie das Repository klonen, eine Konfigurationsdatei erstellen und die Anwendung mit Docker Compose starten.
title: Installation von Open Ticket AI
---
# Installation

Befolgen Sie diese Schritte, um Open Ticket AI zu installieren:

1.  **Klonen Sie das Repository**
    ```bash
    git clone https://github.com/your-org/open-ticket-ai.git
    cd open-ticket-ai
    ```

2.  **Erstellen Sie eine `config.yml`**
    Details zur Einrichtung dieser Datei finden Sie in der Dokumentation zur [Konfiguration](../reference/configuration-reference.md).

3.  **Starten Sie mit Docker Compose**
    Dieser Befehl erstellt die notwendigen Docker-Images und startet die Anwendungsdienste im Detached-Modus.
    ```bash
    docker-compose up -d --build
    ```

4.  **Protokolle überwachen**
    Sie können die Protokolle der laufenden Dienste überwachen, um sicherzustellen, dass alles korrekt startet.
    ```bash
    docker-compose logs -f
    ```