---
title: Training von KI-Models für Open Ticket AI
description: Anleitung zum Trainieren oder Fine-Tuning von Models für Open Ticket AI.
---

# Training des Model

:::note
Sie müssen nur dann ein eigenes Model trainieren, wenn Sie ein benutzerdefiniertes Model verwenden oder die Standard-Models per Fine-Tuning anpassen möchten. Um gute Ergebnisse zu erzielen, ist eine erhebliche Menge an Trainingsdaten erforderlich – idealerweise mindestens 1000 Tickets pro Warteschlange und Priorität. Datenbereinigung, Normalisierung, Tokenisierung und das Experimentieren mit verschiedenen Models und Hyperparametern sind oft erforderlich.
:::

Das Training oder Fine-Tuning eines Model für Open Ticket AI umfasst mehrere Schlüsselschritte:

### 1. Datensammlung

*   **Historische Daten exportieren**: Sammeln Sie historische Ticketdaten (einschließlich Betreff und Text) aus Ihrem bestehenden Ticketsystem.
*   **Daten labeln**: Weisen Sie jedem Ticket die korrekte Warteschlange und Priorität zu. Dieser gelabelte Datensatz bildet die Grundlage für das Training Ihres Model.

### 2. Datenbereinigung

*   **Stördaten entfernen**: Beseitigen Sie irrelevante Informationen wie E-Mail-Signaturen, personenbezogene Daten (PII) und Spam.
*   **Text normalisieren**: Standardisieren Sie Leerräume und stellen Sie eine konsistente Zeichenkodierung sicher.

### 3. Datentransformation & Tokenisierung

*   **Felder kombinieren**: Verketten Sie den Betreff und den Text der Tickets zu einem einzigen Eingabetext für das Model.
*   **`max_length` festlegen**: Wählen Sie eine geeignete `max_length` für die Tokenisierung (z. B. 256–512 Tokens), basierend auf der medianen Länge Ihrer Tickets. Dies verhindert das Abschneiden wichtiger Informationen und schont gleichzeitig die Rechenressourcen.
*   **Tokenizer verwenden**: Nutzen Sie den bereitgestellten `ticket_combined_email_tokenizer` oder einen Tokenizer, der mit dem von Ihnen gewählten Model kompatibel ist.

### 4. Model-Auswahl & Hardware

Berücksichtigen Sie bei der Auswahl eines Model und der erforderlichen Hardware Folgendes:

| Model                          | Benötigter RAM | Anmerkungen                   |
| ------------------------------ | -------------- | ----------------------------- |
| `distilbert-base-german-cased` | 2 GB           | Leichtgewichtig, deutscher Text |
| `bert-base-german-cased`       | 4 GB           | Höhere Genauigkeit, deutscher Text |
| `deberta-large-mnli`           | 8 GB           | Mehrsprachig / große Kontexte |

(*Hinweis: Die obige Tabelle enthält Beispiele; die tatsächlichen Anforderungen können abweichen.*)

### 5. Training & Fine-Tuning

*   **Hyperparameter-Tuning**: Verwenden Sie den integrierten Hyperparameter-Tuner, um mit Einstellungen wie `learning_rate`, `batch_size` und `epochs` zu experimentieren und die optimale Konfiguration für Ihren Datensatz zu finden.
*   **Leistung überwachen**: Das Trainingsskript gibt eine Zusammenfassung der Leistung und Ressourcennutzung des Model aus, die Ihnen hilft, den Fortschritt zu verfolgen und Anpassungen vorzunehmen.

### 6. Evaluierung

*   **Genauigkeit messen**: Bewerten Sie die Leistung des Model anhand seiner Genauigkeit bei der Vorhersage von Warteschlange und Priorität.
*   **Konfidenz analysieren**: Untersuchen Sie die Beziehung zwischen den Konfidenzwerten des Model und der Korrektheit seiner Vorhersagen. Diese Analyse ist entscheidend für die Festlegung eines optimalen `confidence_threshold` in der Konfiguration.
*   **Confidence-Weighted Accuracy Score (CWAS)** (Optional): Sie könnten die Verwendung einer Metrik wie CWAS in Betracht ziehen, um eine differenziertere Sicht auf die Leistung zu erhalten:
    ```math
    \text{CWAS} = \text{percent_predicted} \times (\text{percent_correct}^2)
    ```
    Dieser Score belohnt Models, die sowohl genau sind als auch einen hohen Prozentsatz an Vorhersagen treffen (d. h. sich bei Fällen mit geringer Konfidenz nicht übermäßig auf einen Standardwert zurückfallen lassen).