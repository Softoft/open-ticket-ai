---
description: Sparen Sie Zeit und Kosten bei der Kennzeichnung von Tausenden von Tickets.
  Erfahren Sie, wie Sie GPT für die halbautomatische Zero-Shot-Vorkennzeichnung und
  Tools wie Label Studio für eine effiziente menschliche Überprüfung nutzen können.
  Enthält Python-Beispiele.
---
# Effiziente Kennzeichnung von 10.000 Tickets: Strategien für die halbautomatische Kennzeichnung

Die manuelle Kennzeichnung von Tausenden von Support-Tickets ist zeitaufwändig und teuer. Ein **halbautomatischer Workflow** nutzt große Sprachmodelle (LLMs) wie GPT, um Tickets **vorzukennzeichnen** (mittels Zero-Shot-/Few-Shot-Prompts) und lässt menschliche Annotatoren diese Kennzeichnungen anschließend **überprüfen und korrigieren**. Dieser hybride Ansatz reduziert den Annotationsaufwand drastisch: Eine Fallstudie ergab beispielsweise, dass von GPT generierte „Vor-Annotationen“ *„gut genug waren, um uns zu helfen, den Kennzeichnungsprozess zu beschleunigen“*. In der Praxis können *minimale Kennzeichnungen* vom `model` den Zeit- und Kostenaufwand für die Annotation reduzieren. In diesem Artikel erklären wir, wie man eine solche Pipeline einrichtet, zeigen `Python`-Beispiele (mit GPT über OpenRouter oder OpenAI) und besprechen Tools wie Label Studio für die Überprüfung.

## Verwendung von GPT für die Zero-Shot-/Few-Shot-Vorkennzeichnung

Moderne LLMs können Text mit **null oder wenigen Beispielen** klassifizieren. Beim Zero-Shot-Labeling weist das `model` Kategorien zu, ohne explizit auf Ticket-Daten trainiert worden zu sein. Wie es in einem Tutorial heißt: *„Zero-Shot-Lernen ermöglicht es Modellen, neue Instanzen ohne gekennzeichnete Beispiele zu klassifizieren“*. In der Praxis erstellen Sie einen Prompt, der GPT anweist, ein Ticket zu kennzeichnen. Zum Beispiel:

```text
Ticket: "Cannot login to account."
Classify this ticket into one of {Bug, Feature Request, Question}.
```

Das `model` antwortet dann mit einer Kennzeichnung. Few-Shot-Labeling fügt dem Prompt einige Beispiele hinzu, um die Genauigkeit zu verbessern. Das bedeutet, wir können anfängliche Kennzeichnungen **direkt über die API** ohne jegliches `model`-Training generieren.

> **Tipp:** Verwenden Sie einen strukturierten Prompt oder fordern Sie eine `JSON`-Ausgabe an, um das Parsen zu erleichtern. Zum Beispiel:
>
> ```
> Ticket: "Password reset email bounced."
> Respond in JSON like {"category": "..."}.
> ```
>
> Dies hilft bei der Integration der Antwort in Ihre Pipeline.

## Beispiel: Python-Code für die Vorkennzeichnung

