---
description: Lernen Sie, wie Sie ein KI-Modell mit Ihren eigenen Ticketdaten für eine
  präzise, automatisierte Ticket-Klassifizierung feinabstimmen. Diese Anleitung bietet
  Schritt-für-Schritt-Anweisungen zur Vorbereitung von Datensätzen und zum Training
  von Modellen mit Hugging Face Transformers oder einer On-Premise-REST-API.
---
# Wie man ein KI-Modell mit eigenen Ticketdaten feinabstimmt

Das Fine-Tuning eines KI-Modells mit Ihren eigenen Ticketdaten ist eine leistungsstarke Methode, um die Ticket-Klassifizierung für Ihr Unternehmen anzupassen. Indem Sie ein Modell mit gekennzeichneten Support-Tickets trainieren, bringen Sie ihm Ihre domänenspezifische Sprache und Kategorien bei. Dieser Prozess umfasst in der Regel die Vorbereitung eines Datensatzes (oft eine CSV- oder JSON-Datei mit Tickets und Labels), die Auswahl oder Erstellung von Labels (wie Abteilungen oder Prioritätsstufen) und das anschließende Training eines Modells wie eines Transformer-basierten Klassifikators mit diesen Daten. Sie können Werkzeuge wie die Transformer-Bibliothek von Hugging Face verwenden, um Modelle lokal zu trainieren, oder eine dedizierte Lösung wie **Open Ticket AI (ATC)** nutzen, die eine On-Premise-REST-API für die Ticket-Klassifizierung bereitstellt. In beiden Fällen profitieren Sie vom Transfer-Learning: Ein vortrainiertes Modell (z. B. BERT, DistilBERT oder RoBERTa) wird an Ihre Ticket-Kategorien angepasst, was die Genauigkeit im Vergleich zu einem generischen Modell erheblich verbessert.

Moderne Workflows zur Textklassifizierung folgen diesen übergeordneten Schritten:

* **Daten sammeln und kennzeichnen:** Sammeln Sie historische Tickets und weisen Sie ihnen die richtigen Kategorien (Queues) oder Prioritäten zu. Jedes Ticket sollte ein Textfeld und mindestens ein Label haben.
* **Dataset formatieren:** Speichern Sie diese gekennzeichneten Daten in einem strukturierten Format (CSV oder JSON). Eine CSV-Datei könnte beispielsweise die Spalten `"text"` und `"label"` haben.
* **In Trainings-/Testdaten aufteilen:** Reservieren Sie einen Teil zur Validierung/Testen, um die Leistung zu bewerten.
* **Modell feinabstimmen:** Verwenden Sie eine Bibliothek wie Hugging Face Transformers oder unsere Open Ticket AI API, um ein Klassifizierungsmodell mit den Daten zu trainieren.
* **Evaluieren und bereitstellen:** Überprüfen Sie die Genauigkeit (oder den F1-Score) an zurückgehaltenen Daten und verwenden Sie dann das trainierte Modell, um neue Tickets zu klassifizieren.

Technisch versierte Leser können diese Schritte im Detail befolgen. Die folgenden Beispiele veranschaulichen, wie Sie Ticketdaten vorbereiten und ein Modell mit **Hugging Face Transformers** feinabstimmen können, und wie unsere Open Ticket AI-Lösung diesen Workflow über API-Aufrufe unterstützt. Wir gehen dabei von gängigen Ticket-Kategorien (z. B. „Rechnungsstellung“, „Technischer Support“) und Prioritäts-Labels aus, aber Ihre Labels können alles sein, was für Ihr System relevant ist.

## Vorbereitung Ihrer Ticketdaten

Sammeln Sie zunächst einen repräsentativen Satz vergangener Tickets und kennzeichnen Sie diese gemäß Ihrem Klassifikationsschema. Labels können Abteilungen (wie **Technischer Support**, **Kundenservice**, **Rechnungsstellung** usw.) oder Prioritätsstufen (z. B. **Niedrig**, **Mittel**, **Hoch**) sein. Der Softoft-Ticket-Datensatz enthält beispielsweise Kategorien wie *Technischer Support*, *Rechnungsstellung und Zahlungen*, *IT-Support* und *Allgemeine Anfrage*. Ein Hugging Face Beispiel-Modell verwendet Labels wie *Frage zur Rechnung*, *Funktionswunsch*, *Allgemeine Anfrage* und *Technisches Problem*. Definieren Sie die Kategorien, die für Ihren Workflow sinnvoll sind.

