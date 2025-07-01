---
description: Eine technische Übersicht über das Automated Ticket Classification (ATC) MVP,
  die dessen Architektur, die Verwendung von Hugging Face-Modellen zur Queue- und Prioritätsklassifizierung
  sowie spezifische Integrationsschritte für das OTOBO-Ticketsystem beschreibt.
title: Technische Übersicht (MVP)
---
# Technische Übersicht (MVP)

Dieses Dokument beschreibt die zentralen technischen Aspekte des Minimum Viable Product (MVP) für das System zur automatisierten Ticket-Klassifizierung (Automated Ticket Classification, ATC).

## MVP-Funktionen

Das MVP konzentriert sich auf die folgenden grundlegenden Fähigkeiten:

*   **Queue-Klassifizierung:** Automatisches Zuweisen von Tickets zum richtigen Team oder zur richtigen Abteilung.
*   **Prioritätsklassifizierung:** Automatisches Bestimmen der Dringlichkeit eines Tickets.

Benutzer können ihre eigenen Hugging Face-Modelle nutzen oder die Standard-ATC-Modelle verwenden. Das Standard-Queue-Modell kann zwischen 42 verschiedenen Klassen unterscheiden, und das Standard-Prioritätsmodell kann 5 Prioritätsstufen differenzieren.

Diese vorhergesagten Queues und Prioritäten können auf die spezifischen Queues und Prioritäten Ihrer Organisation abgebildet werden. Konfigurationsoptionen ermöglichen es Ihnen außerdem, Folgendes zu definieren:
*   Die Queue für eingehende Tickets.
*   Die Queue für Tickets, die nicht mit ausreichender Sicherheit klassifiziert werden konnten.
*   Den Konfidenzschwellenwert für das Queue-Modell.

## Implementierung der Architektur

Der Kern der MVP-Architektur ist einfach gehalten:

*   **`QueueClassifier` und `PriorityClassifier`:** Diese Komponenten laden die angegebenen Hugging Face-Modelle und führen sie aus, um Queue und Priorität vorherzusagen.
*   **Abbildung auf lokale Queues/Prioritäten:** Die Vorhersagen der Modelle werden dann auf die Queues und Prioritäten Ihres lokalen Systems abgebildet. Diese Zuordnung wird als Dictionary in der Konfigurationsdatei definiert. Sie können ein Wildcard-Zeichen (`*`) verwenden, um jede beliebige Queue abzugleichen. Es ist üblich, eine „Sonstiges“- oder „Junk“-Queue zu haben, in die Wildcard-Übereinstimmungen geleitet werden. Dieselbe Wildcard-Logik gilt für Prioritäten, obwohl sie bei der typischen 5-stufigen Prioritätsskala seltener benötigt wird.
*   **`TicketClassifier`:** Diese Komponente orchestriert den Prozess, indem sie sowohl den `QueueClassifier` als auch den `PriorityClassifier` gleichzeitig aufruft und deren kombinierte Ergebnisse zurückgibt.
*   **`TicketProcessor`:** Diese Komponente ist für den gesamten Arbeitsablauf verantwortlich. Sie:
    1.  Holt das nächste Ticket aus dem integrierten Ticketsystem (über den `TicketSystemAdapter`).
    2.  Ruft den `TicketClassifier` auf, um Vorhersagen zu erhalten.
    3.  Ruft die `updateTicket`-Methode des injizierten `TicketSystemAdapter` auf, um die Klassifizierungsergebnisse auf das Ticket im externen System anzuwenden.
    Der `TicketProcessor` läuft in einer Endlosschleife und fragt in einem konfigurierbaren Intervall (standardmäßig 10 Sekunden) nach neuen Tickets.

Nachfolgend finden Sie einige Diagramme, die Teile des Systemdesigns veranschaulichen:

### MVP Software-Design
![MVP Software-Design](/images/mvp-software-design.png)

### MVP Design-Diagramm
![MVP Design-Diagramm](/images/mvp-design.png)

### Datenfluss bei der Sammlung (MVP)
![Keine Datensammlung im MVP](/images/mv-no-data-collection.png)


## OTOBO-Spezifika

Die Anwendung läuft als Docker Compose-Dienst, idealerweise im selben Netzwerk wie der OTOBO-Webserver.

Für die OTOBO-Integration ist die folgende Einrichtung erforderlich:

*   **OTOBO Webservices:** Konfigurieren Sie die notwendigen Webservices in OTOBO.
*   **Dedizierter ATC-Benutzer:** Erstellen Sie ein spezielles Benutzerkonto in OTOBO für ATC mit den entsprechenden Berechtigungen:
    *   Lesezugriff auf die Queue für eingehende Tickets.
    *   „Verschieben nach“-Berechtigungen für alle Queues, denen ATC Tickets zuweisen können soll.
    *   Schreib- und/oder Prioritätsaktualisierungsberechtigungen für die Queue der eingehenden Tickets.
    *   *(Hinweis: In der Regel wird zuerst die Priorität und dann die Queue aktualisiert.)*
*   **OTOBO als REST-Provider:** Stellen Sie sicher, dass OTOBO korrekt als REST-Provider eingerichtet ist.

Die URLs für die OTOBO REST API und die Kennung des Ticketsystems („otobo“) werden dann in der ATC YAML-Konfigurationsdatei angegeben.