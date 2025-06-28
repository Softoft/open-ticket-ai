---
title: Training von KI-Modellen für Open Ticket AI
description: Anleitung zum Trainieren oder Feinabstimmen von Modellen für Open Ticket AI.
---

# Training des Modells

:::note
Sie müssen nur dann ein eigenes Modell trainieren, wenn Sie ein benutzerdefiniertes Modell verwenden oder die Standardmodelle feinabstimmen möchten. Um gute Ergebnisse zu erzielen, ist eine erhebliche Menge an Trainingsdaten erforderlich – idealerweise mindestens 1000 Tickets pro Warteschlange und Priorität. Häufig sind Datenbereinigung, Normalisierung, Tokenisierung und Experimente mit verschiedenen Modellen und Hyperparametern notwendig.
:::

Das Training oder Feinabstimmen eines Modells für Open Ticket AI umfasst mehrere Schritte:

### 1. Datensammlung

*   **Export historischer Daten**: Sammeln Sie historische Ticketdaten (einschließlich Betreff und Text) aus Ihrem bestehenden Ticketsystem.
*   **Datenkennzeichnung**: Kennzeichnen Sie jedes Ticket korrekt mit der richtigen Warteschlange und Priorität. Dieser gekennzeichnete Datensatz bildet die Grundlage für das Training Ihres Modells.

### 2. Datenbereinigung

*   **Rauschentfernung**: Entfernen Sie irrelevante Informationen wie E-Mail-Signaturen, personenbezogene Daten (PII) und Spam.
*   **Textnormalisierung**: Standardisieren Sie Leerzeichen und stellen Sie konsistente Zeichenkodierungen sicher.

### 3. Datentransformation & Tokenisierung

*   **Feldkombination**: Verknüpfen Sie Betreff und Text der Tickets zu einem einzigen Eingabetext für das Modell.
*   **`max_length` festlegen**: Wählen Sie eine geeignete `max_length` für die Tokenisierung (z.B. 256–512 Tokens) basierend auf der durchschnittlichen Ticketlänge. Dies verhindert das Abschneiden wichtiger Informationen bei gleichzeitiger Ressourcenoptimierung.
*   **Tokenizer verwenden**: Nutzen Sie den bereitgestellten `ticket_combined_email_tokenizer` oder einen mit Ihrem Modell kompatiblen Tokenizer.

### 4. Modellauswahl & Hardware

Berücksichtigen Sie bei der Modell- und Hardwareauswahl folgende Aspekte:

| Modell                          | Benötigter RAM | Anmerkungen                         |
| ------------------------------ | ------------ | ----------------------------- |
| `distilbert-base-german-cased` | 2 GB         | Leichtgewicht, deutscher Text      |
| `bert-base-german-cased`       | 4 GB         | Höhere Genauigkeit, deutscher Text  |
| `deberta-large-mnli`           | 8 GB         | Mehrsprachig / große Kontexte |

(*Hinweis: Die Tabelle dient der Veranschaulichung; tatsächliche Anforderungen können variieren.*)

### 5. Training & Feinabstimmung

*   **Hyperparameter-Abstimmung**: Nutzen Sie den integrierten Hyperparameter-Tuner, um Einstellungen wie `learning_rate`, `batch_size` und `epochs` zu optimieren.
*   **Leistungsüberwachung**: Das Trainingsskript liefert eine Zusammenfassung der Modellleistung und Ressourcennutzung zur Fortschrittskontrolle.

### 6. Auswertung

*   **Genauigkeitsmessung**: Bewerten Sie die Modellleistung anhand der Vorhersagegenauigkeit für Warteschlangen und Prioritäten.
*   **Konfidenzanalyse**: Untersuchen Sie den Zusammenhang zwischen Konfidenzwerten des Modells und Vorhersagekorrektheit. Diese Analyse ist entscheidend für die Festlegung eines optimalen `confidence_threshold` in der Konfiguration.
*   **Confidence-Weighted Accuracy Score (CWAS)** (Optional): Für eine differenzierte Leistungsbewertung kann CWAS verwendet werden:
    ```math
    \text{CWAS} = \text{percent_predicted} \times (\text{percent_correct}^2)
    ```
    Diese Metrik begünstigt Modelle mit hoher Genauigkeit und Vorhersagequote (geringe Rückfallrate auf Standardwerte bei niedriger Konfidenz).