---
title: Technische Übersicht (MVP)
description: Ein technischer Blick auf das Minimal Viable Product (MVP) des Automated Ticket Classification (ATC)-Systems.
---

# Technische Übersicht (MVP)

Dieses Dokument beschreibt die zentralen technischen Aspekte des Minimal Viable Product (MVP) für das Automated Ticket Classification (ATC)-System.

## MVP-Funktionen

Der MVP-Fokus liegt auf den grundlegenden Fähigkeiten:

*   **Queue-Klassifizierung:** Automatische Zuweisung von Tickets an das richtige Team oder die richtige Abteilung.
*   **Prioritätsklassifizierung:** Automatische Bestimmung der Dringlichkeit eines Tickets.

Nutzer können eigene Hugging Face-Modelle verwenden oder die Standard-ATC-Modelle nutzen. Das Standard-Queue-Modell kann zwischen 42 verschiedenen Klassen unterscheiden, das Standard-Prioritätsmodell zwischen 5 Prioritätsstufen.

Diese vorhergesagten Queues und Prioritäten können auf die spezifischen Queues und Prioritäten Ihrer Organisation gemappt werden. Konfigurationsoptionen ermöglichen zudem die Definition von:
*   Der Queue für eingehende Tickets.
*   Der Queue für Tickets, die nicht sicher klassifiziert werden konnten.
*   Dem Konfidenzschwellenwert für das Queue-Modell.

## Architekturimplementierung

Der Kern der MVP-Architektur ist einfach gehalten:

*   **`QueueClassifier` und `PriorityClassifier`:** Diese Komponenten laden die spezifizierten Hugging Face-Modelle und führen sie aus, um Queue und Priorität vorherzusagen.
*   **Mapping auf lokale Queues/Prioritäten:** Die Vorhersagen der Modelle werden auf die Queues und Prioritäten Ihres lokalen Systems gemappt. Dieses Mapping wird als Dictionary in der Konfigurationsdatei definiert. Ein Wildcard-Zeichen (`*`) kann verwendet werden, um beliebige Queues abzugleichen. Es ist gängige Praxis, eine "Sonstiges"- oder "Junk"-Queue zu haben, in die Wildcard-Matches weitergeleitet werden. Dieselbe Wildcard-Logik gilt für Prioritäten, wird jedoch aufgrund der typischen 5-stufigen Prioritätsskala seltener benötigt.
*   **`TicketClassifier`:** Diese Komponente orchestriert den Prozess, indem sie sowohl den `QueueClassifier` als auch den `PriorityClassifier` gleichzeitig aufruft und deren kombinierte Ergebnisse zurückgibt.
*   **`TicketProcessor`:** Diese Komponente ist für den gesamten Workflow verantwortlich. Sie:
    1.  Holt das nächste Ticket aus dem integrierten Ticketsystem (über den `TicketSystemAdapter`).
    2.  Ruft den `TicketClassifier` auf, um Vorhersagen zu erhalten.
    3.  Ruft die `updateTicket`-Methode des injizierten `TicketSystemAdapter` auf, um die Klassifizierungsergebnisse auf das Ticket im externen System anzuwenden.
    Der `TicketProcessor` läuft in einer kontinuierlichen Schleife und prüft in einem konfigurierbaren Intervall (standardmäßig 10 Sekunden) auf neue Tickets.

Nachfolgend finden Sie Diagramme, die Teile des Systemdesigns veranschaulichen:

### MVP-Softwaredesign
![MVP-Softwaredesign](/images/mvp-software-design.png)

### MVP-Design-Diagramm
![MVP-Design](/images/mvp-design.png)

### Datenabfluss im MVP
![Keine Datensammlung im MVP](/images/mv-no-data-collection.png)

## OTOBO-spezifische Details

Die Anwendung läuft als Docker Compose-Service, idealerweise im selben Netzwerk wie der OTOBO-Webserver.

Für die OTOBO-Integration ist folgende Einrichtung erforderlich:

*   **OTOBO-Webservices:** Konfiguration der notwendigen Webservices in OTOBO.
*   **Dedizierter ATC-Benutzer:** Einrichten eines speziellen Benutzerkontos in OTOBO für ATC mit entsprechenden Berechtigungen:
    *   Lesezugriff auf die Queue für eingehende Tickets.
    *   "Move into"-Berechtigungen für alle Queues, denen ATC Tickets zuweisen können soll.
    *   Schreib- und/oder Prioritätsaktualisierungsberechtigungen für die Eingangs-Queue.
    *   *(Hinweis: Die Priorität wird typischerweise zuerst aktualisiert, dann die Queue.)*
*   **OTOBO als REST-Anbieter:** Sicherstellen, dass OTOBO korrekt als REST-Provider eingerichtet ist.

Die URLs für die OTOBO-REST-API und der Ticketsystem-Identifier ("otobo") werden dann in der ATC-YAML-Konfigurationsdatei angegeben.