Organisieren Sie die Daten im CSV- oder JSON-Format. Jeder Datensatz sollte den Ticket-Text und sein Label enthalten. Eine CSV-Datei könnte zum Beispiel so aussehen:

```
text,label
"Mein Drucker verbindet sich nicht mit dem WLAN",Hardware,  # Beispiel-Ticket-Text und seine Kategorie
"Ich benötige Hilfe beim Zugriff auf mein Konto",Konto
```

Wenn Sie Prioritäten oder mehrere Labels einbeziehen, können Sie weitere Spalten hinzufügen (z. B. `priority`). Die genaue Struktur ist flexibel, solange Sie jeden Ticket-Text eindeutig seinem Label (oder seinen Labels) zuordnen. Üblicherweise gibt es eine Spalte für den Ticket-Inhalt (z. B. `"text"` oder `"ticket_text"`) und eine Spalte für das Label.

Möglicherweise müssen Sie den Text leicht bereinigen und vorverarbeiten (z. B. Signaturen, HTML-Tags entfernen oder Daten anonymisieren), aber in vielen Fällen funktioniert der rohe Ticket-Text als Eingabe für moderne NLP-Modelle gut. Teilen Sie abschließend die gekennzeichneten Daten in einen Trainings- und einen Validierungs-/Testdatensatz auf (zum Beispiel 80 % Training / 20 % Test). Diese Aufteilung ermöglicht es Ihnen zu messen, wie gut das feinabgestimmte Modell verallgemeinert.

## Kennzeichnung von Tickets

Konsistente, genaue Labels sind entscheidend. Stellen Sie sicher, dass jedes Ticket korrekt einer Ihrer gewählten Kategorien zugewiesen wird. Dies kann manuell durch Support-Mitarbeiter erfolgen oder durch die Verwendung vorhandener Ticket-Metadaten, falls verfügbar. Oft kennzeichnen Organisationen Tickets nach *Queue* oder Abteilung und manchmal auch nach *Priorität*. Der Softoft-E-Mail-Ticket-Datensatz kategorisiert Tickets beispielsweise sowohl nach Abteilung (Queue) als auch nach Priorität. Die Priorität kann nützlich sein, wenn Sie ein Modell trainieren möchten, um die Dringlichkeit vorherzusagen: z. B. `Niedrig`, `Mittel`, `Kritisch`. In vielen Setups könnten Sie ein Modell für die Abteilungsklassifizierung und ein anderes für die Prioritätsklassifizierung trainieren.

Unabhängig von Ihrem Schema, stellen Sie sicher, dass Sie einen endlichen Satz von Label-Werten haben. In einer CSV-Datei könnten Sie Folgendes haben:

```
text,label,priority
"Systemabsturz beim Speichern der Datei","Technischer Support","Hoch"
"Anfrage zur Änderung der Rechnungsadresse","Rechnungsstellung","Niedrig"
```

Dieses Beispiel hat zwei Label-Spalten: eine für die Kategorie und eine für die Priorität. Der Einfachheit halber gehen wir in den folgenden Beispielen von einer Single-Label-Klassifizierungsaufgabe aus (eine Label-Spalte).

**Wichtige Tipps zur Kennzeichnung:**

* Definieren Sie Ihre Label-Namen eindeutig. Zum Beispiel *Technischer Support* vs. *IT-Support* vs. *Hardware-Problem* – vermeiden Sie mehrdeutige Überschneidungen.
* Wenn Tickets oft zu mehreren Kategorien gehören, könnten Sie eine Multi-Label-Klassifizierung (Zuweisung mehrerer Labels) in Betracht ziehen oder es in separate Modelle aufteilen.
* Verwenden Sie eine konsistente Formatierung (gleiche Schreibweise, Groß-/Kleinschreibung) für die Labels in Ihrem Datensatz.

Am Ende dieses Schrittes sollten Sie eine gekennzeichnete Datensatzdatei (CSV oder JSON) mit Ticket-Texten und deren Labels haben, die für das Modell bereit ist.

## Fine-Tuning mit Hugging Face Transformers

