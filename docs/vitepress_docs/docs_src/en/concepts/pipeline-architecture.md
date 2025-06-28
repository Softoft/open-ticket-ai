---
title: Open Ticket AI Architecture
description: Learn about the architecture of Open Ticket AI.
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

## System Diagrams

### Application Class Diagram

### Overview Diagram
