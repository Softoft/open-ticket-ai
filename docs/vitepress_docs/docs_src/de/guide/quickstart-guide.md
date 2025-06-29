---
title: Installation und Nutzung von ATC
description: Installieren Sie ATC auf Ihrem Server und nutzen Sie die API zur automatisierten Klassifizierung von Support-Tickets.
---
# Installation von ATC

ATC kann einfach mit Docker auf Ihrem Server installiert werden. Führen Sie die folgenden Schritte aus, um die Installation durchzuführen:

## Schritt 1: Docker installieren

Zuerst müssen Sie Docker auf Ihrem Server installieren. Führen Sie die folgenden Befehle aus, um Docker zu installieren:

```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Schritt 2: Den ATC-Container ausführen

Nachdem Docker installiert ist, können Sie den ATC-Container ausführen. Verwenden Sie den folgenden Befehl, um den Container zu starten:

```bash
docker run -d -p 8080:80 your-docker-repo/atc:latest
```

Dieser Befehl lädt das neueste ATC Docker-Image aus Ihrem Repository und startet es auf Port 8080.

# Nutzung der ATC-API

Nach der Installation haben Sie HTTP-REST-Zugriff auf die ATC-API. Hier sind einige grundlegende Befehle zur Nutzung der API:

## Senden von Trainingsdaten

Um Trainingsdaten oder eine CSV-Datei an die ATC-REST-API zu senden, verwenden Sie den folgenden Befehl:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

Dieser Befehl sendet die Datei `yourfile.csv` an die API, um sie für das Training zu verwenden.

## Starten des Trainings

Um das Training des Modells zu starten, verwenden Sie diesen Befehl:

```bash
curl -X POST http://your-server:8080/api/start-training
```

Dieser Befehl startet den Trainingsprozess basierend auf den zuvor gesendeten Daten.

## Klassifizieren von Tickets

Nach erfolgreichem Training können Sie Ticketdaten zur Klassifizierung an die API senden und die entsprechenden Labels erhalten:

```bash
curl -X POST http://your-server:8080/api/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Your ticket content"}'
```

Dieser Befehl sendet den Ticketinhalt zur Klassifizierung und gibt die Klassifizierungs-Labels zurück.

# Zusammenfassung

Mit diesen Schritten können Sie ATC auf Ihrem Server installieren und die grundlegenden API-Funktionen nutzen. ATC bietet eine leistungsstarke, flexible Lösung für die automatisierte Klassifizierung von Support-Tickets, die einfach zu installieren und zu verwenden ist.

Dieser Abschnitt beschreibt die Installation von ATC und die grundlegenden API-Befehle im Detail. Sie können ihn anpassen und erweitern, um zusätzliche Informationen oder spezifische Anweisungen aufzunehmen.
