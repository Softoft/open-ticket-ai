---
description: Explore the Open Ticket AI architecture, a modular pipeline that leverages
  transformer models to automatically classify support tickets by queue and priority,
  streamlining help desk workflows and integrating with ticket systems via a REST
  API.
title: Open Ticket AI Architecture
---
# Architecture

## Pipeline & Value Objects

The core of Open Ticket AI is its processing pipeline:

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

Each stage in this pipeline consumes and produces **Value Objects** (e.g., `subject`, `body`, `queue_id`, `priority`). This design makes the pipeline modular and easy to extend with custom processing steps or new value objects.

## Pipeline Components

- **Pipeline** – A container that executes a sequence of pipes. It controls the
  overall status and stops execution if any pipe reports a failure.
- **Pipe** – A single processing step that implements a `process()` method.
  Pipes inherit from the `Providable` mixin so they can be created from the
  dependency injection container.
- **PipelineContext** – A Pydantic model passed to every pipe. It stores the
  ticket ID, arbitrary data produced by pipes and meta‑information such as the
  current pipeline status. Pipes read from and write to this context object to
  share data.

## System Diagrams

### Application Class Diagram

### Overview Diagram
