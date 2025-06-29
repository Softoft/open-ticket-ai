# Open Ticket AI Project Summary

This document provides a high-level technical overview of the Open Ticket AI system, based on the
provided source code documentation. The system is designed for the automated classification and
processing of support tickets.

## 1. Core Architecture

The application is built around a modular, configurable **pipeline architecture**. It operates as a
long-running, scheduled service that continuously processes tickets from integrated systems.

The main components of this architecture are:

- **App (`app.py`):** The main application entry point. It initializes the system, validates the
  configuration, sets up scheduled jobs via the `Orchestrator`, and runs an infinite loop to execute
  pending tasks.
- **Orchestrator (`orchestrator.py`):** The top-level manager responsible for building and
  scheduling the execution of processing pipelines based on the application's configuration. It uses
  the `schedule` library to run pipelines at periodic intervals.
- **Pipeline (`pipeline.py`):** A composite component that executes a sequence of individual
  processing stages (`Pipes`) in a defined order. It manages the flow of data through its
  constituent pipes.
- **Pipe (`pipe.py`):** An abstract base class representing a single stage in a processing pipeline.
  Each `Pipe` implementation performs a specific task, such as fetching data, preparing it, running
  an AI model, or updating a ticket.
- **PipelineContext (`context.py`):** A state object that is passed between each `Pipe` in a
  `Pipeline`. It carries the `ticket_id` and a flexible `data` dictionary to share information (
  e.g., ticket content, model predictions) across stages.

### Standard Processing Flow

A typical ticket classification pipeline follows these steps:

1. **Fetch Ticket:** A fetcher pipe (e.g., `BasicTicketFetcher`) retrieves ticket data from an
   external system using a `TicketSystemAdapter`.
2. **Prepare Data:** A preparer pipe (e.g., `SubjectBodyPreparer`) cleans and transforms the raw
   ticket data (like subject and body) into a format suitable for the AI model.
3. **AI Inference:** An inference service pipe (e.g., `HFAIInferenceService`) processes the prepared
   data with a machine learning model (e.g., a local Hugging Face model) to generate predictions.
4. **Update Ticket:** An updater pipe (e.g., `GenericTicketUpdater`) uses the prediction results
   stored in the `PipelineContext` to update the ticket in the source system.

## 2. Modularity and Configuration

The system is designed to be highly extensible and configurable, primarily through Dependency
Injection (DI) and a component registry.

- **Dependency Injection (`di.md`):** A central DI container is responsible for instantiating and
  wiring together all components of the system. The `create_registry()` function registers the
  default implementations for adapters, preparers, and AI services, allowing them to be referenced
  in the configuration.
- **Registry & Providables (`mixins.md`):** Components intended to be managed by the DI system
  inherit from `RegistryProvidableInstance`. This base class allows them to be identified by a
  unique `provider_key` (their class name) and configured with specific parameters via a
  `RegistryInstanceConfig` object. This makes the system's components discoverable and configurable.
- **Configuration (`ce_core_config.md`):** The entire application, including the pipelines and their
  components, is defined in a configuration file (e.g., `config.yml`). This configuration is
  validated against Pydantic models at startup. Utilities like `create_json_config_schema.py` are
  provided to generate a JSON schema for configuration validation and editor support.

## 3. Extensibility

The architecture makes it straightforward to extend the system's functionality:

- **Ticket System Integration (`ticket_system_integration.md`):** To support a new ticketing system,
  a developer can create a new class that inherits from the abstract `TicketSystemAdapter` and
  implements its methods (`find_tickets`, `update_ticket`, etc.). This new adapter can then be
  registered and used in the configuration. The `OTOBOAdapter` serves as the primary example.
- **Custom Pipeline Stages (`pipes.md`):** New processing logic can be added by creating a new class
  that inherits from the `Pipe` interface and implements the `process()` method. Once created, this
  new pipe can be registered and included in any pipeline via the configuration file.

## 4. Execution Model

The application is launched via a Command-Line Interface (CLI) defined in `main.py`.

1. The `start()` command initializes the DI container and retrieves the main `App` instance.
2. The `App.run()` method is called.
3. The `Orchestrator` builds all pipelines defined in the configuration.
4. The `Orchestrator` then configures a scheduler to execute each pipeline's processing function at
   its specified interval.
5. The application enters a continuous loop, checking for and running scheduled jobs.
