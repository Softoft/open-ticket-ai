---
title: Konfiguration von Open Ticket AI
description: Wie man Open Ticket AI mit `config.yml` konfiguriert.
---

# Konfiguration

Open Ticket AI wird über eine `config.yml`-Datei konfiguriert, die im Projektstammverzeichnis liegt.

## Beispiel für `config.yml`

Nachfolgend ist eine Beispielstruktur der `config.yml`-Datei dargestellt:

```yaml
open_ticket_ai:
  # only one ticket-system adapter
  system:
    provider_key: "OTOBOAdapter"
    params:
      server_address: "http://18.193.56.84"
      webservice_name: "OTAI"
      search_operation_url: "ticket/search"
      update_operation_url: "ticket"
      get_operation_url: "ticket/get"
      username: "root@locallhost"
      password_env_var: "OTOBOPASS"
  fetchers:
    - id: "basic_ticket"
      provider_key: "BasicTicketFetcher"
      params:
        filters:
          - attribute: "queue"
            value: "incoming_queue"

  data_preparers:
    - id: "subject_body"
      provider_key: "SubjectBodyPreparer"
      params:
        subject_field: "subject"
        body_field: "body"
        repeat_subject: 3

  ai_inference_services:
    - id: "queue_model"
      provider_key: "HFAIInferenceService"
      params:
        hf_model: "open-ticket-ai/queue-classification-german-bert"
        hf_token_env_var: "HUGGINGFACE_TOKEN"

    - id: "priority_model"
      provider_key: "HFAIInferenceService"
      params:
        hf_model: "open-ticket-ai/priority-classification-german-bert"
        hf_token_env_var: "HUGGINGFACE_TOKEN"

  modifiers:
    - id: "queue_updater"
      provider_key: "QueueModifier"
      params:
        confidence_threshold: 0.8
        low_confidence_value: "unclassified"
    - id: "priority_updater"
      provider_key: "PriorityModifier"
      params:
        confidence_threshold: 0.6
        low_confidence_value: 3

  attribute_predictors:
    - id: "queue_classification"
      provider_key: "QueuePredictor"
      fetcher_id: "basic_ticket"
      preparer_id: "subject_body"
      ai_inference_service_id: "queue_model"
      modifier_id: "queue_updater"
      schedule:
        interval: 10
        unit: "seconds"
      params:
        ticket_system_value2model_values:
          otobo_queue1:
            - "IT & Technology/Security Operations"
          otobo_queue2:
            - "IT & Technology/Software Development"
          research_development:
            - "Science/*"
          misc:
            - "*"

    - id: "priority_classification"
      provider_key: "PriorityPredictor"
      fetcher_id: "basic_ticket"
      preparer_id: "subject_body"
      ai_inference_service_id: "priority_model"
      modifier_id: "priority_updater"
      schedule:
        interval: 10
        unit: "seconds"
      params:
        ticket_system_value2model_values:
          1: [ 1 ]
          2: [ 2 ]
          3: [ 3 ]
          4: [ 4 ]
          5: [ 5 ]

```

### Wichtige Konfigurationsabschnitte

*   **`system`**: Definiert die Verbindung zu Ihrem Ticket-System.
    * `provider_key` – Welche Adapter-Implementierung verwendet werden soll.
    * `params` – Verbindungsdetails wie Serveradresse und Anmeldeinformationen.
*   **`fetchers`**: Beschreiben, wie Tickets aus dem System abgerufen werden.
*   **`data_preparers`**: Legen fest, wie Ticketdaten für die Modellverarbeitung vorbereitet werden.
*   **`ai_inference_services`**: Konfigurieren die KI-Modelle.
    * `hf_model` – Hugging Face Modellkennung.
    * `hf_token_env_var` – Umgebungsvariable für Hugging Face Token.
*   **`modifiers`**: Aktualisieren Tickets mit Vorhersageergebnissen.
    * Typische Parameter: `confidence_threshold` und `low_confidence_value`.
*   **`attribute_predictors`**: Verknüpfen alle Komponenten. Referenzieren Fetcher, Preparer, KI-Service und Modifier, inklusive Zeitplan.

## Standard Hugging Face Modelle

Open Ticket AI verwendet standardmäßig vortrainierte Modelle. Für Basisfunktionalität ist kein Fine-Tuning erforderlich.

::: note
In Entwicklung. Siehe Huggingface für aktuelle Modelle.
:::

*   `open-ticket-ai-queue-german-bert`
*   `open-ticket-ai-priority-german-bert`
*   `open-ticket-ai-priority-english-bert`
*   `open-ticket-ai-priority-multilingual-bert`

So verwenden Sie eigene Modelle:
1.  Setzen Sie `hf_model: "<Ihr-Benutzername>/<Ihr-Modellname>"` in der jeweiligen Klassifikatorkonfiguration.
2.  Stellen Sie sicher, dass Ihr `hf_token` bei privaten Modellen Zugriff gewährt.