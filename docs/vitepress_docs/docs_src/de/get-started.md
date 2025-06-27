```markdown
---
title: Erste Schritte
description: Installieren Sie Open Ticket AI und integrieren Sie es in Ihr Ticketsystem.
---

# Installation

Open Ticket AI kann schnell mit Docker bereitgestellt werden. Führen Sie den folgenden Befehl auf Ihrem Server aus, um den Container zu starten:

```bash
docker run -d your-docker-repo/atc:latest
```

Diese Community Edition bietet **keine** öffentliche REST API. Stattdessen erfolgt die gesamte Kommunikation über die Webdienste Ihres Ticketsystems.

# Ticketsystem-Integration

Derzeit sind Integrationen für **OTRS**, **OTOBO** und **Znuny** verfügbar. Die Einrichtung ist für alle drei Systeme identisch:

1. Konfigurieren Sie die notwendigen Webdienste in Ihrem Ticketsystem.
2. Erstellen Sie einen dedizierten Benutzer oder Agenten für den Open Ticket AI-Zugriff.
3. Richten Sie die Integration auf die URL und Anmeldedaten dieses Webdienst-Benutzers aus.

Detaillierte Anweisungen finden Sie in den entsprechenden Erste-Schritte-Anleitungen für Ihr Ticketsystem.
```