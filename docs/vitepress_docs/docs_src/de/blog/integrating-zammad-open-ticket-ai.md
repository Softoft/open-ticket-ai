---
description: Erfahren Sie, wie Sie OpenTicketAI mit Zammad für eine on-premise, automatisierte Ticket-Klassifizierung und -Weiterleitung integrieren. Diese Anleitung beschreibt die Erstellung eines ZammadAdapters, der die REST API nutzt, um Tickets abzurufen, sie durch eine KI-Pipeline zu leiten und deren Queue, Priorität und Notizen automatisch zu aktualisieren.
---
# Integration von OpenTicketAI mit Zammad zur automatisierten Ticket-Klassifizierung

OpenTicketAI ist ein on-premise **KI-Ticket-Klassifikator**, der die Kategorisierung, Weiterleitung und Priorisierung von Support-Tickets automatisiert. Um es mit Zammad zu integrieren, implementieren wir einen **ZammadAdapter**, der das `TicketSystemAdapter`-Interface von OpenTicketAI erweitert. Dieser Adapter verwendet die REST API von Zammad, um Tickets von Zammad *abzurufen*, sie *durch die Pipeline von OpenTicketAI zu leiten* und das Ticket (Queue, Priorität, Kommentare) basierend auf den KI-Vorhersagen zu *aktualisieren*. Die Schlüsselkomponenten sind in der Architektur dargestellt: Die **AdapterFactory** von OpenTicketAI erstellt den passenden Adapter (z. B. ZammadAdapter), um über REST mit dem Ticketsystem zu kommunizieren. Die Pipeline ruft Tickets ab, klassifiziert sie, und schließlich aktualisiert der Ticketsystem-Adapter Zammad über dessen API.

Die Architektur von OpenTicketAI verwendet eine modulare Pipeline, in der jedes Ticket von einer Reihe von Pipes verarbeitet wird. Die letzte Stufe, der *Ticket System Adapter*, wendet Aktualisierungen (Queue, Priorität, Notizen) über die REST API auf das externe System an. In der Praxis registrieren Sie Ihren `ZammadAdapter` in der Dependency-Injection-Konfiguration, sodass die **BasicTicketFetcher**-Pipe ihn zum Laden von Tickets und die **GenericTicketUpdater**-Pipe ihn zum Anwenden von Aktualisierungen verwendet.

## Überblick über die OpenTicketAI-Pipeline

OpenTicketAI läuft in einer *Pipeline*, die Ticketdaten Schritt für Schritt transformiert. Ein vereinfachter Ablauf ist:

1. **Preprocessor** – Zusammenführen/Bereinigen von `subject` und `body`.
2. **Transformer / Tokenizer** – Text für die KI vorbereiten.
3. **Queue Classifier** – Sagt die Ziel-Queue/Gruppe voraus.
4. **Priority Classifier** – Sagt die Prioritätsstufe voraus.
5. **Postprocessor** – Wendet Schwellenwerte an, wählt Aktionen aus.
6. **Ticket System Adapter** – Aktualisiert das Ticket in Zammad über die REST API.

Jede Stufe nimmt ein `PipelineContext`-Objekt (das `ticket_id` und ein `data`-Dict enthält) entgegen und reichert es an. Nachdem die Klassifikatoren ausgeführt wurden, könnte das `data` des Kontexts beispielsweise Schlüssel wie `new_queue`, `new_priority` oder einen hinzuzufügenden `article` (Kommentar) enthalten. Die **GenericTicketUpdater**-Pipe sucht dann nach einem `update_data`-Eintrag im Kontext und ruft den Adapter auf, um diese Felder auf das Ticket anzuwenden. Dieses Design macht es einfach, neue Schritte hinzuzufügen (z. B. eine Pseudonymisierungs-Pipe) oder die Aktualisierungslogik anzupassen. Der Orchestrator verwaltet diese *AttributePredictors* (Fetcher, Preparer, KI-Dienst, Modifier) basierend auf der YAML-Konfiguration.

## TicketSystemAdapter und ZammadAdapter

OpenTicketAI definiert eine abstrakte Basisklasse `TicketSystemAdapter`, die alle Integrationen erweitern müssen. Sie deklariert Kernmethoden wie:

