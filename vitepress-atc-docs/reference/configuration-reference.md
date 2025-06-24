---
title: Configuring Open Ticket AI
description: How to configure Open Ticket AI using run_config.yaml.
---

# Configuration

Open Ticket AI is configured using a `run_config.yaml` file placed at the project root.

## `run_config.yaml` Example

Below is an example structure of the `run_config.yaml` file:

```yaml
run_config:
  hf_token: "your_huggingface_token_here" # Your Hugging Face API token

  ticket_classifiers:
    queue_classification:
      tokenizer: "ticket_combined_email_tokenizer"
      hf_model: "google/flan-t5-base" # Hugging Face model for queue classification
      ticket_attribute: "queue_id" # Ticket attribute to store the queue
      confidence_threshold: 0.5 # Minimum confidence to assign a queue
      low_confidence_value: "misc" # Queue for low-confidence predictions
      ticket_to_model_results_map: # Mapping from model output to your ticket system queues
        - otobo_queue1:
            - "IT & Technology/Security Operations"
        - otobo_queue2:
            - "IT & Technology/Software Development"
        - research_development:
            - "Science/*" # Wildcard matching
        - misc:
            - "*" # Default catch-all

    priority_classification:
      tokenizer: "ticket_combined_email_tokenizer"
      hf_model: "google/flan-t5-base" # Hugging Face model for priority classification
      ticket_attribute: "priority" # Ticket attribute to store the priority
      ticket_to_model_results_map: # Mapping from model output to your priority levels
        - 1: [1]
        - 2: [2]
        - 3: [3]
        - 4: [4]
        - 5: [5]

  ticket_system_adapter:
    system_name: "otobo" # Name of your ticket system (e.g., otobo, zammad)
    rest_settings:
      base_url: "https://your-otobo-instance.com" # Base URL of your ticket system's API
      username: "your_username"
      password: "your_password"
      search_url: "/api/v1/ticket/search" # API endpoint for searching tickets
      get_url:    "/api/v1/ticket/get"    # API endpoint for fetching a ticket
      update_url: "/api/v1/ticket/update"  # API endpoint for updating a ticket
    incoming_queue: "otobo_queue1" # The queue from which to fetch new tickets
```

### Key Configuration Sections:

*   `hf_token`: Your personal Hugging Face access token, required for downloading models.
*   `ticket_classifiers`: Defines the behavior for different classification tasks (e.g., queue, priority).
    *   `tokenizer`: Specifies the tokenizer to be used.
    *   `hf_model`: The Hugging Face model identifier.
    *   `ticket_attribute`: The field in your ticket system where the prediction will be stored.
    *   `confidence_threshold` (for queue_classification): If the model's confidence is below this threshold, the `low_confidence_value` is used.
    *   `low_confidence_value` (for queue_classification): The queue assigned when confidence is low.
    *   `ticket_to_model_results_map`: A crucial mapping that translates the raw output of the AI model to the specific queue names or priority levels used in your ticket system. Wildcards (`*`) can be used for broader matching.
*   `ticket_system_adapter`: Configures how Open Ticket AI interacts with your specific ticket system.
    *   `system_name`: Identifies the type of ticket system.
    *   `rest_settings`: Contains the API endpoint details and credentials.
    *   `incoming_queue`: The specific queue in your ticket system that Open Ticket AI will monitor for new tickets to process.

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