Eine der flexibelsten Methoden zum Fine-Tuning eines Textklassifikators ist die Verwendung der [Hugging Face Transformers](https://huggingface.co/transformers/)-Bibliothek. Damit können Sie mit einem vortrainierten Sprachmodell (wie BERT oder RoBERTa) beginnen und es auf Ihrem spezifischen Ticket-Datensatz weiter trainieren. Die Kernschritte sind: den Text tokenisieren, einen `Trainer` einrichten und `train()` aufrufen.

1. **Dataset laden:** Verwenden Sie `datasets` oder `pandas`, um Ihre CSV/JSON-Datei zu laden. Die `datasets`-Bibliothek von Hugging Face kann beispielsweise eine CSV-Datei direkt einlesen:

   ```python
   from datasets import load_dataset
   dataset = load_dataset("csv", data_files={
       "train": "tickets_train.csv",
       "validation": "tickets_val.csv"
   })
   # Annahme: 'text' ist die Spalte mit dem Ticket-Inhalt und 'label' die Kategoriespalte.
   ```

2. **Text tokenisieren:** Vortrainierte Transformer benötigen eine tokenisierte Eingabe. Laden Sie einen Tokenizer (z. B. von DistilBERT) und wenden Sie ihn auf Ihren Text an:

   ```python
   from transformers import AutoTokenizer
   tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

   def preprocess_function(examples):
       # Tokenisiert die Texte (dies erzeugt input_ids, attention_mask, etc.)
       return tokenizer(examples["text"], truncation=True, padding="max_length")

   tokenized_datasets = dataset.map(preprocess_function, batched=True)
   ```

   Dies folgt dem Hugging Face-Beispiel: Zuerst wird der DistilBERT-Tokenizer geladen, dann wird `Dataset.map` verwendet, um alle Texte in Batches zu tokenisieren. Das Ergebnis (`tokenized_datasets`) enthält Input-IDs und Attention-Masks, bereit für das Modell.

3. **Modell laden:** Wählen Sie ein vortrainiertes Modell und geben Sie die Anzahl der Labels an. Zum Beispiel, um DistilBERT für die Klassifizierung feinabzustimmen:

   ```python
   from transformers import AutoModelForSequenceClassification
   num_labels = 4  # auf die Anzahl Ihrer Kategorien setzen
   model = AutoModelForSequenceClassification.from_pretrained(
       "distilbert-base-uncased", num_labels=num_labels
   )
   ```

   Dies entspricht dem Sequenzklassifizierungs-Beispiel von Hugging Face, bei dem das Modell mit `num_labels` geladen wird, was der Anzahl der Klassen in Ihrem Datensatz entspricht.

4. **Trainingsargumente und Trainer festlegen:** Definieren Sie Hyperparameter mit `TrainingArguments` und erstellen Sie dann einen `Trainer` mit Ihrem Modell und den tokenisierten Daten:

   ```python
   from transformers import TrainingArguments, Trainer
   training_args = TrainingArguments(
       output_dir="./ticket_model",
       num_train_epochs=3,
       per_device_train_batch_size=8,
       per_device_eval_batch_size=8,
       learning_rate=2e-5,
       evaluation_strategy="epoch"
   )
   trainer = Trainer(
       model=model,
       args=training_args,
       train_dataset=tokenized_datasets["train"],
       eval_dataset=tokenized_datasets["validation"],
       tokenizer=tokenizer
   )
   ```

   Dies spiegelt die Anleitung von Hugging Face wider: Nach dem Einrichten der `TrainingArguments` (für Ausgabeverzeichnis, Epochen, Batch-Größe usw.) instanziieren wir den `Trainer` mit dem Modell, den Datensätzen, dem Tokenizer und den Trainingsargumenten.

5. **Modell trainieren:** Rufen Sie `trainer.train()` auf, um das Fine-Tuning zu starten. Dies läuft für die angegebene Anzahl von Epochen und evaluiert periodisch auf dem Validierungsdatensatz, falls vorhanden.

   ```python
   trainer.train()
   ```

   Gemäß der Dokumentation startet dieser einzelne Befehl das Fine-Tuning. Das Training kann Minuten bis Stunden dauern, abhängig von der Datengröße und der Hardware (GPU für große Datensätze empfohlen).

6. **Evaluieren und Speichern:** Nach dem Training evaluieren Sie das Modell auf Ihrem Testdatensatz, um die Genauigkeit oder andere Metriken zu überprüfen. Speichern Sie dann das feinabgestimmte Modell und den Tokenizer:

   ```python
   trainer.evaluate()
   model.save_pretrained("fine_tuned_ticket_model")
   tokenizer.save_pretrained("fine_tuned_ticket_model")
   ```

   Sie können dieses Modell später mit `AutoModelForSequenceClassification.from_pretrained("fine_tuned_ticket_model")` wieder laden.

Nach dem Training können Sie das Modell für die Inferenz verwenden. Die Pipeline-API von Hugging Face macht es zum Beispiel einfach:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
results = classifier("Bitte setzen Sie mein Passwort zurück und leeren Sie meinen Cache.")
print(results)
```

Dies gibt das vorhergesagte Label und die Konfidenz für den neuen Ticket-Text aus. Wie in den Beispielen von Hugging Face gezeigt, ermöglicht die `pipeline("text-classification")`-Abstraktion eine schnelle Klassifizierung neuer Ticket-Texte mit dem feinabgestimmten Modell.

## Verwendung von Open Ticket AI (Softofts ATC) für Training und Inferenz

Unser **Open Ticket AI**-System (auch bekannt als ATC – AI Ticket Classification) bietet eine On-Premise-, Docker-basierte Lösung mit einer REST-API, die Ihre gekennzeichneten Ticketdaten aufnehmen und Modelle automatisch trainieren kann. Das bedeutet, Sie können alle Daten lokal halten und trotzdem leistungsstarkes ML nutzen. Die ATC-API verfügt über Endpunkte zum Hochladen von Daten, zum Auslösen des Trainings und zum Klassifizieren von Tickets.

* **Trainingsdaten hochladen:** Senden Sie Ihre gekennzeichnete Ticket-CSV-Datei an den `/api/v1/train-data`-Endpunkt. Die API erwartet einen CSV-Payload (`Content-Type: text/csv`), der Ihre Trainingsdaten enthält. Zum Beispiel mit Python `requests`:

  ```python
  import requests
  url = "http://localhost:8080/api/v1/train-data"
  headers = {"Content-Type": "text/csv"}
  with open("tickets_labeled.csv", "rb") as f:
      res = requests.post(url, headers=headers, data=f)
  print(res.status_code, res.text)
  ```

  Dies entspricht der „Train Data“-API in der ATC-Dokumentation. Eine erfolgreiche Antwort bedeutet, dass die Daten empfangen wurden.

* **Modelltraining starten:** Nach dem Hochladen der Daten lösen Sie das Training durch einen Aufruf von `/api/v1/train` aus (kein Body erforderlich). In der Praxis:

  ```bash
  curl -X POST http://localhost:8080/api/v1/train
  ```

  Oder in Python:

  ```python
  train_res = requests.post("http://localhost:8080/api/v1/train")
  print(train_res.status_code, train_res.text)
  ```

  Dies entspricht dem Beispiel in der Entwicklerdokumentation, das zeigt, dass ein einfacher POST-Request das Training startet. Der Dienst trainiert das Modell mit den hochgeladenen Daten (er verwendet intern seine eigene Trainings-Pipeline, möglicherweise basierend auf ähnlichen Transformer-Modellen). Das Training läuft auf Ihrem Server, und das Modell wird nach Abschluss lokal gespeichert.

* **Neue Tickets klassifizieren:** Sobald das Training abgeschlossen ist, verwenden Sie den `/api/v1/classify`-Endpunkt, um Vorhersagen für neue Ticket-Texte zu erhalten. Senden Sie einen JSON-Payload mit dem Feld `"ticket_data"`, das den Ticket-Text enthält. Zum Beispiel:

  ```python
  ticket_text = "Mein Laptop überhitzt, wenn ich die App starte"
  res = requests.post(
      "http://localhost:8080/api/v1/classify",
      json={"ticket_data": ticket_text}
  )
  print(res.json())  # z. B. {"predicted_label": "Hardware-Problem", "confidence": 0.95}
  ```

  Die ATC-Dokumentation zeigt ein ähnliches `curl`-Beispiel für die Klassifizierung. Die Antwort enthält typischerweise die vorhergesagte Kategorie (und möglicherweise die Konfidenz).

Die Verwendung der REST-API von Open Ticket AI integriert den Trainingsablauf in Ihre eigenen Systeme. Sie können Uploads und Trainingsläufe automatisieren (z. B. nächtliches Training oder Training mit neuen Daten) und dann den Klassifizierungs-Endpunkt in Ihrem Ticketing-Workflow verwenden. Da alles On-Premise läuft, verlassen sensible Ticket-Inhalte niemals Ihre Server.

## Beispiel für Python-Code

Unten finden Sie ein zusammenfassendes Beispiel, das beide Workflows veranschaulicht:

```python
# Beispiel: Fine-Tuning mit Hugging Face
from transformers import AutoTokenizer,
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments
from datasets import load_dataset

# Laden und Aufteilen Ihres CSV-Datensatzes
dataset = load_dataset("csv", data_files={"train": "train.csv", "validation": "val.csv"})
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


# Tokenisieren
def preprocess(examples):
    return tokenizer(examples["text"], truncation=True, padding="max_length")


tokenized = dataset.map(preprocess, batched=True)

# Modell laden
num_labels = 5  # z. B. Anzahl der Ticket-Kategorien
model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert-base-uncased",
    num_labels=num_labels
    )

