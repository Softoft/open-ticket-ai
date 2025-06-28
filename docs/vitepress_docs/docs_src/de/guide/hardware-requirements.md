---
title: Hardware-Empfehlungen für Open Ticket AI
description: Leitfaden zur Hardware für den Betrieb von Open Ticket AI.
---

# Hardware-Empfehlungen

Die Wahl der richtigen Hardware ist wichtig für die Leistung von Open Ticket AI, insbesondere bei einem großen Ticketaufkommen oder bei der Verwendung komplexerer Modelle.

*   **Nur CPU**: Ausreichend für geringe Ticketvolumen (z. B. < 50 Tickets pro Minute). Die meisten modernen Server-CPUs sollten diese Arbeitslast bewältigen können.
*   **GPU (Graphics Processing Unit)**: Empfohlen für höhere Volumen (z. B. > 100 Tickets pro Minute) oder bei der Verwendung größerer, rechenintensiverer Modelle. GPUs der NVIDIA RTX-Serie sind eine gängige Wahl.
    *   **Beispiele**:
        *   Hetzner Matrix GPU (die typischerweise mit reichlich vRAM ausgestattet ist)
        *   AWS `g4ad.xlarge`-Instanz oder ähnliche Cloud-GPU-Instanzen.

## Arbeitsspeicher (RAM)

Stellen Sie sicher, dass Sie genügend RAM für die Modelle zur Verfügung haben, die Sie verwenden möchten. Beispiele für RAM-Anforderungen für bestimmte Modelle finden Sie im Abschnitt [Training des Modells](./training-models.md#4-model-selection-hardware).

*   Für die standardmäßigen BERT-Modelle benötigen Sie in der Regel mindestens 4 GB RAM für das Modell, plus zusätzlichen RAM für das Betriebssystem und das Ticketsystem selbst, wenn diese auf demselben Host laufen.

## Überlegungen zur Bereitstellung

*   **Co-Location vs. separate Geräte**: Sie können Open Ticket AI auf demselben Server wie Ihr Ticketsystem oder auf einer separaten Maschine ausführen.
*   **Netzwerkkonfiguration**: Wenn Sie die Anwendung auf separaten Geräten ausführen, stellen Sie sicher, dass Ihre Netzwerkkonfiguration die Kommunikation zwischen Open Ticket AI und Ihrem Ticketsystem ermöglicht. Sie müssen die `rest_settings` (insbesondere die `base_url`) in Ihrer `config.yml` anpassen, damit sie auf die korrekte Netzwerkadresse der API Ihres Ticketsystems verweist.