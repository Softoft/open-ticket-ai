---
description: Meistern Sie die KI-Ticket-Klassifizierung mit diesem Leitfaden zur Evaluierung.
  Erfahren Sie, warum Genauigkeit bei unausgeglichenen Daten irreführend ist, und
  entdecken Sie die wesentlichen Metriken, die wirklich zählen, einschließlich Precision,
  Recall, F1-Score und Multi-Label-Strategien.
---
# Evaluierung von KI-Klassifikatoren für reale Ticket-Daten: Die entscheidenden Metriken

## Einleitung

Support-Ticket-Daten sind unstrukturiert und oft stark auf wenige gängige Kategorien konzentriert. Beispielsweise könnten 80 % der Tickets als **„allgemeine Anfrage“** gekennzeichnet sein, was Klassifikatoren zugunsten der Mehrheitsklasse verzerrt. In der Praxis kann ML für Ticket-Daten für folgende Zwecke eingesetzt werden:

- **Prioritätsvorhersage** (z. B. Kennzeichnung dringender Anliegen)
- **Zuweisung zu Warteschlangen oder Teams** (z. B. Weiterleitung von Rechnungsfragen an die Finanzabteilung)
- **Absichts- oder Themenklassifizierung** (z. B. „Feature-Request“ vs. „Bug-Report“)

Diese Anwendungsfälle zeigen, warum die Evaluierung eine Herausforderung darstellt: Reale Ticket-Datensätze sind Multi-Class und Multi-Label, mit verrauschtem Text und **unausgeglichenen Klassen**:contentReference[oaicite:0]{index=0}. Ein naives Modell, das immer die Mehrheitsklasse vorhersagt, kann dennoch eine hohe Genauigkeit (Accuracy) erzielen, indem es seltene, aber wichtige Fälle ignoriert. Wir werden untersuchen, warum die Genauigkeit allein irreführend ist, und die Metriken erörtern, die wirklich von Bedeutung sind.

## Warum Genauigkeit (Accuracy) irreführend ist

**Accuracy** (Genauigkeit) ist definiert als die Gesamtzahl der korrekten Vorhersagen geteilt durch alle Vorhersagen:
$ \text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN} $
In Formelschreibweise: Accuracy = (TP + TN) / (alle Samples). Obwohl einfach, versagt die Accuracy bei unausgeglichenen Daten erheblich. Wenn beispielsweise 80 % der Tickets zur Klasse A gehören, erreicht ein einfacher Klassifikator, der *immer* A vorhersagt, standardmäßig eine Accuracy von 80 % – ignoriert dabei aber die anderen 20 % der Tickets vollständig. In Extremfällen (z. B. bei einer Klassenverteilung von 99 % zu 1 %) führt die ständige Vorhersage der Mehrheitsklasse zu einer Accuracy von 99 %, obwohl kein echtes Lernen stattgefunden hat. Kurz gesagt, eine hohe Accuracy kann lediglich die Klassenverteilung widerspiegeln, nicht die tatsächliche Leistung.

> **„… Accuracy ist kein geeignetes Maß mehr [für unausgeglichene Datensätze], da sie nicht zwischen der Anzahl korrekt klassifizierter Beispiele verschiedener Klassen unterscheidet. Daher kann sie zu fehlerhaften Schlussfolgerungen führen …“.**

## Kernmetriken: Precision, Recall, F1-Score

Um Klassifikatoren bei unausgeglichenen Daten zu bewerten, stützen wir uns auf **Precision, Recall und den F1-Score**, die sich auf Fehler in den Minderheitsklassen konzentrieren. Diese werden aus der Konfusionsmatrix abgeleitet, z. B. für eine binäre Klassifizierung:

|                         | Vorhergesagt Positiv                  | Vorhergesagt Negativ                  |
|-------------------------|---------------------------------------|---------------------------------------|
| **Tatsächlich Positiv**  | Richtig Positiv (True Positive, TP)   | Falsch Negativ (False Negative, FN)   |
| **Tatsächlich Negativ** | Falsch Positiv (False Positive, FP)   | Richtig Negativ (True Negative, TN)   |

Aus diesen Zählungen definieren wir:

