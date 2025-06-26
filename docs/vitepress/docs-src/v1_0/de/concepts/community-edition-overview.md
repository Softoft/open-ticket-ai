---
title: ATC Community Edition Überblick
description: Eine umfassende Übersicht über die Funktionen und Einsatzmöglichkeiten der ATC Community Edition.
---
:::warning
Die ATC CE ist noch nicht veröffentlicht.
:::

# ATC Community Edition Überblick

## Einführung

Die ATC (Automated Ticket Classification) Community Edition ist eine fortschrittliche Lösung zur automatisierten
Klassifizierung von Support-Tickets. Sie ist kostenlos, On-Premise und kann auf jedem Betriebssystem installiert werden,
das Docker unterstützt. Diese Dokumentation bietet eine umfassende Übersicht über die Funktionen und
Einsatzmöglichkeiten von ATC.

## Hauptfunktionen

### Einfache Installation

ATC lässt sich schnell und einfach auf Ihrem Server mit Docker installieren. Durch die Nutzung von Docker-Containern
wird die Bereitstellung und Verwaltung der Anwendung vereinfacht, was eine schnelle Inbetriebnahme ermöglicht.

### Leistungsstarke API

ATC bietet eine robuste HTTP REST API, über die Benutzer Daten zur Verarbeitung senden, das Training des Modells starten
und Klassifizierungsergebnisse abrufen können. Die API ist darauf ausgelegt, eine hohe Flexibilität und Integration in
bestehende Systeme zu ermöglichen.

### Datenübertragung und Training

Benutzer können Trainingsdaten oder CSV-Dateien über die REST API an ATC senden. Das Training des Modells kann ebenfalls
über die API gestartet werden, wodurch der gesamte Prozess der Datenverarbeitung und Modelloptimierung automatisiert
wird.

### Automatisierte Klassifizierung

Nach dem Training kann ATC automatisch eingehende Support-Tickets klassifizieren. Die Klassifizierung erfolgt anhand der
im Training gelernten Muster, wodurch eine konsistente und genaue Zuordnung von Tickets gewährleistet wird.

### OTOBO Integration

ATC bietet ein spezielles Add-On für das OTOBO Ticketsystem, das eine nahtlose Integration ermöglicht. Dieses Add-On
sammelt Daten aus dem OTOBO System und nutzt ATC zur automatisierten Klassifizierung von Tickets. Dies verbessert die
Effizienz und Genauigkeit der Ticketbearbeitung erheblich.

### Hohe Sicherheit

Die Sicherheit und der Schutz von Kundendaten haben höchste Priorität. Alle Datenverarbeitungsprozesse finden lokal auf
dem Server statt, ohne dass Daten extern gespeichert oder verarbeitet werden. Dies stellt sicher, dass alle
Datenschutzanforderungen erfüllt werden.

### Flexibilität und Anpassungsfähigkeit

ATC bietet eine hohe Flexibilität durch anpassbare Konfigurationen. Benutzer können die Einstellungen an ihre
spezifischen Bedürfnisse anpassen, um optimale Ergebnisse zu erzielen.

## Installation und Nutzung

### Docker-Installation

ATC kann einfach auf Ihrem Server mit Docker installiert werden. Folgen Sie den untenstehenden Schritten, um die
Installation durchzuführen:

1. **Docker installieren**:
    ```bash
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    ```

2. **ATC Container ausführen**:
    ```bash
    docker run -d -p 8080:80 
    ```

### API-Nutzung

Nach der Installation haben Sie über HTTP REST Zugriff auf die ATC API. Sie können Daten zur API senden, um das Training
zu starten und die Klassifizierungsergebnisse abzurufen.

#### Trainingsdaten senden

Senden Sie Ihre Trainingsdaten oder eine CSV-Datei zur ATC REST API:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

#### Training starten

Starten Sie das Training des Modells:

```bash
curl -X POST http://your-server:8080/api/start-training
```

#### Klassifizierung von Tickets

Nach dem Training können Sie Tickets zur Klassifizierung an die API senden und erhalten die entsprechenden Labels
zurück:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Ihr Ticketinhalt"}'
```

## Zukünftige Erweiterungen

Wir planen, in Zukunft weitere Integrations-Add-Ons für verschiedene Systeme bereitzustellen. Bleiben Sie auf dem
Laufenden, um die neuesten Updates zu erhalten.

## Zusammenfassung

ATC Community Edition ist eine leistungsstarke, kostenlose Lösung zur automatisierten Klassifizierung von
Support-Tickets. Mit einer benutzerfreundlichen API, einfacher Docker-Installation und nahtloser OTOBO-Integration
bietet ATC eine flexible und skalierbare Möglichkeit, Ihre Support-Prozesse zu optimieren und die Effizienz Ihres Teams
zu steigern.

Weitere Informationen finden Sie auf unserer Webseite: [SoftOft](https://softoft.de/otobo/docs)