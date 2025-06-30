---
description: Entdecken Sie, wie Sie ATC einfach mit Docker installieren und die REST-API
  für die automatisierte Klassifizierung von Support-Tickets nutzen können. Diese
  Anleitung bietet schrittweise Anweisungen zum Senden von Trainingsdaten, zum Starten
  des Model-Trainings und zum Klassifizieren neuer Tickets, um Ihren Support-Workflow
  zu optimieren.
title: Installation und Nutzung von ATC
---
-----------------------------------------------------------------------------------------------------

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

# Verwendung der ATC-API

Nach der Installation haben Sie HTTP-REST-Zugriff auf die ATC-API. Hier sind einige grundlegende Befehle zur Verwendung der API:

## Senden von Trainingsdaten

Um Trainingsdaten oder eine CSV-Datei an die ATC-REST-API zu senden, verwenden Sie den folgenden Befehl:

```bash
curl -X POST http://your-server:8080/api/train \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

Dieser Befehl sendet die Datei `yourfile.csv` zur Verwendung im Training an die API.

## Starten des Trainings

Um das Model-Training zu starten, verwenden Sie diesen Befehl:

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

Dieser Befehl sendet den Ticketinhalt zur Klassifizierung und gibt die Klassifizierungslabels zurück.

# Zusammenfassung

Mit diesen Schritten können Sie ATC auf Ihrem Server installieren und die grundlegenden API-Funktionen nutzen. ATC bietet eine leistungsstarke, flexible Lösung für die automatisierte Klassifizierung von Support-Tickets, die einfach zu installieren und zu verwenden ist.

Dieser Abschnitt beschreibt die Installation von ATC und die grundlegenden API-Befehle im Detail. Sie können ihn anpassen und erweitern, um zusätzliche Informationen oder spezifische Anweisungen aufzunehmen.