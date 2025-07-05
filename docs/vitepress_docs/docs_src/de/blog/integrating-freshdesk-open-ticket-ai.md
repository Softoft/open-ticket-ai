---
description: Erfahren Sie, wie Sie die On-Premise-Lösung Open Ticket AI (OTAI) in Freshdesk
  integrieren, um eine leistungsstarke, automatisierte Ticket-Klassifizierung zu
  ermöglichen. Dieses Dokument beschreibt die Erstellung eines benutzerdefinierten
  Python `TicketSystemAdapter`, um die KI-Modelle von OTAI mit der Freshdesk REST
  API zu verbinden. Automatisieren Sie die Ticket-Triage, indem Sie Freshdesk-Tickets
  mit KI-vorhergesagten Kategorien und Prioritäten aktualisieren und so eine intelligente
  Klassifizierung direkt in Ihren Support-Workflow einbetten.
---
# Freshdesk-KI-Integration mit Open Ticket AI

Open Ticket AI (OTAI) ist ein lokales, on-premise **Ticket-Klassifizierungssystem** (auch als ATC Community Edition bezeichnet), das die Kategorisierung und das Routing von Support-Tickets automatisiert. Freshdesk ist eine beliebte cloudbasierte Kundensupport-Plattform mit eigenen KI-Tools, die Ticketing, Workflows und Reporting bietet. Durch das Schreiben eines benutzerdefinierten *TicketSystemAdapter* können Sie OTAI in Freshdesk integrieren und Freshdesk-Tickets automatisch über dessen REST API aktualisieren. Dies ermöglicht eine KI-gesteuerte Ticket-Triage innerhalb der Freshdesk-Umgebung. In der Pipeline von Open Ticket AI ist die letzte Stufe ein **TicketSystemAdapter**, der KI-Vorhersagen über REST-Aufrufe auf das Ticketsystem anwendet. Um OTAI für Freshdesk zu erweitern, implementieren Sie einen `FreshdeskAdapter`, der von `TicketSystemAdapter` erbt und Methoden zum Abfragen und Aktualisieren von Tickets in Freshdesk implementiert.

&#x20;*Abbildung: UML-Klassendiagramm der Open Ticket AI-Architektur. Die abstrakte `TicketSystemAdapter`-Klasse bildet die Basis für systemspezifische Adapter (z. B. einen OTOBOAdapter), die sich mit externen Ticketsystemen verbinden.* Die OTAI-Architektur ist modular aufgebaut: Eingehende Tickets durchlaufen NLP-Klassifikatoren, und ein **TicketSystemAdapter** schreibt die Ergebnisse anschließend zurück in das Ticketsystem. Die Dokumentation erklärt, dass `TicketSystemAdapter` eine abstrakte Basisklasse ist, „die alle konkreten Ticketsystem-Adapter implementieren müssen“, um mit verschiedenen Ticket-Plattformen zu interagieren. Unterklassen müssen drei zentrale `async`-Methoden implementieren: `update_ticket(ticket_id, data)`, `find_tickets(query)` und `find_first_ticket(query)`. In der Praxis würden Sie eine neue Python-`class` erstellen, z. B. `class FreshdeskAdapter(TicketSystemAdapter)`, und diese Methoden überschreiben. Zum Beispiel:

```python
import aiohttp

from open_ticket_ai.src.ce.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class FreshdeskAdapter(TicketSystemAdapter):
    async def update_ticket(self, ticket_id: str, data: dict) -> dict:
        # Construct Freshdesk API URL for updating a ticket
        base = f"https://{self.config.freshdesk_domain}.freshdesk.com"
        url = f"{base}/api/v2/tickets/{ticket_id}"
        auth = aiohttp.BasicAuth(self.config.freshdesk_api_key, password="X")
        async with aiohttp.ClientSession(auth=auth) as session:
            async with session.put(url, json=data) as resp:
                return await resp.json()

    async def find_tickets(self, query: dict) -> list[dict]:
        # Use Freshdesk List Tickets or Search API to retrieve tickets matching query
        base = f"https://{self.config.freshdesk_domain}.freshdesk.com"
        params = {k: v for k, v in query.items()}
        url = f"{base}/api/v2/tickets"
        async with aiohttp.ClientSession(
            auth=aiohttp.BasicAuth(self.config.freshdesk_api_key, password="X"),
        ) as session:
            async with session.get(url, params=params) as resp:
                data = await resp.json()
                return data.get('tickets', [])

    async def find_first_ticket(self, query: dict) -> dict:
        tickets = await self.find_tickets(query)
        return tickets[0] if tickets else None
```

