---
description: Hier finden Sie die offiziellen Hardware-Empfehlungen für Open Ticket AI.
  Dieser Leitfaden beschreibt die idealen Anforderungen an CPU, GPU und RAM, um Spitzenleistung
  für jedes Bereitstellungsszenario zu gewährleisten.
title: Hardware-Empfehlungen für Open Ticket AI
---
# Hardware-Empfehlungen

Die Auswahl geeigneter Hardware gewährleistet einen reibungslosen Betrieb von Open Ticket AI.

* **Nur-CPU**: Ausreichend für geringe Ticketvolumen und Modelle wie DistilBERT.
* **GPU**: Empfohlen für hohe Volumen oder bei der Verwendung größerer Modelle. Karten der NVIDIA RTX-Serie oder vergleichbare Cloud-Instanzen (z. B. Hetzner Matrix GPU, AWS `g4ad.xlarge`) funktionieren gut.

## Arbeitsspeicher (RAM)

Ungefährer RAM-Bedarf für die mitgelieferten Modelle:

| Modell               | RAM |
| -------------------- | --- |
| DistilBERT           | ~2 GB |
| BERT-base            | ~4 GB |

Stellen Sie sicher, dass zusätzlicher RAM für das Betriebssystem und das Ticketsystem zur Verfügung steht, wenn diese auf demselben Host laufen.

## Überlegungen zur Bereitstellung

* **Co-Location vs. separate Geräte**: Sie können Open Ticket AI auf demselben Server wie Ihr Ticketsystem oder auf einem separaten Rechner ausführen.
* **Netzwerkkonfiguration**: Wenn die Anwendung auf separaten Geräten läuft, passen Sie die `rest_settings.base_url` in der `config.yml` an, damit Ihr Ticketsystem die Anwendung erreichen kann.