* `async update_ticket(ticket_id: str, data: dict) -> dict | None`: **Aktualisiert** die Felder eines Tickets (z. B. Queue, Priorität, Notiz hinzufügen). Muss Teilaktualisierungen verarbeiten und das aktualisierte Ticket-Objekt zurückgeben.
* `async find_tickets(query: dict) -> list[dict]`: **Sucht** nach Tickets, die einer Abfrage entsprechen. Das Abfrageformat ist adapterspezifisch, aber diese Methode sollte eine Liste passender Tickets zurückgeben.
* `async find_first_ticket(query: dict) -> dict | None`: Bequemlichkeitsmethode, um nur den ersten Treffer zurückzugeben.

Ein **ZammadAdapter** wird diese Klasse als Unterklasse verwenden und diese Methoden mithilfe der Zammad-API implementieren. Er wird typischerweise Konfigurationsdaten (Basis-URL, Anmeldeinformationen) enthalten, die über eine `SystemConfig` injiziert werden. Zum Beispiel:

```python
from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter
import httpx

class ZammadAdapter(TicketSystemAdapter):
    def __init__(self, config):
        super().__init__(config)
        # Assume config.zammad contains URL and auth info
        self.base_url = config.zammad.base_url.rstrip('/')
        self.auth = (config.zammad.user, config.zammad.password)

    async def find_tickets(self, query: dict) -> list[dict]:
        # Use Zammad search API (e.g. full-text search or filters).
        async with httpx.AsyncClient(auth=self.auth) as client:
            params = {"query": query.get("search", "")}
            res = await client.get(f"{self.base_url}/api/v1/tickets/search", params=params)
            res.raise_for_status()
            return res.json()  # list of matching tickets (each as dict)

    async def find_first_ticket(self, query: dict) -> dict | None:
        tickets = await self.find_tickets(query)
        return tickets[0] if tickets else None

    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        # Send PUT to update the ticket. Data can include 'group', 'priority', etc.
        url = f"{self.base_url}/api/v1/tickets/{ticket_id}"
        async with httpx.AsyncClient(auth=self.auth) as client:
            res = await client.put(url, json=data)
            if res.status_code == 200:
                return res.json()  # updated ticket object
            return None
```

*Anmerkung:* Die Basisklasse erfordert diese Methoden. In diesem Beispiel verwenden wir `httpx.AsyncClient` (da die Methoden `async` sind), aber man könnte in einem synchronen Kontext ähnlich `requests` verwenden. Zum Beispiel könnte das Abrufen aller Tickets so einfach sein wie `requests.get(f"{base_url}/api/v1/tickets", auth=(user, pwd))`.

### Abrufen von Tickets aus Zammad

Die REST API von Zammad bietet Endpunkte zum Auflisten und Suchen von Tickets. Eine einfache Möglichkeit, aktuelle oder passende Tickets abzurufen, ist über:

* **Alle auflisten (paginiert)**: `GET /api/v1/tickets` gibt ein Array von Ticket-Objekten zurück.
* **Suchen**: `GET /api/v1/tickets/search?query=...` unterstützt Volltext- oder Feldabfragen und gibt passende Tickets im JSON-Format zurück (und `expand=true` kann zugehörige Felder auflösen).

Ihre `find_tickets`-Implementierung kann diese verwenden. Zum Beispiel, um nach Status oder Betreff zu filtern:

```python
async with httpx.AsyncClient(auth=self.auth) as client:
    res = await client.get(f"{base_url}/api/v1/tickets/search", params={"query": "state:open OR state:new"})
    res.raise_for_status()
    tickets = res.json()  # a list of dicts
```

Anschließend verpacken oder geben Sie diese in dem von OpenTicketAI erwarteten Format zurück (eine Liste von Ticket-Dicts). Die `BasicTicketFetcher`-Pipe ruft dies mit der Ticket-ID aus dem `PipelineContext` auf, um ein Ticket vor der Verarbeitung zu laden.

### Aktualisieren von Zammad-Tickets