Unten sehen Sie ein `Python`-Beispiel, das die `API` von OpenAI über die `openai`-Bibliothek verwendet. Es durchläuft eine Dummy-Ticketliste, fordert GPT-4 auf, jedes Ticket zu klassifizieren, und speichert die Kategorie. (Sie können [OpenRouter](https://openrouter.ai) auf ähnliche Weise verwenden, indem Sie `base_url="https://openrouter.ai/api/v1"` setzen und den `model`-Parameter ändern.)

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

Dies sind **Vorkennzeichnungen**, die menschliche Prüfer kontrollieren werden. Beachten Sie, wie OpenRouter den Wechsel von Modellen erleichtert: Durch Ändern von `model="openai/gpt-4"` zu einem anderen Anbieter (z. B. Claude oder einem leichteren `model`) funktioniert derselbe Code. Tatsächlich ermöglicht die einheitliche `API` von OpenRouter das Ausprobieren mehrerer Anbieter oder die Verwendung von Fallback-Modellen, falls eines ausfällt. Zum Beispiel:

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

Dies verwendet GPT-4, falls verfügbar, andernfalls wird auf Claude oder PaLM zurückgegriffen, wie in der Dokumentation von OpenRouter gezeigt. Eine solche Flexibilität ist nützlich für Unternehmen, die eine hohe Verfügbarkeit benötigen oder Modelle vergleichen möchten.

## Integration von Vorkennzeichnungen in Labeling-Tools

Sobald GPT Kennzeichnungen generiert hat, ist der nächste Schritt, sie **in eine Kennzeichnungsoberfläche** für die menschliche Überprüfung zu importieren. Eine beliebte Open-Source-Lösung ist [Label Studio](https://labelstud.io). Label Studio unterstützt den Import von `model`-Vorhersagen als „Vor-Annotationen“ zusammen mit den Daten. Annotatoren sehen die vorgeschlagene Kennzeichnung und müssen nur Fehler korrigieren, anstatt von Grund auf neu zu kennzeichnen. Im Grunde genommen wechselt das Team *„von der zeitintensiven Aufgabe der Datenkennzeichnung zum weitaus effizienteren Prozess der Überprüfung und Verfeinerung der vorläufigen Kennzeichnungen“*.

Label Studio bietet sogar ein ML-Backend: Sie können einen kleinen Server mit der `LabelStudioMLBase`-`class` schreiben, der für jede Aufgabe GPT aufruft. In ihrem Tutorial zeigt Label Studio, wie GPT-4-Aufrufe in diese `class` eingebettet werden, um Vorhersagen spontan zurückzugeben. Alternativ können Sie eine `JSON`-Datei mit Vorhersagen importieren. Das erforderliche `JSON`-Format hat ein `data`-Feld (den Ticket-Text) und ein `predictions`-Array (das jede Kennzeichnung enthält). Zum Beispiel (vereinfacht):

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

Nach dem Import zeigt Label Studio jedes Ticket mit der vom `model` vorausgefüllten Kennzeichnung an. Die Aufgabe des Annotators besteht darin, zu **überprüfen und zu korrigieren**. Dieser halbautomatische Workflow hat sich als gut funktionierend erwiesen: Ein Beispiel von Kili Technology demonstrierte das Laden eines mit GPT vor-gekennzeichneten Datensatzes und stellte fest: *„Wir haben unseren Datensatz erfolgreich vor-annotiert“* und dass dieser Ansatz *„das Potenzial hat, uns viel Zeit zu sparen“*. In der Praxis liegt die Genauigkeit von GPT bei der Kennzeichnung bei etwa 80–90 %, was bedeutet, dass Menschen nur die verbleibenden 10–20 % korrigieren.

## Tools und Workflow-Schritte

Zusammenfassend sieht eine typische halbautomatische Kennzeichnungs-Pipeline wie folgt aus:

*   **Ticket-Datensatz vorbereiten.** Exportieren Sie Ihre 10.000 ungekennzeichneten Tickets (z. B. als `JSON` oder CSV).
*   **Vorkennzeichnungen per LLM generieren.** Führen Sie Code (wie oben) aus, der GPT-4 (oder ein anderes `model` über OpenRouter) aufruft, um jedes Ticket zu klassifizieren. Speichern Sie die Antworten.
*   **Vorhersagen in ein Labeling-Tool importieren.** Verwenden Sie Label Studio (oder Ähnliches), um Tickets zu laden und jedes mit der von GPT generierten Kennzeichnung (der „Vorhersage“) zu verknüpfen. Die Dokumentation von Label Studio erklärt, wie man Vorhersagen mit seinen Daten importiert.
*   **Menschliche Überprüfung.** Annotatoren gehen die Tickets in Label Studio durch und akzeptieren oder korrigieren die Kennzeichnungen. Dies ist viel schneller als das Kennzeichnen von Grund auf. Die Benutzeroberfläche von Label Studio hebt den `model`-Vorschlag für jede Aufgabe hervor, sodass die Aufgabe zu einer schnellen Validierung wird.
*   **Endgültige Kennzeichnungen exportieren.** Nach der Überprüfung exportieren Sie die korrigierten Annotationen für das `model`-Training oder für Analysen.

Wichtige öffentliche Tools, die diesen Ansatz unterstützen, sind:

*   **OpenRouter** – ein einheitliches LLM-`API`-Gateway (openrouter.ai). Es ermöglicht den einfachen Wechsel zwischen GPT-4, Anthropic Claude, Google PaLM usw. Sie können sogar eine Fallback-Liste in einem einzigen `API`-Aufruf angeben.
*   **OpenAI API (GPT-4/3.5)** – die Kern-Engine zur Generierung von Kennzeichnungen mit Zero-/Few-Shot-Prompts.
*   **Label Studio** – eine Open-Source-Benutzeroberfläche für die Datenkennzeichnung. Es unterstützt den Import von Vorhersagen und verfügt über ein ML-Backend zum Aufrufen von Modellen.
*   **Doccano** – ein einfacheres Open-Source-Tool für die Textannotation (Klassifizierung, NER usw.). Es hat keine integrierte LLM-Integration, aber Sie können GPT trotzdem offline verwenden, um Kennzeichnungen zu generieren und sie als anfängliche Auswahl zu laden.
*   **Snorkel/Programmatic Labeling** – für einige regelbasierte oder schwach überwachte Fälle können Tools wie Snorkel LLM-Kennzeichnungen ergänzen, aber moderne LLMs decken oft viele Fälle von Haus aus ab.

## Beispiel für Dummy-Ticketdaten

Zur Veranschaulichung finden Sie hier einige *Dummy-Ticketdaten*, mit denen Sie arbeiten könnten:

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

Diese Kennzeichnungen würden dann in die Überprüfungsoberfläche geladen. Selbst wenn einige falsch sind (z. B. könnte GPT einen kniffligen Bug fälschlicherweise als Feature kennzeichnen), muss der Annotator sie nur *korrigieren*, anstatt von Grund auf neu anzufangen. Empirisch erreichen von GPT generierte Kennzeichnungen oft eine Genauigkeit von ~80–90 %, sodass die Überprüfung viel schneller ist als die vollständige Kennzeichnung.

## Ergebnisse und Erkenntnisse

Der halbautomatische Ansatz skaliert gut. In einem großen Projekt müssen menschliche Annotatoren möglicherweise nur einige hundert oder tausend Kennzeichnungen korrigieren, anstatt 10.000. Wie das Kili-Tutorial nach der Ausführung von GPT-Vorkennzeichnungen feststellte: *„Großartig! Wir haben unseren Datensatz erfolgreich vor-annotiert. Es sieht so aus, als hätte diese Lösung das Potenzial, uns in zukünftigen Projekten viel Zeit zu sparen.“*. Mit anderen Worten, LLMs dienen als Kraftmultiplikator. Auch wenn das `model` nicht 100 % korrekt ist, **„beschleunigt es den Kennzeichnungsprozess“**, indem es den größten Teil der Arbeit erledigt.

**Best Practices:** Verwenden Sie eine niedrige Temperatur (z. B. 0.0–0.3) für konsistente Kennzeichnungen und geben Sie klare Anweisungen oder eine kleine Liste von Beispielen. Überwachen Sie die Fehler von GPT: Möglicherweise müssen Sie Prompts anpassen oder einige Few-Shot-Beispiele für Kategorien mit schlechter Leistung hinzufügen. Halten Sie den Prompt einfach (z. B. „Klassifiziere den Ticket-Text in A, B oder C“). Sie können auch mehrere Tickets in einem `API`-Aufruf bündeln, wenn das `model` und die `API` dies zulassen, um Kosten zu sparen. Und schließen Sie immer eine menschliche Überprüfung ein – dies gewährleistet eine hohe Qualität und fängt alle LLM-Fehler oder -Abweichungen ab.

## Fazit

Die halbautomatische Kennzeichnung mit GPT und Tools wie OpenRouter und Label Studio ist eine leistungsstarke Strategie zur schnellen Kennzeichnung großer Textdatensätze. Indem Unternehmen **10.000 Tickets mit einem LLM vorkennzeichnen und diese dann überprüfen**, können sie ihre KI-Workflows mit minimalen Anfangsdaten schnell starten. Dieser Ansatz senkt Kosten und Zeit drastisch und gewährleistet gleichzeitig die Qualität durch menschliche Aufsicht. Wie ein Implementierungsleitfaden feststellt, beschleunigt die Verlagerung des Workflows von der *„Datenkennzeichnung“* zum *„Überprüfen und Verfeinern“* von LLM-generierten Kennzeichnungen *„Ihren Workflow erheblich.“*. Kurz gesagt, die Kombination von GPT-basierter Vor-Annotation mit einer benutzerfreundlichen Oberfläche (Label Studio, Doccano usw.) hilft Software-/KI-Teams, riesige Ticket-Datensätze effizient und genau zu kennzeichnen.