- **Precision** (Präzision) = TP / (TP + FP) – der Anteil der positiven Vorhersagen, die korrekt sind.
- **Recall** (Trefferquote) = TP / (TP + FN) – der Anteil der tatsächlich positiven Fälle, die gefunden wurden.
- **F1-Score** = das harmonische Mittel aus Precision und Recall:
  \[ \mathrm{F1} = \frac{2 \cdot \mathrm{TP}}{2 \cdot \mathrm{TP} + \mathrm{FP} + \mathrm{FN}}. \]

Jede Metrik hebt unterschiedliche Fehler hervor: Precision bestraft Fehlalarme (FP), während Recall übersehene Fälle (FN) bestraft. Der F1-Score gleicht beide aus. Der Vollständigkeit halber sei erwähnt, dass die Accuracy auch als \( (TP + TN) / (TP+TN+FP+FN) \) geschrieben werden kann:contentReference[oaicite:8]{index=8}, aber bei unausgeglichenen Daten verdeckt sie die Schwächen des Modells.

In der Praxis berechnet der `classification_report` von scikit-learn diese Metriken für jede Klasse. Zum Beispiel:

gibt Precision, Recall, F1-Score (und Support) für jede Ticket-Klasse aus.

## Macro- vs. Micro-Averaging

Bei Multi-Class-Problemen können Metriken auf unterschiedliche Weise gemittelt werden. **Micro-Averaging** fasst alle Klassen zusammen, indem globale TP, FP und FN summiert und dann die Metriken berechnet werden – was einer Gewichtung nach dem Support jeder Klasse entspricht. **Macro-Averaging** berechnet die Metrik für jede Klasse separat und bildet dann den ungewichteten Mittelwert. Mit anderen Worten, Macro-Averaging behandelt alle Klassen gleich (sodass seltene Klassen genauso viel zählen wie häufige), während Micro-Averaging die Leistung bei häufigen Klassen bevorzugt. Verwenden Sie **Macro-Averaging**, wenn Minderheitsklassen kritisch sind (z. B. das Erkennen eines seltenen, dringenden Tickets), und **Micro-Averaging**, wenn die Gesamtgenauigkeit über alle Tickets hinweg wichtiger ist.

| Mittelung | Berechnungsmethode                                                  | Anwendungsfall                                                     |
|-----------|---------------------------------------------------------------------|--------------------------------------------------------------------|
| **Micro** | Globale Zählung von TP, FP, FN über alle Klassen                    | Gibt die Gesamtleistung an (bevorzugt große Klassen)               |
| **Macro** | Mittelwert der Metrik jeder Klasse (jede Klasse gleich gewichtet)   | Stellt sicher, dass kleine/seltene Klassen gleich gewichtet werden |

## Herausforderungen bei Multi-Label-Klassifizierung

Helpdesk-Tickets haben oft mehrere Labels gleichzeitig (z. B. kann ein Ticket sowohl ein **Warteschlangen**- als auch ein **Prioritäts**-Label haben). In Multi-Label-Szenarien kommen zusätzliche Metriken zur Anwendung:

*   **Subset Accuracy** (Exakte Übereinstimmung) – der Anteil der Samples, bei denen *alle* vorhergesagten Labels exakt mit dem wahren Satz von Labels übereinstimmen. Dies ist sehr streng: Ein falsches Label bedeutet einen Fehlschlag.
*   **Hamming Loss** (Hamming-Verlust) – der Anteil der einzelnen Label-Vorhersagen, die falsch sind. Der Hamming Loss ist nachsichtiger: Jedes Label wird unabhängig bewertet. Ein niedrigerer Hamming Loss (nahe 0) ist besser.
*   **Label Ranking Loss** – misst, wie viele Label-Paare fälschlicherweise nach Konfidenz geordnet sind. Dies ist relevant, wenn das Modell Scores für jedes Label ausgibt und uns die Rangfolge der Labels für jedes Ticket wichtig ist.

Scikit-learn bietet Funktionen wie `accuracy_score` (Subset Accuracy im Multi-Label-Modus) und `hamming_loss`. Im Allgemeinen wählt man die Metrik, die den Geschäftsanforderungen entspricht: exakte Übereinstimmung, wenn alle Labels korrekt sein müssen, oder Hamming/Ranking Loss, wenn eine teilweise Korrektheit akzeptabel ist.

## Die Konfusionsmatrix in der Praxis