Nach der Klassifizierung aktualisieren wir Zammad über seine **Update Ticket** API. Zammad unterstützt das Ändern von Feldern wie Gruppe (Queue) und Priorität und sogar das Hinzufügen einer internen Notiz oder eines Artikels in einem einzigen Aufruf. Zum Beispiel setzt die folgende Payload (gesendet über `PUT /api/v1/tickets/{id}`) eine neue Gruppe und Priorität und fügt einen internen Artikel hinzu:

```json
{
  "group": "Sales",
  "state": "open",
  "priority": "3 high",
  "article": {
    "subject": "AI Insight",
    "body": "Sentiment analysis: negative tone detected.",
    "internal": true
  }
}
```

Dies würde das Ticket der Gruppe „Sales“ neu zuweisen, es auf hohe Priorität setzen und eine neue Notiz (interner Kommentar) mit KI-Erkenntnissen anhängen. Im Code könnte unser `update_ticket` Folgendes tun:

```python
await client.put(f"{base_url}/api/v1/tickets/{ticket_id}", json={
    "group": new_queue,
    "priority": f"{priority_level} {priority_label}",
    "article": {
        "subject": "Auto-classified Ticket",
        "body": f"Queue={new_queue}, Priority={priority_label}",
        "internal": True
    }
})
```

Die Antwort ist das vollständige aktualisierte Ticket-JSON bei Status 200. Wenn Sie nur einen Kommentar oder eine Notiz posten müssen, fügen Sie den `article`-Block wie oben gezeigt ein. Alternativ können für kleinere Aktualisierungen (wie nur das Setzen einer Notiz) das „note“-Feld des Tickets oder ein separater Artikel-Endpunkt verwendet werden, aber der gebündelte `article` im PUT ist praktisch.

## Pipeline-Integration in OpenTicketAI

Um dies in die Pipeline von OpenTicketAI einzubinden, fügen Sie **Pipes** in `config.yml` hinzu. Zum Beispiel:

* **BasicTicketFetcher**: konfiguriert mit `ticket_system: ZammadAdapter`. Er ruft `find_tickets`/`find_first_ticket` auf und füllt `context.data` mit den Ticket-Feldern.
* **Preparer**: z. B. `SubjectBodyPreparer`, um Betreff- und Nachrichtentext zu kombinieren.
* **AI Inference Services**: Ihre benutzerdefinierten Queue-/Prioritäts-Klassifikatoren (z. B. ein HuggingFace-Modell).
* **GenericTicketUpdater**: konfiguriert mit `ticket_system: ZammadAdapter`. Er sucht nach der Inferenz nach `context.data["update_data"]` und ruft `update_ticket` auf.

Zum Beispiel könnte eine benutzerdefinierte Pipe Folgendes tun:

```python
class QueuePriorityPredictor(Pipe):
    def process(self, context: PipelineContext) -> PipelineContext:
        subject = context.data.get("subject", "")
        body = context.data.get("body", "")
        queue_pred = my_queue_model.predict(subject + body)
        prio_pred = my_prio_model.predict(subject + body)
        # Prepare update data for Zammad
        context.data['update_data'] = {
            "group": queue_pred.group_name,
            "priority": f"{prio_pred.score} {prio_pred.label}",
            "article": {
                "subject": "AI Classification",
                "body": f"Assigned to {queue_pred.group_name}, Priority={prio_pred.label}",
                "internal": True
            }
        }
        return context
```

Dies richtet die `update_data` ein, die der GenericTicketUpdater verwenden wird.

Schließlich stellt die **AdapterFactory** (konfiguriert über DI) sicher, dass `ticket_system: Zammad` eine Instanz Ihrer `ZammadAdapter`-Klasse erstellt und die Basis-URL sowie die Authentifizierungsdaten aus `config.yml` injiziert. Die **GenericTicketUpdater**-Pipe ruft dann `await adapter.update_ticket(id, update_data)` auf und wendet Ihre KI-gesteuerten Änderungen an.

## Erweiterungen: Klassifizierung, Pseudonymisierung und Notizen

Über die grundlegende Queue-/Prioritätszuweisung hinaus bietet OpenTicketAI Funktionen, um die Zammad-Integration zu erweitern:

