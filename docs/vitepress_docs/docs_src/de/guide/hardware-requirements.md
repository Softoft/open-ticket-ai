---
title: Hardware-Empfehlungen für Open Ticket AI
description: Leitfaden zur Hardware für den Betrieb von Open Ticket AI.
---

# Hardware-Empfehlungen

Die Wahl der richtigen Hardware ist entscheidend für die Leistung von Open Ticket AI, insbesondere bei hohem Ticketaufkommen oder bei Verwendung komplexerer Modelle.

*   **CPU-only**: Ausreichend für geringes Ticketvolumen (z. B. < 50 Tickets pro Minute). Die meisten modernen Server-CPUs sollten diese Last bewältigen.
*   **GPU (Graphics Processing Unit)**: Empfohlen für höhere Volumen (z. B. > 100 Tickets pro Minute) oder bei rechenintensiven Modellen. NVIDIA-RTX-Serie-GPUs sind eine gängige Wahl.
    *   **Beispiele**:
        *   Hetzner Matrix GPU (typischerweise mit ausreichend vRAM)
        *   AWS `g4ad.xlarge`-Instanz oder ähnliche Cloud-GPU-Instanzen

## Arbeitsspeicher (RAM)

Stellen Sie ausreichend RAM für die verwendeten Modelle bereit. Konsultieren Sie den Abschnitt [Modelltraining](./training-models.md#4-model-selection-hardware) für spezifische RAM-Anforderungen.

*   Für Standard-BERT-Modelle werden mindestens 4 GB RAM für das Modell benötigt, plus zusätzlicher Speicher für Betriebssystem und Ticketsystem bei gemeinsamer Nutzung desselben Hosts.

## Bereitstellungsüberlegungen

*   **Gemeinsame vs. getrennte Bereitstellung**: Open Ticket AI kann auf demselben Server wie Ihr Ticketsystem oder auf separater Hardware laufen.
*   **Netzwerkkonfiguration**: Bei getrennter Bereitstellung muss die Kommunikation zwischen Open Ticket AI und Ihrem Ticketsystem gewährleistet sein. Passen Sie dazu `rest_settings` (insbesondere `base_url`) in Ihrer `config.yml` an die Netzwerkadresse der Ticketsystem-API an.