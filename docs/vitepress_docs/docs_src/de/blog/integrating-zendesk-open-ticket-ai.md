---
description: Erfahren Sie, wie Sie Zendesk mit Open Ticket AI für die automatisierte Ticket-Klassifizierung integrieren. Diese Anleitung zeigt Entwicklern, wie sie einen benutzerdefinierten Python-Adapter erstellen, um Tickets mithilfe der Zendesk REST API automatisch nach Priorität und Tags zu sortieren und so die Effizienz des Supports zu verbessern.
---
# Integration von Zendesk mit Open Ticket AI zur automatisierten Ticket-Klassifizierung

In modernen Support-Workflows kann KI **Zendesk**-Agenten bei der automatischen Triage von Tickets unterstützen. [Open Ticket AI](https://ticket-classification.softoft.de) (OTAI) ist ein On-Premises-Tool, das eingehende Tickets analysiert und deren Priorität, Warteschlange/Kategorie, Tags und mehr über eine REST API vorhersagt. Durch die Anbindung von OTAI an Zendesk können Support-Teams Prioritäten oder Tags automatisch auf Basis von KI zuweisen, was die Reaktionszeit und Konsistenz verbessert. Dieser Artikel zeigt Entwicklern, wie sie einen benutzerdefinierten **ZendeskAdapter** für OTAI erstellen, indem sie den bestehenden `TicketSystemAdapter` erweitern und die Zendesk REST API aufrufen.

## OTAI-Architektur und TicketSystemAdapter

Open Ticket AI verwendet eine **modulare Pipeline**-Architektur. Jedes eingehende Ticket wird vorverarbeitet, durch Warteschlangen- und Prioritätsklassifikatoren geleitet und schließlich über einen Adapter an das Ticketsystem zurückgesendet. Die Schlüsselkomponente hierbei ist der **TicketSystemAdapter** (eine abstrakte Basisklasse), der definiert, wie Tickets in einem externen System aktualisiert oder abgefragt werden. Eingebaute Adapter (z. B. für OTOBO) erben von dieser Basisklasse. Für Zendesk erstellen wir eine neue Unterklasse.

&#x20;*Abbildung: Architektur von Open Ticket AI (Auszug aus dem UML-Klassendiagramm). Die Pipeline-Stufen (Vorverarbeitung, Klassifizierung usw.) münden in einem **TicketSystemAdapter**, der Aktualisierungen über REST an das externe Ticketsystem sendet. Die Erweiterung von OTAI um Zendesk beinhaltet das Erstellen einer Unterklasse (subclassing) dieses Adapters, damit KI-Ergebnisse (Priorität, Tags usw.) in Zendesk-Tickets geschrieben werden.*

In der Praxis wird OTAI über YAML konfiguriert und nutzt **Dependency Injection**. Alle Komponenten (Fetcher, Klassifikatoren, Modifikatoren usw.) werden in der `config.yml` definiert und beim Start zusammengesetzt. Die Dokumentation merkt an: „Benutzerdefinierte Fetcher, Preparer, KI-Dienste oder Modifikatoren können als Python-Klassen implementiert und über die Konfiguration registriert werden. Dank Dependency Injection können neue Komponenten einfach integriert werden.“. Mit anderen Worten, das Hinzufügen eines `ZendeskAdapter` ist unkompliziert: Wir implementieren ihn als Python-`class` und deklarieren ihn in der Konfiguration.

## Schritte zum Hinzufügen eines Zendesk-Adapters

Folgen Sie diesen Schritten, um Zendesk in OTAI zu integrieren:

1. **`TicketSystemAdapter` als Unterklasse verwenden**: Erstellen Sie eine neue Adapter-Klasse (z. B. `ZendeskAdapter`), die den abstrakten `TicketSystemAdapter` erweitert. Diese `class` implementiert, wie OTAI von Zendesk liest oder dorthin schreibt.
2. **`update_ticket` implementieren**: Überschreiben Sie in `ZendeskAdapter` die Methode `async def update_ticket(self, ticket_id: str, data: dict)`. Diese Methode sollte eine HTTP-Anfrage an Zendesk senden, um die Felder des angegebenen Tickets (z. B. Priorität, Tags) zu aktualisieren. Zum Beispiel senden Sie eine `PUT`-Anfrage an `https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json` mit einem JSON-Payload, der die zu aktualisierenden Felder enthält.
3. **(Optional) Suchmethoden implementieren**: Sie können auch `find_tickets(self, query: dict)` oder `find_first_ticket(self, query: dict)` überschreiben, wenn Sie Tickets von Zendesk abrufen müssen (z. B. um neue Tickets zu erhalten). Diese Methoden sollten die GET-Endpunkte von Zendesk (wie `/api/v2/tickets.json` oder die Such-API) aufrufen und Ticketdaten als Python-Dictionaries zurückgeben.
4. **Anmeldeinformationen konfigurieren**: Fügen Sie Ihre Zendesk-Anmeldeinformationen zur OTAI-Konfiguration hinzu. Speichern Sie beispielsweise die **Subdomain**, die **Benutzer-E-Mail** und den **API-Token** in der `config.yml` oder in Umgebungsvariablen. Der Adapter kann diese aus der injizierten `SystemConfig` (die im Konstruktor übergeben wird) auslesen.
5. **Adapter registrieren**: Aktualisieren Sie die `config.yml`, sodass OTAI den `ZendeskAdapter` für die Integration des Ticketsystems verwendet. Das DI-Framework von OTAI instanziiert dann Ihre `class` mit den Konfigurationsparametern.

Diese Schritte nutzen die Erweiterbarkeit von OTAI. Die Pipeline wird in der Konfiguration definiert (für das Auslösen der Klassifizierung ist kein REST erforderlich). Durch das einfache Einbinden Ihres Adapters wird Zendesk zum Zielsystem der Pipeline.

## Beispiel: Implementierung des ZendeskAdapter

Unten sehen Sie einen Entwurf, wie der Python-Adapter aussehen könnte. Er wird mit Konfigurationswerten initialisiert und implementiert `update_ticket` unter Verwendung der `requests`-Bibliothek von Python. Der folgende Code dient zur Veranschaulichung; Sie müssen `requests` installieren (oder `httpx`/`aiohttp` für `async`-Operationen verwenden) und Fehler nach Bedarf behandeln:

```python
import requests
from open_ticket_ai.src.ticket_system_integration.ticket_system_adapter import TicketSystemAdapter


class ZendeskAdapter(TicketSystemAdapter):
    def __init__(self, config):
        super().__init__(config)
        # Zendesk-Einstellungen aus der Konfiguration lesen (in config.yml definiert)
        self.subdomain = config.zendesk_subdomain
        self.user_email = config.zendesk_user_email
        self.api_token = config.zendesk_api_token

    async def update_ticket(self, ticket_id: str, data: dict) -> dict | None:
        """
        Aktualisiert ein Zendesk-Ticket mit den bereitgestellten Daten (dict von Feldern).
        Verwendet die Zendesk Tickets API, um Änderungen anzuwenden.
        """
        url = f"https://{self.subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json"
        # Zendesk erwartet ein JSON-Objekt mit "ticket": { ...Felder... }
        payload = {"ticket": data}
        auth = (f"{self.user_email}/token", self.api_token)
        response = requests.put(url, json=payload, auth=auth)
        if response.status_code == 200:
            return response.json().get("ticket")
        else:
            # Fehler protokollieren oder behandeln (z. B. ungültige ID oder Authentifizierung)
            return None

    async def find_tickets(self, query: dict) -> list[dict]:
        """
        (Optional) Nach Tickets suchen. Die Abfrage könnte Filterkriterien enthalten.
        Dieses Beispiel verwendet den Such-Endpunkt von Zendesk.
        """
        query_str = query.get("query", "")  # z. B. "status<solved"
        url = f"https://{self.subdomain}.zendesk.com/api/v2/search.json?query={query_str}"
        auth = (f"{self.user_email}/token", self.api_token)
        response = requests.get(url, auth=auth)
        if response.status_code == 200:
            return response.json().get("results", [])
        return []
```

Der Konstruktor dieses `ZendeskAdapter` holt die Einstellungen aus der injizierten `config`. Die `update_ticket`-Methode erstellt die URL nach dem Standardmuster von Zendesk und sendet eine PUT-Anfrage. In diesem Beispiel authentifizieren wir uns mit HTTP Basic Auth unter Verwendung der Zendesk-E-Mail und des API-Tokens (konventionsgemäß lautet der Benutzername `user_email/token`). Der Payload umschließt die Ticketdaten mit dem Schlüssel `"ticket"`, wie es die API von Zendesk erwartet. Nach einer erfolgreichen Aktualisierung gibt sie das aktualisierte Ticket-JSON zurück.

Sie würden `config.zendesk_subdomain`, `config.zendesk_user_email` und `config.zendesk_api_token` in der `config.yml` definieren. Zum Beispiel:

```yaml
ticket_system_integration:
    adapter: open_ticket_ai.src.ce.ticket_system_integration.zendesk_adapter.ZendeskAdapter
    zendesk_subdomain: "mycompany"
    zendesk_user_email: "agent@mycompany.com"
    zendesk_api_token: "ABCD1234TOKEN"
```

Dies weist OTAI an, den `ZendeskAdapter` zu verwenden. Die Dependency Injection von OTAI wird dann Ihren Adapter mit diesen Werten erstellen.

## Aufruf der Zendesk REST API

Der Schlüssel zum Adapter liegt darin, HTTP-Anfragen an die API-Endpunkte von Zendesk zu senden. Wie oben gezeigt, ruft der Adapter von OTAI URLs wie `https://{subdomain}.zendesk.com/api/v2/tickets/{ticket_id}.json` auf. Laut der Zendesk-Dokumentation erfordert die Aktualisierung eines Tickets eine PUT-Anfrage an diese URL mit einem JSON-Body (zum Beispiel `{"ticket": {"priority": "high", "tags": ["urgent"]}}`, wenn Sie Priorität und Tags setzen möchten). Im obigen Beispielskript erledigt `requests.put(url, json=payload, auth=auth)` dies.

Zur Vollständigkeit können Sie auch die Ticketerstellung (`requests.post(...)`) oder andere API-Aufrufe implementieren. Für die Klassifizierung ist jedoch in der Regel nur die **Aktualisierung bestehender Tickets** erforderlich (um die von der KI vorhergesagten Felder zurückzuschreiben). Stellen Sie sicher, dass der Zendesk API-Token über die erforderlichen Berechtigungen verfügt und dass Sie den „Token-Zugriff“ in der Zendesk-Administration aktiviert haben.

Wenn Sie auch Tickets von Zendesk abrufen möchten (zum Beispiel, um neu erstellte Tickets zur Verarbeitung zu finden), verwenden Sie die Listen- oder Such-APIs von Zendesk. Sie könnten beispielsweise eine GET-Anfrage an `/api/v2/tickets.json` senden, um durch Tickets zu blättern, oder `/api/v2/search.json?query=type:ticket status:new` verwenden, um alle neuen Tickets zu finden. Geben Sie das JSON als eine Liste von Ticket-Dicts von `find_tickets()` an OTAI zurück.

## Pipeline und Verwendung

Wenn der `ZendeskAdapter` eingerichtet ist, wird er beim Ausführen von OTAI nahtlos in die Pipeline integriert. Nachdem Sie beispielsweise Ihre KI-Modelle (Warteschlangen- und Prioritätsprädiktoren) eingerichtet haben, wird durch den Start des OTAI-Schedulers (z. B. `python -m open_ticket_ai.src.ce.main start`) die Pipeline ausgelöst. OTAI wird Ihren Adapter als letzten „Modifier“-Schritt verwenden: Nachdem die KI Attribute für jedes Ticket abgeleitet hat, ruft sie `ZendeskAdapter.update_ticket` auf, um diese Attribute wieder in Zendesk anzuwenden. Der gesamte Prozess bleibt für OTAI transparent – es weiß nur, dass es `update_ticket` auf einer Adapter-Klasse aufruft.

Da die Komponenten von OTAI in YAML definiert sind, können Sie konfigurieren, wie oft Tickets abgerufen oder geprüft werden und wie Aktualisierungen angewendet werden. Die Entwicklerdokumentation betont, dass alle Komponenten über die Konfiguration und DI (Dependency Injection) einsteckbar sind. Sobald Ihr Adapter also implementiert und in der `config.yml` eingebunden ist, sind keine weiteren Code-Änderungen erforderlich, um Zendesk in den Ticket-Fluss zu integrieren.