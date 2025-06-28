---
title: Übersicht der ATC Community Edition
description: Ein umfassender Überblick über die Funktionen und Anwendungsfälle der ATC Community Edition.
---

# Übersicht der ATC Community Edition

## Einführung

Die ATC (Automatisierte Ticket-Klassifizierung) Community Edition ist eine fortschrittliche Lösung zur automatischen Klassifizierung von Support-Tickets. Sie ist kostenlos, On-Premise und kann auf jedem Betriebssystem installiert werden, das Docker unterstützt. Diese Dokumentation bietet einen umfassenden Überblick über die Funktionen und Anwendungsfälle von ATC.

## Hauptfunktionen

### Einfache Installation

ATC kann mithilfe von Docker-Containern schnell und einfach auf Ihrem Server installiert werden. Durch die Nutzung von Docker werden die Bereitstellung und Verwaltung der Anwendung vereinfacht, was einen schnellen Start ermöglicht.

### Leistungsstarke API

ATC bietet eine robuste HTTP REST API, über die Benutzer Daten zur Verarbeitung senden, Modelltraining starten und Klassifizierungsergebnisse abrufen können. Die API ist für hohe Flexibilität und nahtlose Integration in bestehende Systeme konzipiert.

### Datentransfer und Training

Benutzer können Trainingsdaten oder CSV-Dateien über die REST API an ATC senden. Modelltraining kann ebenfalls über die API ausgelöst werden, wodurch der gesamte Workflow der Datenverarbeitung und Modelloptimierung automatisiert wird.

### Automatisierte Klassifizierung

Nach dem Training kann ATC eingehende Support-Tickets automatisch klassifizieren. Die Klassifizierung basiert auf den während des Trainings erlernten Mustern und gewährleistet eine konsistente und präzise Ticketzuordnung.

### OTOBO-Integration

ATC bietet ein spezielles Add-on für das OTOBO-Ticketsystem, das eine nahtlose Integration ermöglicht. Dieses Add-on sammelt Daten aus OTOBO und nutzt ATC zur automatischen Ticketklassifizierung, was die Effizienz und Genauigkeit im Ticketblich verbessert.

### Hohe Sicherheit

Datensicherheit und Kundendatenschutz haben höchste Priorität. Die gesamte Datenverarbeitung erfolgt lokal auf dem Server, ohne externe Speicherung oder Verarbeitung. Dies gewährleistet vollständige Compliance mit Datenschutzanforderungen.

### Flexibilität und Anpassbarkeit

ATC bietet durch anpassbare Konfigurationen hohe Flexibilität. Benutzer können die Einstellungen an ihre spezifischen Anforderungen anpassen, um optimale Ergebnisse zu erzielen.

## Installation und Verwendung

### Docker-Installation

ATC kann einfach mit Docker auf Ihrem Server installiert werden. Folgen Sie diesen Schritten:

1. **Docker installieren**:

   ```bash
   sudo apt-get update
   sudo apt-get install docker-ce docker-ce-cli containerd.io
   ```

2. **ATC-Container starten**:

   ```bash
   docker run -d -p 8080:80
   ```

### API-Verwendung

Nach der Installation haben Sie HTTP REST-Zugriff auf die ATC-API. Sie können Daten an die API senden, um Training zu starten und Klassifizierungsergebnisse abzurufen.

#### Trainingsdaten senden

Senden Sie Ihre Trainingsdaten oder eine CSV-Datei an die ATC REST API:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

#### Training starten

Starten Sie das Modelltraining:

```bash
curl -X POST http://your-server:8080/api/start-training
```

#### Tickets klassifizieren

Nach dem Training senden Sie Tickets zur Klassifizierung an die API und erhalten die entsprechenden Labels:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Your ticket content"}'
```

## Zukünftige Erweiterungen

Wir planen, zusätzliche Integrations-Add-ons für verschiedene Systeme bereitzustellen. Bleiben Sie auf dem Laufenden über die neuesten Updates.

## Zusammenfassung

Die ATC Community Edition ist eine leistungsstarke, kostenlose Lösung zur automatischen Klassifizierung von Support-Tickets. Mit einer benutzerfreundlichen API, einfacher Docker-Installation und nahtloser OTOBO-Integration bietet ATC eine flexible und skalierbare Möglichkeit, Ihre Support-Prozesse zu optimieren und die Effizienz Ihres Teams zu steigern.

Weitere Informationen finden Sie auf unserer Website: [SoftOft](https://softoft.de/otobo/docs)