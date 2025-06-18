# Open Ticket AI

**Open Ticket AI** is an on-premise, extensible framework for AI-powered ticket classification and prioritization. It supports major open-source ticket systems (OTOBO, Znuny, Zammad, and more), ensuring full data privacy and seamless integration via REST APIs.

---

## Table of Contents

- [Introduction](#introduction)  
  - [Problem Statement](#problem-statement)  
  - [Solution Overview](#solution-overview)  
  - [Prerequisites](#prerequisites)  
- [Supported Ticket Systems](#supported-ticket-systems)  
- [Features](#features)  
- [Architecture](#architecture)  
  - [Pipeline & Value Objects](#pipeline--value-objects)  
- [Installation](#installation)  
- [Configuration](#configuration)  
  - [`run_config.yaml`](#run_configyaml)  
  - [Default Hugging Face Models](#default-hugging-face-models)  
- [Training the Model](#training-the-model)  
  - [1. Data Collection](#1-data-collection)  
  - [2. Data Cleaning](#2-data-cleaning)  
  - [3. Data Transformation & Tokenization](#3-data-transformation--tokenization)  
  - [4. Model Selection & Hardware](#4-model-selection--hardware)  
  - [5. Training & Fine-Tuning](#5-training--fine-tuning)  
  - [6. Evaluation](#6-evaluation)  
- [Usage](#usage)  
  - [Collect Tickets](#collect-tickets)  
  - [Train Your Models](#train-your-models)  
  - [Run Inference](#run-inference)  
- [Hardware Recommendations](#hardware-recommendations)  
- [Cost–Benefit Analysis](#cost–benefit-analysis)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Introduction

### Problem Statement

Most organizations receive large volumes of text-based tickets (email, chat, forms) that require manual queue assignment and prioritization—an error-prone and time-consuming process. Without 24/7 staffing, critical tickets can sit unattended, breaching SLAs and risking customer satisfaction.

### Solution Overview

Open Ticket AI uses fine-tuned transformer models to automatically:

- Predict **Queue** (which team or department should handle it)  
- Predict **Priority** (how urgently it must be processed)  
- Optionally **answer** simple tickets via a built-in chatbot  

All processing runs **on-premise**, ensuring no sensitive data leaves your environment.

### Prerequisites

- Linux server (Debian/Ubuntu/CentOS)  
- Docker & Docker Compose  
- Python 3.8+  
- A Hugging Face token (for model downloads and custom models)  

---

## Supported Ticket Systems

Open Ticket AI provides out-of-the-box adapters for:

- **OTOBO** (including Znuny / OTRS-derivatives)  
- **Zammad**  
- **Other REST-based systems** (Jira, ServiceNow, custom APIs)  

Adapters use each system’s REST API to fetch, update and move tickets between queues.

---

## Features

- **Queue Classification** (e.g. IT, Accounting, Sales)  
- **Priority Prediction** (numerical 1–5 or continuous 0–100)  
- **Low-confidence Handling**: route uncertain tickets to a review queue  
- **Multi-language Support**: German, English, Multilingual  
- **On-Premise Deployment**: Dockerized; no external data sharing  
- **Extensible Pipelines**: add custom Value Objects (e.g. SLA, tags)  
- **Built-in Hyperparameter Tuner** for optimal model performance  
- **Optional Chatbot Module** to auto-respond to FAQs  

---

## Architecture

### Pipeline & Value Objects

```

\[ Incoming Ticket ]
↓
\[ Preprocessor ] — cleans & merges subject+body
↓
\[ Transformer Tokenizer ]
↓
\[ Queue Classifier ] → Queue ID + confidence
↓
\[ Priority Classifier ] → Priority score + confidence
↓
\[ Postprocessor ] — applies thresholds, routes or flags
↓
\[ Ticket System Adapter ] — updates ticket via REST API

```

Each stage consumes and produces **Value Objects** (e.g. `subject`, `body`, `queue_id`, `priority`), making the pipeline modular and easy to extend.

---

## Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-org/open-ticket-ai.git
   cd open-ticket-ai
   ```

2. **Create a `run_config.yaml`** (see [Configuration](#configuration))

3. **Start with Docker Compose**

   ```bash
   docker-compose up -d --build
   ```

4. **Monitor logs**

   ```bash
   docker-compose logs -f
   ```

---

## Configuration

Place your settings in `run_config.yaml` at the project root:

```yaml
run_config:
  hf_token: "your_huggingface_token_here"

  ticket_classifiers:
    queue_classification:
      tokenizer: "ticket_combined_email_tokenizer"
      hf_model: "google/flan-t5-base"
      ticket_attribute: "queue_id"
      confidence_threshold: 0.5
      low_confidence_value: "misc"
      ticket_to_model_results_map:
        - otobo_queue1:
            - "IT & Technology/Security Operations"
        - otobo_queue2:
            - "IT & Technology/Software Development"
        - research_development:
            - "Science/*"
        - misc:
            - "*"

    priority_classification:
      tokenizer: "ticket_combined_email_tokenizer"
      hf_model: "google/flan-t5-base"
      ticket_attribute: "priority"
      ticket_to_model_results_map:
        - 1: [1]
        - 2: [2]
        - 3: [3]
        - 4: [4]
        - 5: [5]

  ticket_system_adapter:
    system_name: "otobo"
    rest_settings:
      base_url: "https://your-otobo-instance.com"
      username: "your_username"
      password: "your_password"
      search_url: "/api/v1/ticket/search"
      get_url:    "/api/v1/ticket/get"
      update_url: "/api/v1/ticket/update"
    incoming_queue: "otobo_queue1"
```

### Default Hugging Face Models

Out of the box, Open Ticket AI will download and use these pre-trained models (no fine-tuning required for basic operation):

::: note
In Development, See Huggingface for latest models.
:::
* `open-ticket-ai-queue-german-bert`
* `open-ticket-ai-priority-german-bert`
* `open-ticket-ai-priority-english-bert`
* `open-ticket-ai-priority-multilingual-bert`

To use your own model, simply set `hf_model: "<your-username>/<your-model-name>"` and your huggingface API token if its private in the config, and ensure your HF token has access.

---

## Training the Model

:::note
You only need to train your own model if you want to use a custom model or fine-tune the default models.
To get good results you will need a decent amount of training data, at least 1000 tickets per queue and priority.
Most likely you will need to clean your data, normalize the data, tokenize and try different models with different hyperparameters.
::: 

### 1. Data Collection

* Export historical tickets (subject + body) from your system.
* Label each with the correct queue and priority.

### 2. Data Cleaning

* Remove signatures, PII, spam.
* Normalize whitespace and character encodings.

### 3. Data Transformation & Tokenization

* Concatenate subject + body.
* Choose a `max_length` (e.g. 256–512) based on median ticket length.
* Use the provided `ticket_combined_email_tokenizer`.

### 4. Model Selection & Hardware

| Model                          | RAM Required | Notes                         |
| ------------------------------ | ------------ | ----------------------------- |
| `distilbert-base-german-cased` | 2 GB         | Lightweight, German text      |
| `bert-base-german-cased`       | 4 GB         | Higher accuracy, German text  |
| `deberta-large-mnli`           | 8 GB         | Multilingual / large contexts |

### 5. Training & Fine-Tuning

* Use the built-in hyperparameter tuner to sweep `learning_rate`, `batch_size`, `epochs`.
* Training script outputs a summary of model performance and resource usage.

### 6. Evaluation

* Measure **Accuracy** on queue + priority.
* Analyze **Confidence vs. Correctness** to set optimal `confidence_threshold`.
* Optionally compute a **Confidence-Weighted Accuracy Score (CWAS)**:

  ```math
  \text{CWAS} = \text{percent_predicted} \times (\text{percent_correct}^2)
  ```

---

## Usage

### Run Inference

```bash
docker-compose up classifier
```

* **Queue Worker** and **Priority Worker** fetch tickets, predict labels, then move or flag tickets based on confidence.

---

## Hardware Recommendations

* **CPU-only**: small volumes (< 50 tickets/min)
* **GPU** (e.g. NVIDIA RTX series): recommended for > 100 tickets/min
* Example: Hetzner Matrix GPU (20 GB RAM) or AWS `g4ad.xlarge`
And you should have the RAM available for the model you want to use, see table above.
For the default bert models yu will need 4GB + the RAM required for the ticketing system if they run on the same device.
If they ran on seperate devices thats also possible you just need to change the `rest_settings` in the `run_config.yaml` to point to the correct URL.
---

## License
See [LICENSE](LICENSE.md) for details.
