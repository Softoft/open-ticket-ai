---
description: Lernen Sie, wie Sie benutzerdefinierte KI-Modelle für Open Ticket AI trainieren und feinabstimmen. Diese Anleitung behandelt die wesentlichen Schritte von der Datensammlung und -bereinigung über die Hyperparameter-Abstimmung bis hin zur Modellevaluierung, um die Genauigkeit der Klassifizierung von Ticket-Warteschlangen und -Prioritäten zu verbessern.
title: Training von KI-Modellen für Open Ticket AI
---
# Training des Modells

:::note
Sie müssen nur dann Ihr eigenes Modell trainieren, wenn Sie ein benutzerdefiniertes Modell verwenden oder die Standardmodelle feinabstimmen möchten. Um gute Ergebnisse zu erzielen, ist eine erhebliche Menge an Trainingsdaten erforderlich – idealerweise mindestens 1000 Tickets pro Warteschlange und Priorität. Datenbereinigung, Normalisierung, Tokenisierung und das Experimentieren mit verschiedenen Modellen und Hyperparametern sind oft notwendig.
:::

Das Training oder die Feinabstimmung eines Modells für Open Ticket AI umfasst mehrere Schlüsselschritte:

### 1. Datensammlung

*   **Historische Daten exportieren**: Sammeln Sie historische Ticketdaten (einschließlich Betreff und Text) aus Ihrem bestehenden Ticketsystem.
*   **Daten labeln**: Kennzeichnen Sie jedes Ticket genau mit der richtigen Warteschlange und Priorität. Dieser gelabelte Datensatz bildet die Grundlage für das Training Ihres Modells.

### 2. Datenbereinigung

*   **Rauschen entfernen**: Beseitigen Sie irrelevante Informationen wie E-Mail-Signaturen, personenbezogene Daten (PII) und Spam.
*   **Text normalisieren**: Standardisieren Sie Leerräume und stellen Sie eine konsistente Zeichenkodierung sicher.

### 3. Datentransformation & Tokenisierung

*   **Felder kombinieren**: Verketten Sie den Betreff und den Text der Tickets, um einen einzigen Eingabetext für das Modell zu bilden.
*   **`max_length` festlegen**: Wählen Sie eine geeignete `max_length` für die Tokenisierung (z. B. 256–512 Tokens), basierend auf der medianen Länge Ihrer Tickets. Dies verhindert das Abschneiden wichtiger Informationen und schont gleichzeitig die Rechenressourcen.
*   **Tokenizer verwenden**: Nutzen Sie den bereitgestellten `ticket_combined_email_tokenizer` oder einen Tokenizer, der mit dem von Ihnen gewählten Modell kompatibel ist.

### 4. Modellauswahl & Hardware

Berücksichtigen Sie bei der Auswahl eines Modells und der erforderlichen Hardware Folgendes:

| Modell                         | Benötigter RAM | Anmerkungen                   |
| ------------------------------ | -------------- | ----------------------------- |
| `distilbert-base-german-cased` | 2 GB           | Leichtgewichtig, deutscher Text |
| `bert-base-german-cased`       | 4 GB           | Höhere Genauigkeit, deutscher Text |
| `deberta-large-mnli`           | 8 GB           | Mehrsprachig / große Kontexte |

(*Hinweis: Die obige Tabelle enthält Beispiele; die tatsächlichen Anforderungen können abweichen.*)

### 5. Training & Feinabstimmung

*   **Hyperparameter-Abstimmung**: Verwenden Sie den integrierten Hyperparameter-Tuner, um mit Einstellungen wie `learning_rate`, `batch_size` und `epochs` zu experimentieren und die optimale Konfiguration für Ihren Datensatz zu finden.
*   **Leistung überwachen**: Das Trainingsskript gibt eine Zusammenfassung der Leistung und Ressourcennutzung des Modells aus, die Ihnen hilft, den Fortschritt zu verfolgen und Anpassungen vorzunehmen.

### 6. Evaluierung

*   **Genauigkeit messen**: Bewerten Sie die Leistung des Modells anhand seiner Genauigkeit bei der Vorhersage von Warteschlange und Priorität.
*   **Konfidenz analysieren**: Untersuchen Sie die Beziehung zwischen den Konfidenzwerten des Modells und der Korrektheit seiner Vorhersagen. Diese Analyse ist entscheidend für die Festlegung eines optimalen `confidence_threshold` in der Konfiguration.
*   **Konfidenzgewichteter Genauigkeitswert (CWAS)** (Optional): Sie könnten die Verwendung einer Metrik wie CWAS in Betracht ziehen, um eine differenziertere Sicht auf die Leistung zu erhalten:
    ```math
    \text{CWAS} = \text{Anteil vorhergesagt} \times (\text{Anteil korrekt}^2)
    ```
    Dieser Wert belohnt Modelle, die sowohl genau sind als auch einen hohen Prozentsatz an Vorhersagen treffen (d. h. sich bei Fällen mit geringer Konfidenz nicht übermäßig auf einen Standardwert zurückfallen lassen).