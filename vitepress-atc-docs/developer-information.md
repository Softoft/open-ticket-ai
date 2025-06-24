---
titel: Entwicklerinformationen
description: Entwicklerinformationen für die ATC Community Edition
---
:::warning
Die ATC CE ist noch nicht veröffentlicht.
:::
# Entwicklerinformationen für die ATC Community Edition

## Überblick

Die ATC Community Edition ist eine leistungsstarke, On-Premise-Lösung zur automatisierten Klassifizierung von
Support-Tickets. Diese Dokumentation bietet Entwicklern detaillierte Informationen über die Softwarearchitektur und die
Nutzung der REST API.

## Softwarearchitektur

Die Applikation besteht aus zwei Hauptpaketen: `TRAIN` und `RUN`.

- **TRAIN-Paket**: Dieses Paket enthält den Code zum Trainieren des Modells.
- **RUN-Paket**: Dieses Paket enthält den Code zum Ausführen der Klassifizierung von Tickets.

Entwickler sollten nicht direkt mit diesen Paketen interagieren, sondern die bereitgestellte REST API verwenden, um
Konfigurationen zu verwalten, Trainingsdaten zu senden und Modelle zu trainieren.

### Komponenten

1. **REST API**
    - **POST /api/v1/config**: Konfigurationen senden
    - **GET /api/v1/config**: Konfigurationen abrufen
    - **POST /api/v1/train-data**: Trainingsdaten senden
    - **GET /api/v1/train-data**: Trainingsdaten abrufen
    - **POST /api/v1/train**: Modell trainieren
    - **POST /api/v1/classify**: Ticket klassifizieren

2. **ModelRepository**
    - **save_model()**: Modell speichern
    - **load_model()**: Modell laden

3. **Config**
    - **UNCLASSIFIED_QUEUE**: Warteschlange für unklassifizierte Tickets

## Nutzung der REST API

Die REST API ermöglicht die Interaktion mit den verschiedenen Komponenten der ATC Community Edition.

### Konfigurationen verwalten

#### Konfiguration senden

```bash
curl -X POST http://your-server:8080/api/v1/config \
     -H "Content-Type: application/json" \
     -d '{"config_key": "config_value"}'
```

#### Konfiguration abrufen

```bash
curl -X GET http://your-server:8080/api/v1/config
```

### Trainingsdaten verwalten

#### Trainingsdaten senden

```bash
curl -X POST http://your-server:8080/api/v1/train-data \
     -H "Content-Type: text/csv" \
     --data-binary @yourfile.csv
```

#### Trainingsdaten abrufen

```bash
curl -X GET http://your-server:8080/api/v1/train-data
```

### Modell trainieren

Um das Modell zu trainieren, verwenden Sie den folgenden Befehl:

```bash
curl -X POST http://your-server:8080/api/v1/train
```

### Ticket klassifizieren

Um ein Ticket zu klassifizieren, verwenden Sie den folgenden Befehl:

```bash
curl -X POST http://your-server:8080/api/v1/classify \
     -H "Content-Type: application/json" \
     -d '{"ticket_data": "Ihr Ticketinhalt"}'
```

## Zusammenfassung

Mit diesen Informationen können Entwickler die ATC Community Edition effektiv nutzen und in ihre bestehenden Systeme
integrieren. Durch die Verwendung der REST API können alle wichtigen Funktionen der ATC Community Edition gesteuert und
verwaltet werden.
