---
description: Discover the Open Ticket AI architecture, a modular pipeline that uses
  transformer models to automatically process and classify support tickets by queue
  and priority, streamlining help desk workflows.
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

## System Diagrams

### Application Class Diagram
![Application Class Diagram](/images/application_class_diagram.png)

### Overview Diagram
![Overview Diagram](/images/overview.png)