Eine Konfusionsmatrix ist oft der erste Schritt zur Analyse des Verhaltens eines Klassifikators. In Python können Sie sie mit scikit-learn berechnen und anzeigen:

```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_test, y_pred, labels=classes)
print("Confusion Matrix:\n", cm)

# To visualize:
ConfusionMatrixDisplay(cm, display_labels=classes).plot()
```

Hier ist `cm[i, j]` die Anzahl der Tickets, deren wahre Klasse `i` ist, die aber als Klasse `j` vorhergesagt wurden. Achten Sie bei der Untersuchung einer Konfusionsmatrix (oder ihrer Heatmap) auf Folgendes:

*   **Zellen außerhalb der Diagonalen** – diese deuten auf Fehlklassifizierungen hin (welche Klassen am häufigsten verwechselt werden).
*   **Falsch-Positive vs. Falsch-Negative** – z. B. bedeutet eine hohe Summe in einer Zeile außerhalb der Diagonalen, dass das Modell diese tatsächliche Klasse häufig übersehen hat (viele FNs); eine hohe Summe in einer Spalte außerhalb der Diagonalen bedeutet viele falsche Vorhersagen dieser Klasse (FPs).
*   **Unterrepräsentierte Klassen** – Klassen mit wenigen Beispielen können als fast leere Zeilen/Spalten erscheinen, was darauf hindeutet, dass das Modell sie selten korrekt vorhersagt.

Eine sorgfältige Analyse der Konfusionsmatrix hilft dabei, die Datenbereinigung oder Modellanpassungen für bestimmte Ticket-Typen gezielt vorzunehmen.

## Evaluierungsstrategie für reale Ticket-Systeme

Der Aufbau einer zuverlässigen Evaluierungs-Pipeline erfordert mehr als nur die Auswahl von Metriken:

*   **Saubere, gelabelte Daten**: Stellen Sie sicher, dass Ihr Testdatensatz repräsentativ und korrekt gelabelt ist. Entfernen Sie Duplikate oder falsch gelabelte Tickets vor der Evaluierung.
*   **Baseline vs. Feinabstimmung**: Vergleichen Sie Ihr KI-Modell immer mit einfachen Baselines (z. B. einem Mehrheitsklassen-Prädiktor oder Keyword-basierten Regelsystemen). Messen Sie relative Verbesserungen anhand der ausgewählten Metriken.
*   **Regelmäßige Neubewertung**: Ticket-Trends ändern sich im Laufe der Zeit (saisonale Probleme, neue Produkte). Planen Sie, das Modell regelmäßig neu zu trainieren und zu bewerten oder dies bei Daten-Drift auszulösen.
*   **Kommunikation mit Stakeholdern**: Übersetzen Sie Metriken in handlungsorientierte Erkenntnisse für nicht-technische Stakeholder. Zum Beispiel: „Der Recall für dringende Tickets stieg von 75 % auf 85 %, was bedeutet, dass wir 10 % mehr hochpriore Anliegen automatisch erfassen.“ Verwenden Sie Diagramme (z. B. Balkendiagramme für Precision/Recall pro Klasse) und betonen Sie die geschäftlichen Auswirkungen (schnellere Antworten, reduzierte Rückstände).

## Fazit

Zusammenfassend lässt sich sagen: **Was man nicht misst, kann man nicht verbessern**. Accuracy allein reicht für unausgeglichene, komplexe Ticket-Daten nicht aus. Verfolgen Sie stattdessen klassenweise Precision, Recall und den F1-Score (unter Verwendung von Macro-/Micro-Averages, wo sinnvoll) und ziehen Sie Multi-Label-Metriken in Betracht, wenn Ihre Tickets mehrere Annotationen haben. Beginnen Sie frühzeitig mit dem Tracking von Metriken bei jeder KI-Integration, damit Gewinne (oder Probleme) sichtbar werden. Indem sich Support-Teams von Anfang an auf die richtigen Metriken konzentrieren, können sie ihre Ticket-Klassifikatoren iterativ verbessern und eine zuverlässigere Automatisierung bereitstellen.

Möchten Sie diese Ideen mit Ihren eigenen Daten ausprobieren? Besuchen Sie die [Open Ticket AI Demo](https://open-ticket-ai.com)-Plattform, um mit echten Ticket-Datensätzen und integrierten Evaluierungs-Tools zu experimentieren.