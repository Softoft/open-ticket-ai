---
title: Configuring Open Ticket AI
description: How to configure Open Ticket AI using `config.yml`.
---

# Configuration

Open Ticket AI is configured using a `config.yml` file placed at the project root.

## `config.yml` Example

Below is an example structure of the `config.yml` file:

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

### Key Configuration Sections

*   **`system`**: Defines how Open Ticket AI connects to your ticket system.
    * `provider_key` – Which adapter implementation to use.
    * `params` – Connection details such as server address and credentials.
*   **`fetchers`**: Describe how tickets are retrieved from the system.
*   **`data_preparers`**: Specify how ticket text is combined or preprocessed before being sent to the model.
*   **`ai_inference_services`**: Configure the AI models.
    * `hf_model` – The Hugging Face model identifier.
    * `hf_token_env_var` – Name of the environment variable that stores your Hugging Face token.
*   **`modifiers`**: Update tickets with the prediction results.
    * Typical parameters include `confidence_threshold` and `low_confidence_value`.
*   **`attribute_predictors`**: Tie everything together. Each predictor references a fetcher, preparer, AI inference service and modifier and can define a schedule.

## Default Hugging Face Models

Out of the box, Open Ticket AI is set up to download and use pre-trained models. For basic operation, no fine-tuning is required for these models.

::: note
In Development, See Huggingface for latest models.
:::

*   `open-ticket-ai-queue-german-bert`
*   `open-ticket-ai-priority-german-bert`
*   `open-ticket-ai-priority-english-bert`
*   `open-ticket-ai-priority-multilingual-bert`

To use your own model:
1.  Set `hf_model: "<your-username>/<your-model-name>"` in the respective classifier configuration.
2.  Ensure your `hf_token` provides access to the model if it's private.