# Trainer einrichten
training_args = TrainingArguments(
    output_dir="./model_out", num_train_epochs=3, per_device_train_batch_size=8
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["validation"],
    tokenizer=tokenizer
)
trainer.train()
trainer.evaluate()
model.save_pretrained("fine_tuned_ticket_model")
tokenizer.save_pretrained("fine_tuned_ticket_model")

# Modell zur Klassifizierung verwenden
from transformers import pipeline

classifier = pipeline("text-classification", model="fine_tuned_ticket_model")
print(classifier("Beispiel: Die App stürzt ab, wenn ich versuche, sie zu öffnen"))

# Beispiel: Verwendung der Open Ticket AI API
import requests

# Daten hochladen (CSV)
with open("tickets_labeled.csv", "rb") as data_file:
    res = requests.post(
        "http://localhost:8080/api/v1/train-data",
        headers={"Content-Type": "text/csv"},
        data=data_file
        )
    print("Upload-Status:", res.status_code)
# Training auslösen
train_res = requests.post("http://localhost:8080/api/v1/train")
print("Trainings-Status:", train_res.status_code)
# Neues Ticket klassifizieren
res = requests.post(
    "http://localhost:8080/api/v1/classify",
    json={"ticket_data": "Kann mich nicht im Konto anmelden"}
    )
