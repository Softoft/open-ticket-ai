---
title: Technische Übersicht (MVP)
description: Ein technischer Blick auf das Minimum Viable Product des ATC-Systems.
---

# Technische Übersicht (MVP)

Dieses Dokument beschreibt die zentralen technischen Aspekte des Minimum Viable Product (MVP) für das Automated Ticket Classification (ATC)-System.

## MVP-Funktionen

Der MVP konzentriert sich auf folgende Kernfunktionen:

*   **Warteschlangen-Klassifizierung:** Automatische Zuweisung von Tickets zum richtigen Team oder Bereich.
*   **Prioritäts-Klassifizierung:** Automatische Bestimmung der Dringlichkeit eines Tickets.

Benutzer können eigene Hugging Face-Modelle nutzen oder die Standard-ATC-Modelle verwenden. Das Standard-Warteschlangenmodell unterscheidet 42 verschiedene Klassen, das Standard-Prioritätsmodell erkennt 5 Prioritätsstufen.

Die vorhergesagten Warteschlangen und Prioritäten können auf organisationsspezifische Warteschlangen und Prioritäten abgebildet werden. Konfigurationsoptionen ermöglichen die Definition von:
*   Der Standard-Warteschlange für eingehende Tickets
*   Der Warteschlange für nicht sicher klassifizierbare Tickets
*   Dem Konfidenzschwellenwert für das Warteschlangenmodell

## Architekturimplementierung

Der Kern der MVP-Architektur ist einfach gehalten:

*   **`QueueClassifier` und `PriorityClassifier`:** Diese Komponenten laden die spezifizierten Hugging Face-Modelle und führen sie zur Vorhersage von Warteschlange und Priorität aus.
*   **Abbildung auf lokale Warteschlangen/Prioritäten:** Die Vorhersagen werden auf organisationsinterne Warteschlangen und Prioritäten gemappt. Diese Zuordnung wird im Konfigurationsfile als Dictionary definiert. Ein Wildcard-Zeichen (`*`) kann beliebige Warteschlangen abdecken - üblicherweise wird eine "Sonstiges"- oder "Junk"-Warteschlange für Wildcard-Matches verwendet. Dieselbe Logik gilt für Prioritäten, wird aber aufgrund der typischen 5-Stufen-Skala seltener benötigt.
*   **`TicketClassifier`:** Orchestriert den Prozess durch gleichzeitigen Aufruf von `QueueClassifier` und `PriorityClassifier` und gibt kombinierte Ergebnisse zurück.
*   **`TicketProcessor`:** Steuert den Gesamtworkflow durch:
    1.  Abruf des nächsten Tickets aus dem integrierten Ticketsystem (via `TicketSystemAdapter`)
    2.  Aufruf des `TicketClassifier` für Vorhersagen
    3.  Anwendung der Klassifizierungsergebnisse auf das Ticket im externen System via `updateTicket`-Methode des `TicketSystemAdapter`
    Der `TicketProcessor` arbeitet in einer Endlosschleife mit konfigurierbarem Polling-Intervall (Standard: 10 Sekunden).

Folgende Diagramme veranschaulichen Teile des Systemdesigns:

### MVP-Softwaredesign
![MVP Software Design](/images/mvp-software-design.png)

### MVP-Design-Diagramm
![MVP Design](/images/mvp-design.png)

### Datenfluss im MVP
![Keine Datenerfassung im MVP](/images/mv-no-data-collection.png)

## OTOBO-spezifische Details

Die Anwendung läuft als Docker-Compose-Service, idealerweise im selben Netzwerk wie der OTOBO-Webserver.

Für die OTOBO-Integration ist folgende Konfiguration erforderlich:

*   **OTOBO-Webservices:** Einrichtung der erforderlichen Webservices in OTOBO
*   **Dedizierter ATC-Benutzer:** Anlegen eines speziellen OTOBO-Benutzerkontos für ATC mit Berechtigungen für:
    *   Lesezugriff auf die Eingangswarteschlange
    *   "Verschieben in"-Berechtigung für alle Zielwarteschlangen
    *   Schreib- und Prioritätsaktualisierungsberechtigungen für die Eingangswarteschlange
    *   *(Hinweis: Priorität wird typischerweise vor der Warteschlange aktualisiert)*
*   **OTOBO als REST-Provider:** Korrekte Konfiguration von OTOBO als REST-Dienst

Die URLs für die OTOBO-REST-API und der Ticketsystem-Identifier ("otobo") werden in der ATC-YAML-Konfigurationsdatei spezifiziert.