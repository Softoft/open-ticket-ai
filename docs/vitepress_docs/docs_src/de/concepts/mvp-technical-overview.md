---
description: Entdecken Sie die technische Architektur des Automated Ticket Classification
  (ATC) MVP. Detailliert beschrieben werden die Verwendung von Hugging Face-Modellen
  zur automatischen Klassifizierung von Queues und Prioritäten sowie die spezifischen
  Schritte zur Integration mit dem OTOBO-Ticketsystem.
title: Technische Übersicht (MVP)
---
# Technische Übersicht (MVP)

Dieses Dokument beschreibt die technischen Kernaspekte des Minimum Viable Product (MVP) für das System zur automatisierten Ticket-Klassifizierung (Automated Ticket Classification, ATC).

## MVP-Funktionen

Das MVP konzentriert sich auf die grundlegenden Fähigkeiten:

*   **Queue-Klassifizierung:** Automatisches Zuweisen von Tickets zum richtigen Team oder zur richtigen Abteilung.
*   **Prioritätsklassifizierung:** Automatisches Bestimmen der Dringlichkeit eines Tickets.

Benutzer können ihre eigenen Hugging Face-Modelle nutzen oder die Standard-ATC-Modelle verwenden. Das Standard-Queue-Modell kann zwischen 42 verschiedenen Klassen unterscheiden, und das Standard-Prioritätsmodell kann 5 Prioritätsstufen differenzieren.

Diese vorhergesagten Queues und Prioritäten können den spezifischen Queues und Prioritäten Ihrer Organisation zugeordnet werden. Konfigurationsoptionen ermöglichen es Ihnen außerdem, Folgendes zu definieren:
*   Die Queue für eingehende Tickets.
*   Die Queue für Tickets, die nicht mit ausreichender Sicherheit klassifiziert werden konnten.
*   Den Konfidenzschwellenwert für das Queue-Modell.

## Implementierung der Architektur

Das MVP verwendet dieselbe Pipeline-Architektur wie der Rest von Open Ticket AI. Eine
Pipeline wird in `config.yml` definiert und listet die Komponenten auf, die der Reihe nach ausgeführt werden sollen.
Typische Stufen umfassen einen Fetcher, Datenaufbereiter, KI-Inferenzdienste und Modifikatoren,
die Ergebnisse zurück in das Helpdesk-System schreiben.

Pipelines werden vom `Orchestrator` ausgeführt, der sie in dem in der Konfiguration festgelegten Intervall plant.
Jede Pipeline fragt das Ticketsystem nach neuen Tickets ab und verarbeitet diese durch die konfigurierten Pipes.

Starten Sie den Dienst mit:

```bash
python -m open_ticket_ai.src.ce.main start
```

Dieser Befehl startet die CLI, lädt die `config.yml`, erstellt den Dependency-Injection-Container und beginnt mit der Ausführung der Pipelines.

Nachfolgend finden Sie einige Diagramme, die Teile des Systemdesigns veranschaulichen:

### MVP-Software-Design

### MVP-Design-Diagramm

### Datenfluss (MVP)


## OTOBO-Spezifika

Die Anwendung läuft als Docker Compose-Dienst, idealerweise im selben Netzwerk wie der OTOBO-Webserver.

Für die OTOBO-Integration ist folgendes Setup erforderlich:

*   **OTOBO Webservices:** Konfigurieren Sie die notwendigen Webservices in OTOBO.
*   **Dedizierter ATC-Benutzer:** Erstellen Sie ein spezielles Benutzerkonto in OTOBO für ATC mit den entsprechenden Berechtigungen:
    *   Lesezugriff auf die Queue für eingehende Tickets.
    *   "Verschieben nach"-Berechtigungen für alle Queues, denen ATC Tickets zuweisen können soll.
    *   Schreib- und/oder Prioritätsaktualisierungsberechtigungen für die Queue der eingehenden Tickets.
    *   *(Hinweis: In der Regel wird zuerst die Priorität und dann die Queue aktualisiert.)*
*   **OTOBO als REST-Provider:** Stellen Sie sicher, dass OTOBO korrekt als REST-Provider eingerichtet ist.

Die URLs für die OTOBO REST API und die Kennung des Ticketsystems ("otobo") werden dann in der ATC YAML-Konfigurationsdatei angegeben.