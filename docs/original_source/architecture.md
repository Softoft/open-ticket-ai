---
description: Explore the technical architecture of Open Ticket AI. Learn how its modular
  data pipeline and Hugging Face models enable intelligent ticket classification and
  routing.
title: Open Ticket AI Architecture Overview
---
# Architecture Overview

Open Ticket AI is built around a modular pipeline that processes each ticket through a series of well-defined stages. The system relies on dependency injection and configuration files to assemble these stages, making it easy to extend or replace individual pieces.

## Processing Pipeline

The ticket processing pipeline looks like this:

```
[ Incoming Ticket ]
       ↓
[ Preprocessor ] — cleans & merges subject+body
       ↓
[ Transformer Tokenizer ]
       ↓
[ Queue Classifier ] → Queue ID + confidence
       ↓
[ Priority Classifier ] → Priority score + confidence
       ↓
[ Postprocessor ] — applies thresholds, routes or flags
       ↓
[ Ticket System Adapter ] — updates ticket via REST API
```

Each step consumes and produces **Value Objects** such as `subject`, `body`, `queue_id` and `priority`. This approach keeps the pipeline modular and allows new steps or value objects to be added with minimal changes to the rest of the system.

## Main Components

- **App & Orchestrator** – Validate configuration, schedule jobs and manage the overall loop.
- **Fetchers** – Retrieve new tickets from external systems.
- **Preparers** – Transform raw ticket data into a form suitable for AI models.
- **AI Inference Services** – Load Hugging Face models and produce queue or priority predictions.
- **Modifiers** – Apply the predictions back to the ticket system via adapters.
- **Ticket System Adapters** – Provide REST integrations with systems such as OTOBO.

All components are registered in a central dependency injection container and configured via `config.yml`.

## Diagrams

### Application Class Diagram
![Application Class Diagram](../../public/images/application_class_diagram.png)

### Overview Diagram
![Overview DIagram](../../public/images/overview.png)

These diagrams illustrate how the pipeline is orchestrated and how each component interacts with the others.

---
