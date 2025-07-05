---
description: Sparen Sie Zeit und Kosten bei der Kennzeichnung von Tausenden von Tickets.
  Erfahren Sie, wie Sie GPT für die halbautomatische Zero-Shot-Vorkennzeichnung und
  Tools wie Label Studio für eine effiziente menschliche Überprüfung nutzen können.
  Enthält Python-Beispiele.
---
# 10.000 Tickets effizient labeln: Strategien für halbautomatisches Labeling

Das manuelle Labeling von Tausenden von Support-Tickets ist zeitaufwendig und teuer. Ein **halbautomatischer
Workflow** nutzt große Sprachmodelle (LLMs) wie GPT, um Tickets **vorzukennzeichnen** (mittels
Zero-Shot-/Few-Shot-Prompts) und lässt menschliche Annotatoren diese Labels anschließend **überprüfen und korrigieren**.
Dieser hybride Ansatz reduziert den Annotationsaufwand drastisch: Eine Fallstudie ergab beispielsweise,
dass von GPT generierte „Vor-Annotationen“ *„gut genug waren, um uns zu helfen, den Labeling-Prozess zu beschleunigen“*. In
der Praxis können *minimale Labels* vom Model Zeit und Kosten der Annotation reduzieren. In diesem Artikel
erklären wir, wie man eine solche Pipeline einrichtet, zeigen Python-Beispiele (mit GPT über OpenRouter oder OpenAI)
und besprechen Tools wie Label Studio für die Überprüfung.

## GPT für Zero-Shot-/Few-Shot-Vorkennzeichnung verwenden

Moderne LLMs können Text mit **null oder wenigen Beispielen** klassifizieren. Beim Zero-Shot-Labeling weist das Model
Kategorien zu, ohne explizit auf Ticket-Daten trainiert worden zu sein. Wie es in einem Tutorial heißt:
*„Zero-Shot-Lernen ermöglicht es Modellen, neue Instanzen ohne gelabelte Beispiele zu klassifizieren“*. In der
Praxis erstellen Sie einen Prompt, der GPT anweist, ein Ticket zu kategorisieren. Zum Beispiel:

```text
Ticket: "Cannot login to account."
Classify this ticket into one of {Bug, Feature Request, Question}.
```

Das Model antwortet dann mit einem Label. Beim Few-Shot-Labeling werden dem Prompt einige Beispiele hinzugefügt, um
die Genauigkeit zu verbessern. Das bedeutet, wir können initiale Labels **direkt über die API** ohne jegliches
Modelltraining generieren.

> **Tipp:** Verwenden Sie einen strukturierten Prompt oder fordern Sie eine JSON-Ausgabe an, um das Parsen zu erleichtern. Zum Beispiel:
>
> ```
> Ticket: "Password reset email bounced."
> Respond in JSON like {"category": "..."}.
> ```
>
> Dies hilft bei der Integration der Antwort in Ihre Pipeline.

## Beispiel: Python-Code für die Vorkennzeichnung

