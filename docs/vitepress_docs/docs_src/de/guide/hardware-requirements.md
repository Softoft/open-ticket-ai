---
description: Stellen Sie die optimale Leistung von Open Ticket AI mit der richtigen Hardware sicher. Dieser Leitfaden beschreibt die Anforderungen an CPU, NVIDIA GPU und RAM für jedes Ticketaufkommen und jede Bereitstellung.
title: Hardware-Empfehlungen für Open Ticket AI
---
# Hardware-Empfehlungen

Die Wahl der richtigen Hardware ist wichtig für die Leistung von Open Ticket AI, insbesondere bei einem großen Ticketaufkommen oder bei der Verwendung komplexerer Modelle.

*   **Nur-CPU**: Ausreichend für ein geringes Ticketaufkommen (z. B. < 50 Tickets pro Minute). Die meisten modernen Server-CPUs sollten diese Arbeitslast bewältigen können.
*   **GPU (Graphics Processing Unit)**: Empfohlen für ein höheres Aufkommen (z. B. > 100 Tickets pro Minute) oder bei der Verwendung größerer, rechenintensiverer Modelle. GPUs der NVIDIA RTX-Serie sind eine gängige Wahl.
    *   **Beispiele**:
        *   Hetzner Matrix GPU (die typischerweise mit reichlich vRAM ausgestattet ist)
        *   AWS `g4ad.xlarge`-Instanz oder ähnliche Cloud-GPU-Instanzen.

## Arbeitsspeicher (RAM)

Stellen Sie sicher, dass Sie genügend RAM für die Modelle zur Verfügung haben, die Sie verwenden möchten. Beispiele für RAM-Anforderungen für spezifische Modelle finden Sie im Abschnitt [Training des Modells](./training-models.md#4-model-selection-hardware).

*   Für die Standard-BERT-Modelle benötigen Sie in der Regel mindestens 4 GB RAM, die für das Modell dediziert sind, zuzüglich zusätzlichem RAM für das Betriebssystem und das Ticketsystem selbst, wenn diese auf demselben Host ausgeführt werden.

## Überlegungen zur Bereitstellung

*   **Gemeinsamer Host vs. getrennte Geräte**: Sie können Open Ticket AI auf demselben Server wie Ihr Ticketsystem oder auf einem separaten Rechner ausführen.
*   **Netzwerkkonfiguration**: Wenn Sie die Systeme auf getrennten Geräten ausführen, stellen Sie sicher, dass Ihre Netzwerkkonfiguration die Kommunikation zwischen Open Ticket AI und Ihrem Ticketsystem ermöglicht. Sie müssen die `rest_settings` (insbesondere die `base_url`) in Ihrer `config.yml` anpassen, sodass sie auf die korrekte Netzwerkadresse der API Ihres Ticketsystems verweist.