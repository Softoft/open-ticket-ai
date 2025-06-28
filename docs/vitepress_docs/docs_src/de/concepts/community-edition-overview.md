---
title: ATC Community Edition Übersicht
description: Eine umfassende Übersicht über die Funktionen und Anwendungsfälle der ATC Community Edition.
---

# ATC Community Edition Übersicht

## Einleitung

Die ATC (Automated Ticket Classification) Community Edition ist eine fortschrittliche Lösung zur automatisierten Klassifizierung von Support-Tickets. Sie ist kostenlos, on-premise und kann auf jedem Betriebssystem installiert werden, das Docker unterstützt. Diese Dokumentation bietet eine umfassende Übersicht über die Funktionen und Anwendungsfälle von ATC.

## Hauptmerkmale

### Einfache Installation

ATC kann schnell und einfach auf Ihrem Server mithilfe von Docker-Containern installiert werden. Durch die Nutzung von Docker werden die Bereitstellung und Verwaltung der Anwendung vereinfacht, was eine schnelle Inbetriebnahme ermöglicht.

### Leistungsstarke API

ATC bietet eine robuste HTTP REST API, über die Benutzer Daten zur Verarbeitung senden, das Training von Modellen initiieren und Klassifizierungsergebnisse abrufen können. Die API ist darauf ausgelegt, hohe Flexibilität und eine nahtlose Integration in bestehende Systeme zu ermöglichen.

### Datentransfer und Training

Benutzer können Trainingsdaten oder CSV-Dateien über die REST API an ATC senden. Das Training des Modells kann ebenfalls über die API ausgelöst werden, wodurch der gesamte Workflow der Datenverarbeitung und Modelloptimierung automatisiert wird.

### Automatisierte Klassifizierung

Einmal trainiert, kann ATC eingehende Support-Tickets automatisch klassifizieren. Die Klassifizierung basiert auf den Mustern, die während des Trainings gelernt wurden, und gewährleistet so eine konsistente und genaue Zuweisung der Tickets.

### OTOBO-Integration

ATC bietet ein dediziertes Add-on für das OTOBO-Ticketsystem, das eine nahtlose Integration ermöglicht. Dieses Add-on sammelt Daten aus OTOBO und nutzt ATC zur automatisierten Ticket-Klassifizierung, was die Effizienz und Genauigkeit bei der Ticketbearbeitung erheblich verbessert.

### Hohe Sicherheit

Datensicherheit und der Schutz der Kundendaten haben oberste Priorität. Die gesamte Datenverarbeitung erfolgt lokal auf dem Server, ohne externe Speicherung oder Verarbeitung. Dies gewährleistet die vollständige Einhaltung der Datenschutzanforderungen.

### Flexibilität und Anpassbarkeit

ATC bietet hohe Flexibilität durch anpassbare Konfigurationen. Benutzer können die Einstellungen an ihre spezifischen Bedürfnisse anpassen, um optimale Ergebnisse zu erzielen.

## Installation und Nutzung

### Docker-Installation

ATC kann einfach mit Docker auf Ihrem Server installiert werden. Führen Sie die folgenden Schritte zur Installation aus:

1.  **Docker installieren**:

    ```bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```

2.  **ATC-Container ausführen**:

    ```bash
    docker run -d -p 8080:80
    ```

### API-Nutzung

Nach der Installation haben Sie HTTP-REST-Zugriff auf die ATC-API. Sie können Daten an die API senden, um das Training zu starten und Klassifizierungsergebnisse abzurufen.

#### Senden von Trainingsdaten

Senden Sie Ihre Trainingsdaten oder eine CSV-Datei an die ATC REST API:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

#### Training starten

Das Training des Modells auslösen:

```bash
curl -X POST http://your-server:8080/api/start-training
```

#### Tickets klassifizieren

Senden Sie nach dem Training Tickets zur Klassifizierung an die API und erhalten Sie die entsprechenden Labels:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Your ticket content"}'
```

## Zukünftige Erweiterungen

Wir planen, in Zukunft zusätzliche Integrations-Add-ons für verschiedene Systeme bereitzustellen. Bleiben Sie auf dem Laufenden für die neuesten Updates.

## Zusammenfassung

Die ATC Community Edition ist eine leistungsstarke, kostenlose Lösung zur automatisierten Klassifizierung von Support-Tickets. Mit einer benutzerfreundlichen API, einer einfachen Docker-Installation und einer nahtlosen OTOBO-Integration bietet ATC eine flexible und skalierbare Möglichkeit, Ihre Support-Prozesse zu optimieren und die Effizienz Ihres Teams zu steigern.

Für weitere Informationen besuchen Sie unsere Website: [SoftOft](https://softoft.de/otobo/docs)