Der obige Code zeigt einen einfachen **FreshdeskAdapter**. Er bezieht die Freshdesk-Domain (den Firmennamen) und den API-Schlüssel aus der OTAI-Konfiguration (`self.config`), die zur Laufzeit injiziert wird. Anschließend verwendet er `aiohttp` von Python für asynchrone HTTP-Aufrufe. Die `update_ticket`-Methode sendet eine PUT-Anfrage an `https://<domain>.freshdesk.com/api/v2/tickets/<id>` mit dem JSON-Payload der zu ändernden Felder. Die `find_tickets`-Methode verwendet GET auf `/api/v2/tickets` mit Query-Parametern (alternativ könnten Sie `/api/v2/search/tickets` für komplexere Suchen aufrufen). Die Freshdesk API erfordert Basic Auth: Ihr API-Schlüssel (aus Ihrem Freshdesk-Profil) wird als Benutzername und ein beliebiges Passwort (oft nur „X“) als Passwort verwendet.

**Wichtige Schritte zur Integration von Freshdesk:**

* *API-Zugriff konfigurieren:* Melden Sie sich bei Freshdesk an und holen Sie sich Ihren **API-Schlüssel** aus dem Profil (dieser Schlüssel wird zur Authentifizierung von API-Anfragen verwendet). Notieren Sie sich auch Ihre Freshdesk-Domain (die Subdomain in Ihrer Freshdesk-URL).
* *Adapter implementieren:* Erstellen Sie eine `class` `FreshdeskAdapter`, die `TicketSystemAdapter` erweitert, und implementieren Sie `update_ticket`, `find_tickets` und `find_first_ticket`. Verwenden Sie in diesen Methoden die REST-API-Endpunkte von Freshdesk (z. B. `GET /api/v2/tickets` und `PUT /api/v2/tickets/{id}`).
* *OTAI konfigurieren:* Aktualisieren Sie die `config.yml` von OTAI, um den `FreshdeskAdapter` und seine Einstellungen (wie `freshdesk_domain` und `freshdesk_api_key`) aufzunehmen. Dank des Dependency-Injection-Setups von OTAI wird der neue Adapter zur Laufzeit geladen.
* *Klassifizierung ausführen:* Starten Sie Open Ticket AI (z. B. über `python -m open_ticket_ai.src.ce.main start`). Sobald neue Tickets abgerufen werden, klassifiziert die Pipeline diese und ruft dann Ihre `FreshdeskAdapter.update_ticket(...)`-Methode auf, um die vorhergesagte Warteschlange oder Priorität zurück in Freshdesk zu schreiben.

Mit diesem benutzerdefinierten Adapter durchlaufen Freshdesk-Tickets die OTAI-Pipeline genau wie bei jedem anderen Ticketsystem. Sobald OTAI eine Warteschlangen-ID oder Priorität zuweist, überträgt der `update_ticket`-Aufruf diese Information über die API zurück an Freshdesk. Dies ermöglicht es Freshdesk-Benutzern, die KI-Modelle von OTAI für die *automatisierte Ticket-Klassifizierung* zu nutzen, während sie weiterhin innerhalb der Freshdesk-Plattform arbeiten. Die flexible REST API von Freshdesk (die das Suchen, Auflisten, Erstellen und Aktualisieren von Tickets unterstützt) macht diese Integration unkompliziert. Indem Entwickler dem OTAI-Adapter-Muster und den Freshdesk-API-Konventionen folgen, können sie eine KI-gesteuerte Ticket-Triage nahtlos in Freshdesk einbetten, ohne auf proprietäre Cloud-KI angewiesen zu sein – und dabei auf Wunsch alle Daten lokal halten.

**Referenzen:** Die Dokumentation von Open Ticket AI erläutert die Adapter-Architektur und die `TicketSystemAdapter`-Schnittstelle. Die OTAI-Architekturübersicht zeigt den Adapter-Schritt in der Pipeline. Der API-Leitfaden und die Entwickler-Blogs von Freshdesk dokumentieren, wie man sich authentifiziert (mit einem API-Schlüssel) und Ticket-Endpunkte aufruft. Zusammen skizzieren diese Quellen die Schritte zum Erstellen einer benutzerdefinierten Freshdesk-Integration.