```markdown
---
title: Training von KI-Modellen für Open Ticket AI
description: Anleitung zum Trainieren oder Feinabstimmen von Modellen für Open Ticket AI.
---

# Training des Modells

:::note
Sie müssen nur dann ein eigenes Modell trainieren, wenn Sie ein benutzerdefiniertes Modell verwenden oder die Standardmodelle feinabstimmen möchten. Um gute Ergebnisse zu erzielen, ist eine erhebliche Menge an Trainingsdaten erforderlich – idealerweise mindestens 1000 Tickets pro Warteschlange und Priorität. Datenbereinigung, Normalisierung, Tokenisierung und Experimente mit verschiedenen Modellen und Hyperparametern sind oft notwendig.
:::

Das Training oder Feinabstimmen eines Modells für Open Ticket AI umfasst mehrere Schritte:

### 1. Datenerfassung

*   **Historische Daten exportieren**: Sammeln Sie historische Ticketdaten (einschließlich Betreff und Text) aus Ihrem bestehenden Ticketsystem.
*   **Daten beschriften**: Versehen Sie jedes Ticket präzise mit der korrekten Warteschlange und Priorität. Dieser beschriftete Datensatz bildet die Grundlage für das Modelltraining.

### 2. Datenbereinigung

*   **Rauschen entfernen**: Entfernen Sie irrelevante Informationen wie E-Mail-Signaturen, personenbezogene Daten (PII) und Spam.
*   **Text normalisieren**: Standardisieren Sie Leerzeichen und stellen Sie konsistente Zeichenkodierungen sicher.

### 3. Datentransformation & Tokenisierung

*   **Felder kombinieren**: Verknüpfen Sie den Betreff und den Text der Tickets zu einem einzigen Eingabetext für das Modell.
*   **`max_length` festlegen**: Wählen Sie eine geeignete `max_length` für die Tokenisierung (z. B. 256–512 Token) basierend auf der medianen Länge Ihrer Tickets. Dies verhindert das Abschneiden wichtiger Informationen bei gleichzeitiger Verwaltung der Rechenressourcen.
*   **Tokenizer verwenden**: Nutzen Sie den bereitgestellten `ticket_combined_email_tokenizer` oder einen mit Ihrem gewählten Modell kompatiblen Tokenizer.

### 4. Modellauswahl & Hardware

Berücksichtigen Sie bei der Auswahl eines Modells und der erforderlichen Hardware Folgendes:

| Modell                          | Benötigter RAM | Hinweise                         |
| ------------------------------ | -------------- | -------------------------------- |
| `distilbert-base-german-cased` | 2 GB           | Leichtgewicht, deutscher Text    |
| `bert-base-german-cased`       | 4 GB           | Höhere Genauigkeit, deutscher Text |
| `deberta-large-mnli`           | 8 GB           | Mehrsprachig / große Kontexte    |

(*Hinweis: Die Tabelle dient als Beispiel; tatsächliche Anforderungen können variieren.*)

### 5. Training & Feinabstimmung

*   **Hyperparameter-Abstimmung**: Verwenden Sie den integrierten Hyperparameter-Tuner, um mit Einstellungen wie `learning_rate`, `batch_size` und `epochs` zu experimentieren und die optimale Konfiguration für Ihren Datensatz zu finden.
*   **Leistung überwachen**: Das Trainingsskript gibt eine Zusammenfassung der Modellleistung und Ressourcennutzung aus, was Ihnen hilft, den Fortschritt zu verfolgen und Anpassungen vorzunehmen.

### 6. Evaluation

*   **Genauigkeit messen**: Bewerten Sie die Modellleistung anhand der Genauigkeit bei der Vorhersage von Warteschlange und Priorität.
*   **Konfidenz analysieren**: Untersuchen Sie den Zusammenhang zwischen den Konfidenzwerten des Modells und der Richtigkeit seiner Vorhersagen. Diese Analyse ist entscheidend für die Festlegung eines optimalen `confidence_threshold` in der Konfiguration.
*   **Konfidenzgewichteter Genauigkeitswert (CWAS)** (Optional): Sie könnten eine Metrik wie CWAS verwenden, um eine differenziertere Leistungsbewertung zu erhalten:
    ```math
    \text{CWAS} = \text{percent_predicted} \times (\text{percent_correct}^2)
    ```
    Dieser Wert belohnt Modelle, die sowohl präzise sind als auch einen hohen Anteil an Vorhersagen treffen (d. h. nicht übermäßig auf Standardrückfälle bei niedriger Konfidenz angewiesen sind).
```