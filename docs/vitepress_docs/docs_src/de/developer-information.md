---
description: Entwicklerleitfaden für die ATC Community Edition, ein On-Premise-Tool zur Ticket-Klassifizierung.
    Lernen Sie, das System mit YAML zu konfigurieren, es über die CLI auszuführen und seine
    Architektur mit benutzerdefinierten Python-Komponenten, pipe_ids und Ticketsystem-Adaptern zu erweitern.
title: Entwicklerinformationen
---

# Entwicklerinformationen für die ATC Community Edition

## Übersicht

Die ATC Community Edition ist eine On-Premise-Lösung zur automatisierten Klassifizierung von Support-Tickets. Die aktuelle MVP-Version wird über eine YAML-Konfigurationsdatei gesteuert und per CLI gestartet. Es gibt keine REST API zum Hochladen von Trainingsdaten oder zum Anstoßen eines Trainingslaufs.

## Softwarearchitektur

Die Anwendung besteht im Wesentlichen aus den folgenden Paketen:

*   **core** – Basisklassen, Konfigurationsmodelle und Hilfsfunktionen.
*   **run** – enthält die Pipeline für die Ticket-Klassifizierung.
*   **ticket\_system\_integration** – Adapter für verschiedene Ticketsysteme.
*   **main.py** – CLI-Einstiegspunkt, der den Scheduler und den Orchestrator startet.

Der Orchestrator führt konfigurierbare `AttributePredictors` aus, die sich aus `DataFetcher`, `DataPreparer`, `AIInferenceService` und `Modifier` zusammensetzen. Alle Komponenten werden in der `config.yml` definiert und beim Programmstart validiert.

Ein Beispielbefehl zum Starten der Anwendung:

```bash
python -m open_ticket_ai.src.ce.main start
```

## Training benutzerdefinierter Modelle

Ein direktes Training durch die Anwendung ist im MVP nicht vorgesehen. Vortrainierte Modelle können in der Konfiguration angegeben und verwendet werden. Wenn ein Modell angepasst oder neu erstellt werden muss, muss dies außerhalb der Anwendung geschehen.

## Erweiterung

Benutzerdefinierte Fetcher, Preparer, KI-Services oder Modifier können als Python-Klassen implementiert und über die Konfiguration registriert werden. Dank Dependency Injection können neue Komponenten einfach integriert werden.

## Wie man eine benutzerdefinierte Pipe hinzufügt

Die Verarbeitungspipeline kann mit eigenen Pipe-Klassen erweitert werden. Eine Pipe ist eine
Arbeitseinheit, die einen `PipelineContext` empfängt, diesen modifiziert und zurückgibt. Alle
Pipes erben von der `Pipe`-Basisklasse, die bereits
das `Providable`-Mixin implementiert.

1.  **Erstellen Sie ein Konfigurationsmodell** für Ihre Pipe, falls diese Parameter benötigt.
2.  **Leiten Sie von `Pipe` ab** und implementieren Sie die `process`-Methode.
3.  **Überschreiben Sie `get_provider_key()`**, wenn Sie einen benutzerdefinierten Schlüssel wünschen.

Das folgende vereinfachte Beispiel aus der `AI_README` zeigt eine Pipe zur Stimmungsanalyse:

```python
class SentimentPipeConfig(BaseModel):
    model_name: str = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"


class SentimentAnalysisPipe(Pipe, Providable):
    def __init__(self, config: SentimentPipeConfig):
        super().__init__(config)
        self.classifier = pipeline("sentiment-analysis", model=config.model_name)

    def process(self, context: PipelineContext) -> PipelineContext:
        ticket_text = context.data.get("combined_text")
        if not ticket_text:
            context.stop_pipeline()
            return context

        sentiment = self.classifier(ticket_text)[0]
        context.data["sentiment"] = sentiment["label"]
        context.data["sentiment_confidence"] = sentiment["score"]
        return context

    @classmethod
    def get_provider_key(cls) -> str:
        return "SentimentAnalysisPipe"
```

Nach der Implementierung der Klasse registrieren Sie diese in Ihrer Dependency-Injection-Registry
und referenzieren sie in der `config.yml` unter Verwendung des von
`get_provider_key()` zurückgegebenen Provider-Schlüssels.

## Wie man ein neues Ticketsystem integriert

Um ein anderes Helpdesk-System anzubinden, implementieren Sie einen neuen Adapter, der von
`TicketSystemAdapter` erbt. Der Adapter konvertiert zwischen der externen API und den
einheitlichen Modellen des Projekts.

1.  **Erstellen Sie eine Adapter-Klasse**, z.B. `FreshdeskAdapter(TicketSystemAdapter)`.
2.  **Implementieren Sie alle abstrakten Methoden**:
    *   `find_tickets`
    *   `find_first_ticket`
    *   `create_ticket`
    *   `update_ticket`
    *   `add_note`
3.  **Übersetzen Sie Daten** in die und aus den `UnifiedTicket`- und `UnifiedNote`-Modellen.
4.  **Stellen Sie ein Konfigurationsmodell** für Anmeldeinformationen oder API-Einstellungen bereit.
5.  **Registrieren Sie den Adapter** in `create_registry.py`, damit er aus der
    YAML-Konfiguration instanziiert werden kann.

Sobald der Adapter registriert ist, geben Sie ihn im `system`-Abschnitt der `config.yml` an, und
der Orchestrator wird ihn zur Kommunikation mit dem Ticketsystem verwenden.

## Zusammenfassung

Die ATC Community Edition bietet in ihrer MVP-Version einen lokal ausgeführten Workflow zur automatischen Ticket-Klassifizierung. Alle
Einstellungen werden über YAML-Dateien verwaltet; es steht keine REST API zur Verfügung. Für das Training müssen externe Prozesse oder Skripte verwendet werden.