print("Vorhersage:", res.json())
```

Dieses Skript demonstriert beide Methoden: die Hugging Face Fine-Tuning-Pipeline und die REST-Aufrufe an die Open Ticket AI. Es lädt und tokenisiert einen CSV-Datensatz, stimmt einen DistilBERT-Klassifikator fein ab und verwendet ihn dann über eine Pipeline. Es zeigt auch, wie man dieselben Daten per POST an die ATC-API sendet, um Training/Klassifizierung auszulösen.

## Fazit

Das Fine-Tuning eines KI-Modells mit Ihren eigenen Ticketdaten ermöglicht eine hochpräzise, angepasste Ticket-Klassifizierung. Durch die Kennzeichnung vergangener Tickets und das Training eines Modells wie eines Transformers nutzen Sie Transfer-Learning und Domänenwissen. Unabhängig davon, ob Sie die Python-APIs von Hugging Face oder eine schlüsselfertige Lösung wie Open Ticket AI (Softofts On-Prem-Klassifizierungsdienst) verwenden, ist der Workflow ähnlich: gekennzeichnete Daten vorbereiten, damit trainieren und dann das trainierte Modell für Vorhersagen verwenden.

Wir haben gezeigt, wie Sie Ihren CSV/JSON-Datensatz strukturieren, die `Trainer`-API von Hugging Face zum Fine-Tuning verwenden und die Open Ticket AI REST-API für On-Prem-Training und Inferenz nutzen. Die Dokumentation von Hugging Face bietet detaillierte Anleitungen zur Verwendung von Tokenizern und dem `Trainer`, und Beispiel-Model-Cards veranschaulichen, wie Klassifizierungsmodelle für das Ticket-Routing eingesetzt werden. Mit diesen Werkzeugen können Sie schnell iterieren: Probieren Sie verschiedene vortrainierte Modelle aus (z. B. BERT, RoBERTa oder sogar domänenspezifische Modelle), experimentieren Sie mit Hyperparametern und messen Sie die Leistung an Ihrem Testdatensatz.

Indem Sie diese Schritte befolgen, kann Ihr Support-System Tickets automatisch an das richtige Team weiterleiten, dringende Probleme kennzeichnen und Ihren Mitarbeitern unzählige Stunden manueller Sortierung ersparen. Diese tiefe Integration von NLP in Ihren Ticket-Workflow ist jetzt mit modernen Bibliotheken und APIs zugänglich – Sie müssen nur Ihre Daten und Labels bereitstellen.