---
title: Hardware-Empfehlungen für Open Ticket AI
description: Anleitung zur Hardware für den Betrieb von Open Ticket AI.
---

# Hardware-Empfehlungen

Die Wahl der richtigen Hardware ist entscheidend für die Leistung von Open Ticket AI, insbesondere bei hohem Ticketaufkommen oder bei Verwendung komplexerer Modelle.

*   **Nur CPU**: Ausreichend für geringe Ticketmengen (z. B. < 50 Tickets pro Minute). Die meisten modernen Server-CPUs bewältigen diese Last.
*   **GPU (Grafikprozessor)**: Empfohlen für höhere Volumen (z. B. > 100 Tickets pro Minute) oder bei rechenintensiven Modellen. NVIDIA-RTX-Serie-GPUs sind gängige Wahl.
    *   **Beispiele**:
        *   Hetzner Matrix GPU (meist mit großzügigem vRAM)
        *   AWS-`g4ad.xlarge`-Instanz oder ähnliche Cloud-GPU-Instanzen.

## Arbeitsspeicher (RAM)

Stellen Sie ausreichend RAM für die verwendeten Modelle bereit. RAM-Anforderungen für spezifische Modelle finden Sie im Abschnitt [Training des Modells](./training-models.md#4-model-selection-hardware).

*   Für Standard-BERT-Modelle sind mindestens 4GB RAM für das Modell erforderlich, plus zusätzlicher RAM für Betriebssystem und Ticketsystem bei gemeinsamer Host-Nutzung.

## Bereitstellungsüberlegungen

*   **Co-Location vs. separate Geräte**: Open Ticket AI kann auf demselben Server wie Ihr Ticketsystem oder separat betrieben werden.
*   **Netzwerkkonfiguration**: Bei getrennter Ausführung muss die Netzwerkkonfiguration Kommunikation zwischen Open Ticket AI und Ihrem Ticketsystem ermöglichen. Passen Sie die `rest_settings` (insbesondere `base_url`) in Ihrer `config.yml` an, um auf die korrekte Netzwerkadresse der API Ihres Ticketsystems zu verweisen.