Unten sehen Sie ein Python-Beispiel, das die API von OpenAI über die `openai`-Bibliothek verwendet. Es durchläuft eine Dummy-Ticketliste, fordert GPT-4 auf, jedes Ticket zu klassifizieren, und speichert die Kategorie. (Sie können [OpenRouter](https://openrouter.ai) auf ähnliche Weise verwenden, indem Sie `base_url="https://openrouter.ai/api/v1"` setzen und den `model`-Parameter ändern.)

```python
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
tickets = [
    {"id": 1, "text": "User cannot login to account", "category": None},
    {"id": 2, "text": "Error 404 when uploading file", "category": None},
    {"id": 3, "text": "Request to add dark mode feature", "category": None},
    {"id": 4, "text": "Payment declined on checkout", "category": None},
]
categories = ["Bug", "Feature Request", "Question"]

for ticket in tickets:
    prompt = f"Ticket: \"{ticket['text']}\". Classify it as one of {categories}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0
    )
    # Extract the category from GPT's reply
    ticket["category"] = response.choices[0].message.content.strip()

print(tickets)
```

Nach der Ausführung könnte `tickets` so aussehen:

```python
[
    {'id': 1, 'text': 'User cannot login to account', 'category': 'Bug'},
    {'id': 2, 'text': 'Error 404 when uploading file', 'category': 'Bug'},
    {'id': 3, 'text': 'Request to add dark mode feature', 'category': 'Feature Request'},
    {'id': 4, 'text': 'Payment declined on checkout', 'category': 'Bug'}
]
```

Dies sind **Vor-Labels** (pre-labels), die menschliche Prüfer kontrollieren werden. Beachten Sie, wie einfach OpenRouter den Wechsel von Modellen macht: Durch Ändern von `model="openai/gpt-4"` zu einem anderen Anbieter (z. B. Claude oder einem schlankeren Model) funktioniert derselbe Code. Tatsächlich ermöglicht die einheitliche API von OpenRouter, mehrere Anbieter auszuprobieren oder Fallback-Modelle zu verwenden, wenn eines ausfällt. Zum Beispiel:

```python
from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="YOUR_OPENROUTER_API_KEY",
)
client.chat.completions.create(
    model="openai/gpt-4o",  # try GPT-4 first
    extra_body={"models": ["anthropic/claude-3.5-sonnet", "google/palm-2"]},
    messages=[{"role": "user", "content": "Ticket: 'Login page error'. Classify it."}]
)
```

Dieser Code verwendet GPT-4, falls verfügbar, und greift andernfalls auf Claude oder PaLM zurück, wie in der Dokumentation von OpenRouter gezeigt. Eine solche Flexibilität ist nützlich für Unternehmen, die eine hohe Verfügbarkeit benötigen oder Modelle vergleichen möchten.

## Integration von Vor-Labels in Labeling-Tools

Sobald GPT Labels generiert hat, ist der nächste Schritt, sie **in eine Labeling-Oberfläche** zur menschlichen Überprüfung zu importieren. Eine beliebte Open-Source-Lösung ist [Label Studio](https://labelstud.io). Label Studio unterstützt den Import von Modellvorhersagen als „Vor-Annotationen“ (pre-annotations) zusammen mit den Daten. Annotatoren sehen das vorgeschlagene Label und müssen nur Fehler korrigieren, anstatt von Grund auf neu zu labeln. Im Endeffekt wechselt das Team *„von der zeitintensiven Aufgabe des Daten-Labelings zum weitaus effizienteren Prozess der Überprüfung und Verfeinerung der vorläufigen Labels“*.

Label Studio bietet sogar ein ML-Backend: Sie können einen kleinen Server mit der `LabelStudioMLBase`-Class schreiben, der für jede Aufgabe GPT aufruft. In ihrem Tutorial zeigt Label Studio, wie man GPT-4-Aufrufe in diese Class einbettet, um Vorhersagen dynamisch zurückzugeben. Alternativ können Sie eine JSON-Datei mit Vorhersagen importieren. Das erforderliche JSON-Format hat ein `data`-Feld (der Ticket-Text) und ein `predictions`-Array (das jedes Label enthält). Zum Beispiel (vereinfacht):

```json
[
    {
        "data": {
            "text": "User cannot login to account"
        },
        "predictions": [
            {
                "result": [
                    {
                        "value": {
                            "choices": [
                                {
                                    "text": "Bug"
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    },
    {
        "data": {
            "text": "Add dark mode to settings"
        },
        "predictions": [
            {
                "result": [
                    {
                        "value": {
                            "choices": [
                                {
                                    "text": "Feature Request"
                                }
                            ]
                        }
                    }
                ]
            }
        ]
    }
]
```

Nach dem Import zeigt Label Studio jedes Ticket mit dem vom Model vorausgefüllten Label an. Die Aufgabe des Annotators ist es, zu **überprüfen und zu korrigieren**. Dieser halbautomatische Workflow hat sich als sehr effektiv erwiesen: Ein Beispiel von Kili Technology demonstrierte das Laden eines mit GPT vor-gelabelten Datensatzes und stellte fest, *„wir haben unseren Datensatz erfolgreich vor-annotiert“* und dass dieser Ansatz *„das Potenzial hat, uns viel Zeit zu sparen“*. In der Praxis liegt die Genauigkeit von GPT beim Labeling bei etwa 80–90 %, was bedeutet, dass Menschen nur die restlichen 10–20 % korrigieren.

## Werkzeuge und Workflow-Schritte

Zusammenfassend sieht eine typische halbautomatische Labeling-Pipeline wie folgt aus:

* **Ticket-Datensatz vorbereiten.** Exportieren Sie Ihre 10.000 ungelabelten Tickets (z. B. als JSON oder CSV).
* **Vor-Labels per LLM generieren.** Führen Sie Code (wie oben) aus, der GPT-4 (oder ein anderes Model über OpenRouter) aufruft, um jedes Ticket zu klassifizieren. Speichern Sie die Antworten.
* **Vorhersagen in ein Labeling-Tool importieren.** Verwenden Sie Label Studio (oder ein ähnliches Tool), um Tickets zu laden und jedem das von GPT generierte Label (die „prediction“) zuzuordnen. Die Dokumentation von Label Studio erklärt, wie man Vorhersagen mit seinen Daten importiert.
* **Menschliche Überprüfung.** Annotatoren gehen die Tickets in Label Studio durch, akzeptieren oder korrigieren die Labels. Dies ist viel schneller als das Labeling von Grund auf. Die Benutzeroberfläche von Label Studio hebt den Modellvorschlag für jede Aufgabe hervor, sodass die Aufgabe zu einer schnellen Validierung wird.
* **Endgültige Labels exportieren.** Nach der Überprüfung exportieren Sie die korrigierten Annotationen für das Modelltraining oder für Analysen.

Wichtige öffentliche Tools, die diesen Ansatz unterstützen, sind:

* **OpenRouter** – ein einheitliches LLM-API-Gateway (openrouter.ai). Es ermöglicht den einfachen Wechsel zwischen GPT-4, Anthropic Claude, Google PaLM usw. Sie können sogar eine Fallback-Liste in einem einzigen API-Aufruf angeben.
* **OpenAI API (GPT-4/3.5)** – die Kern-Engine zur Generierung von Labels mit Zero-/Few-Shot-Prompts.
* **Label Studio** – eine Open-Source-UI für Daten-Labeling. Es unterstützt den Import von Vorhersagen und verfügt über ein ML-Backend zum Aufrufen von Modellen.
* **Doccano** – ein einfacheres Open-Source-Tool für Textannotation (Klassifizierung, NER usw.). Es hat keine integrierte LLM-Integration, aber Sie können GPT trotzdem offline verwenden, um Labels zu generieren und sie als anfängliche Auswahl zu laden.
* **Snorkel/Programmatic Labeling** – für einige regelbasierte oder schwach überwachte Fälle (weak-supervision) können Tools wie Snorkel LLM-Labels ergänzen, aber moderne LLMs decken oft viele Fälle von Haus aus ab.

## Beispiel für Dummy-Ticketdaten

Zur Veranschaulichung hier einige *Dummy-Ticketdaten*, mit denen Sie arbeiten könnten:

```python
tickets = [
    {"id": 101, "text": "Error 500 when saving profile", "label": None},
    {"id": 102, "text": "How do I change my subscription plan?", "label": None},
    {"id": 103, "text": "Feature request: dark mode in settings", "label": None},
    {"id": 104, "text": "Application crashes on startup", "label": None},
]
```

Sie könnten jeden `ticket['text']` mit einem Prompt wie diesem an GPT übergeben:

```text
Ticket: "Error 500 when saving profile."
Classify this issue as one of {Bug, Feature, Question}.
```

Angenommen, GPT gibt jeweils `"Bug"`, `"Question"`, `"Feature"`, `"Bug"` zurück. Nach der Schleife könnte `tickets` so aussehen:

```python
[
    {'id': 101, 'text': 'Error 500 when saving profile', 'label': 'Bug'},
    {'id': 102, 'text': 'How do I change my subscription plan?', 'label': 'Question'},
    {'id': 103, 'text': 'Feature request: dark mode in settings', 'label': 'Feature'},
    {'id': 104, 'text': 'Application crashes on startup', 'label': 'Bug'},
]
```

Diese Labels würden dann in die Überprüfungsoberfläche geladen. Selbst wenn einige falsch sind (z. B. könnte GPT einen kniffligen Bug fälschlicherweise als Feature labeln), muss der Annotator sie nur *korrigieren*, anstatt von vorne anzufangen. Empirisch erreichen von GPT generierte Labels oft eine Genauigkeit von ca. 80–90 %, sodass die Überprüfung viel schneller ist als das vollständige Labeling.

## Ergebnisse und Erkenntnisse

Der halbautomatische Ansatz skaliert gut. In einem großen Projekt müssen menschliche Annotatoren möglicherweise nur einige hundert oder tausend Labels korrigieren, anstatt 10.000. Wie das Kili-Tutorial nach der Ausführung von GPT-Pre-Labels feststellte: *„Großartig! Wir haben unseren Datensatz erfolgreich vor-annotiert. Es sieht so aus, als hätte diese Lösung das Potenzial, uns in zukünftigen Projekten viel Zeit zu sparen.“*. Mit anderen Worten, LLMs dienen als Kraftmultiplikator. Auch wenn das Model nicht 100 % korrekt ist, **„beschleunigt es den Labeling-Prozess“**, indem es den größten Teil der Arbeit erledigt.

**Best Practices:** Verwenden Sie eine niedrige Temperature (z. B. 0.0–0.3) für konsistente Labels und geben Sie klare Anweisungen oder eine kleine Liste von Beispielen. Überwachen Sie die Fehler von GPT: Möglicherweise müssen Sie Prompts anpassen oder einige Few-Shot-Beispiele für Kategorien mit schlechter Leistung hinzufügen. Halten Sie den Prompt einfach (z. B. „Klassifiziere den Ticket-Text in A, B oder C“). Sie können auch mehrere Tickets in einem API-Aufruf bündeln, wenn das Model und die API dies zulassen, um Kosten zu sparen. Und schließen Sie immer eine menschliche Überprüfung ein – dies gewährleistet eine hohe Qualität und fängt alle LLM-Fehler oder -Abweichungen (drift) ab.

## Fazit

Halbautomatisches Labeling mit GPT und Tools wie OpenRouter und Label Studio ist eine leistungsstarke Strategie, um große Textdatensätze schnell zu kennzeichnen. Durch die **Vorkennzeichnung von 10.000 Tickets mit einem LLM und anschließender Überprüfung** können Unternehmen ihre AI-Workflows mit minimalen Anfangsdaten schnell starten. Dieser Ansatz senkt Kosten und Zeit drastisch und gewährleistet gleichzeitig die Qualität durch menschliche Aufsicht. Wie ein Implementierungsleitfaden feststellt, beschleunigt die Verlagerung des Workflows vom *„Daten-Labeling“* zum *„Überprüfen und Verfeinern“* von LLM-generierten Labels *„Ihren Workflow erheblich“*. Kurz gesagt, die Kombination von GPT-basierter Vor-Annotation mit einer benutzerfreundlichen UI (Label Studio, Doccano usw.) hilft Software-/AI-Teams, riesige Ticket-Datensätze effizient und genau zu labeln.