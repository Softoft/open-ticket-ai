---
title: Developer Information
description: Developer information for the ATC Community Edition
---
# Developer Information for the ATC Community Edition

## Overview

The ATC Community Edition is an on-premise solution for automated classification of support tickets. The current MVP version is controlled via a YAML configuration file and started via CLI. There is no REST API for uploading training data or triggering a training run.

## Software Architecture

The application essentially consists of the following packages:

* **core** – base classes, configuration models, and helper functions.
* **run** – contains the pipeline for ticket classification.
* **ticket\_system\_integration** – adapters for different ticket systems.
* **main.py** – CLI entry point that starts the scheduler and the orchestrator.

The orchestrator executes configurable `AttributePredictors`, which are composed of `DataFetcher`, `DataPreparer`, `AIInferenceService`, and `Modifier`. All components are defined in `config.yml` and validated at program startup.

An example command to start the application:

```bash
python -m open_ticket_ai.src.ce.main start
```

## Training Custom Models

Direct training through the application is not provided in the MVP. Pre-trained models can be specified and used in the configuration. If a model needs to be adjusted or newly created, this must be done outside the application.

## Extension

Custom fetchers, preparers, AI services, or modifiers can be implemented as Python classes and registered via the configuration. Thanks to dependency injection, new components can be easily integrated.

## Summary

The ATC Community Edition offers a locally executed workflow for automatic ticket classification in its MVP version. All settings are managed via YAML files; no REST API is available. External processes or scripts must be used for training.
