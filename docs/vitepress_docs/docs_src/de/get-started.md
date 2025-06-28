---
title: Erste Schritte
description: Installieren Sie Open Ticket AI und integrieren Sie es in Ihr Ticketsystem.
---

# Installation

Open Ticket AI kann schnell mit Docker bereitgestellt werden. Führen Sie den folgenden Befehl auf Ihrem Server aus, um
den Container zu starten:

```bash
docker run -d your-docker-repo/atc:latest
```

Diese Community-Edition stellt **keine** öffentliche REST-API zur Verfügung. Stattdessen findet die gesamte Kommunikation
über die Web Services Ihres Ticketsystems statt.

# Ticketsystem-Integration

Derzeit sind Integrationen für **OTRS**, **OTOBO** und **Znuny** verfügbar. Die Einrichtung ist für alle drei Systeme identisch:

1. Konfigurieren Sie die erforderlichen Web Services in Ihrem Ticketsystem.
2. Erstellen Sie einen dedizierten Benutzer oder Agenten für den Zugriff durch Open Ticket AI.
3. Richten Sie die Integration auf die URL und die Anmeldedaten dieses Web-Service-Benutzers aus.

Detaillierte Anweisungen finden Sie in den entsprechenden Anleitungen für die ersten Schritte für Ihr Ticketsystem.