---
description: 'Erfahren Sie, wie Sie benutzerdefinierte Modelle für Open Ticket AI trainieren und feinabstimmen. Diese Anleitung beschreibt den externen Arbeitsablauf: Daten exportieren, ein Modell trainieren und Ihre Konfiguration aktualisieren.'
title: Modelle trainieren
---
# Modelle trainieren

Open Ticket AI bietet keine In-App-Benutzeroberfläche oder API für das Modelltraining. Stattdessen trainieren Sie Modelle extern und verweisen dann in Ihrer Konfiguration auf sie.

## Überblick über den Arbeitsablauf

1. **Kategorisierte Tickets exportieren**
   Exportieren Sie Ticket-Texte mit ihren Warteschlangen- und Prioritäts-Kategorisierungen aus Ihrem Helpdesk.
2. **Ein Modell feinabstimmen**
   Verwenden Sie ein Tool wie ein Jupyter Notebook mit der `transformers`-Bibliothek, um ein Sprachmodell mit diesen Daten zu trainieren oder feinabzustimmen.
3. **Das Modell veröffentlichen oder speichern**
   Laden Sie das resultierende Modell in den Hugging Face Hub hoch oder speichern Sie es lokal, damit Open Ticket AI darauf zugreifen kann.
4. **Die Konfiguration aktualisieren**
   Bearbeiten Sie `config.yml` und setzen Sie den `model_name` (oder `hf_model`) jeder Pipeline auf den Speicherort Ihres neuen Modells. Starten Sie die Anwendung neu, um es zu laden.