* **Queue- & Prioritätsklassifizierung:** Sie können benutzerdefinierte Modelle für spezifische Zammad-Queues oder Prioritätsschemata trainieren. Die vorhergesagten Werte werden auf die Gruppen und Prioritäten von Zammad abgebildet (zum Beispiel verwendet die Prioritäts-API das Format `"priority": "2 normal"`). Durch Anpassen der Schwellenwerte im **Postprocessor** können Sie auch Vorhersagen mit geringer Konfidenz automatisch verwerfen oder Tickets eskalieren.

* **Pseudonymisierungs-Konnektoren:** Um die Privatsphäre der Benutzer zu schützen, können Sie vor der Inferenz eine benutzerdefinierte *Pipeline-Pipe* einfügen, die sensible Daten (z. B. Namen, E-Mails) im Tickettext **pseudonymisiert** oder maskiert. Dies könnte Regex oder externe Dienste verwenden, um personenbezogene Daten (PII) durch Token zu ersetzen. Der maskierte Text wird dann klassifiziert und das ursprüngliche Ticket aktualisiert, wodurch sichergestellt wird, dass keine sensiblen Inhalte Ihr System verlassen.

* **Erstellung von Notizen/Artikeln:** Sie können die Artikel-API von Zammad nutzen, um KI-Erkenntnisse oder Stimmungen zu protokollieren. Wie oben gezeigt, fügen Sie einen `article` in die Update-Payload ein, um Kommentare hinzuzufügen. Alternativ könnten Sie eine separate **Pipe zur Notizerstellung** konfigurieren, die unabhängig von der Aktualisierung von Queue/Priorität immer eine Ticketnotiz mit den Konfidenzwerten des Modells oder einer Stimmungsanalyse anhängt. Diese Notizen helfen Agenten zu verstehen, *warum* eine Entscheidung getroffen wurde.

Jede Erweiterung fügt sich nahtlos in die Pipeline ein und wird automatisch vom GenericTicketUpdater über den Adapter angewendet. Nachdem Sie beispielsweise eine Pipe zur Stimmungsanalyse ausgeführt haben, könnten Sie Folgendes tun:

```python
context.data['update_data'] = {
    "article": {
        "subject": "Sentiment Score",
        "body": f"Sentiment polarity: {sentiment_score}",
        "internal": True,
    },
}
```

Dann wird der Adapter dies als Artikel an Zammad POSTen.

## Vorteile für die Zammad-Ticketautomatisierung

Mit dieser Integration erhält Zammad eine on-premise, KI-gestützte Automatisierung. Eingehende Tickets können automatisch der richtigen Queue zugewiesen und mit einer vorläufigen Priorität versehen werden, wodurch Support-Teams sich auf dringende Probleme konzentrieren können. Da OpenTicketAI lokal ausgeführt wird, bleiben sensible Ticketdaten im eigenen Haus (wichtig für die Compliance). Diese **Zammad-KI-Integration** verwandelt die manuelle Triage in einen optimierten Prozess: Sie behalten die volle Kontrolle und Anpassungsmöglichkeiten (über Konfiguration und benutzerdefinierte Modelle), während Sie die Pipeline von OpenTicketAI nutzen.

Zusammenfassend lässt sich sagen, dass die Implementierung eines **ZammadAdapters** das Erstellen einer Unterklasse von `TicketSystemAdapter` und deren Einbindung in die Pipeline von OpenTicketAI umfasst. Der Adapter verwendet die API von Zammad für CRUD-Operationen mit Tickets (z. B. `GET /tickets` und `PUT /tickets/{id}`). Einmal konfiguriert, wird OpenTicketAI kontinuierlich Tickets abrufen, sie durch Ihren KI-Modell-Stack leiten und Zammad mit der vorhergesagten Queue, Priorität und beliebigen Notizen aktualisieren. Diese **Ticketsystem-KI**-Integration erweitert Zammad um automatisierte Klassifizierung und Weiterleitung und verwirklicht so die Vision eines on-premise KI-Ticket-Klassifikators für Unternehmens-Support-Teams.

**Quellen:** Zammad REST API-Doku; OpenTicketAI Entwickler-Doku.