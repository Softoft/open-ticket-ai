# AI README for Open Ticket AI Project

This document provides a comprehensive guide for AI assistants working on the 'Open Ticket AI' codebase. It outlines the project's architecture, components, conventions, and common development tasks.

## 1. Project Overview and Goal

**Project Name:** Open Ticket AI

**Goal:** To provide an on-premise, extensible framework for AI-powered ticket classification and prioritization.

**Problem Solved:** Addresses the manual, time-consuming, and error-prone process of assigning queues and priorities to incoming support tickets in open-source ticket systems (e.g., OTOBO, Zammad).

**Solution:** Utilizes fine-tuned transformer models to predict the correct queue and priority for each ticket. The system runs entirely on-premise to ensure data privacy and integrates with ticket systems via REST APIs.

## 2. Core Architecture and Workflow

The application employs a modular, pipeline-based architecture orchestrated by a central `App` class that runs a scheduler loop.

**Entry Point:**
*   `main.py`: Command-line interface (CLI) using `typer`. Handles argument parsing, logging configuration, initializes the `DIContainer`, and starts the `App`.

**Main Application Class:**
*   `app.py` (`App` class): Validates the application configuration and runs the main scheduler loop.

**Dependency Injection:**
*   `core/container.py` (`DIContainer`): Uses the `injector` library to manage dependencies. It binds configuration, registry, and various services, promoting modularity and testability.

**Component Registry:**
*   `core/registry.py` (`Registry` class): A simple class registry for looking up and managing available component classes (e.g., fetchers, predictors, modifiers).

**Orchestration:**
*   `run/orchestrator.py` (`Orchestrator` class): Responsible for scheduling and executing attribute predictors based on intervals defined in the `config.yml`.

**Ticket Processing Pipeline:**
The general workflow for processing a ticket involves the following sequence of components:

1.  **`DataFetcher`** (`run/fetchers/data_fetcher.py`): Retrieves ticket data from the source ticket system.
2.  **`DataPreparer`** (`run/preparers/data_preparer.py`): Cleans and transforms the fetched data into a format suitable for the AI model (e.g., concatenating ticket subject and body).
3.  **`AIInferenceService`** (`run/ai_models/ai_inference_service.py`): Takes the prepared data and uses an AI model to generate a prediction (e.g., a queue or priority).
4.  **`Modifier`** (`run/modifiers/modifier.py`): Takes the AI's prediction and applies it to the ticket in the source system via the `TicketSystemAdapter`.

This entire pipeline is managed by an **`AttributePredictor`** (`run/attribute_predictors/attribute_predictor.py`), which coordinates the fetcher, preparer, AI model, and modifier for a specific ticket attribute (e.g., queue, priority).

## 3. Key Components and Their Roles

**Configuration:**
*   `config.yml`: The central configuration file for the application. Defines the ticket system adapter, fetchers, preparers, AI models, modifiers, and attribute predictors, along with their parameters.
*   `core/config_models.py`: Contains Pydantic models used for validating the structure and types of the `config.yml` file.

**Attribute Predictors:**
*   Located in `run/attribute_predictors/`.
*   These are the core workflow managers, orchestrating the prediction process for a specific ticket attribute.
*   Examples: `QueuePredictor`, `PriorityPredictor`.
*   Each predictor is configured with a specific fetcher, preparer, AI service, and modifier.

**Data Fetchers:**
*   Located in `run/fetchers/`.
*   Responsible for retrieving data from the ticket system.
*   Example: `BasicTicketFetcher` (a starting point for fetching ticket data).

**Data Preparers:**
*   Located in `run/preparers/`.
*   Responsible for transforming raw ticket data into a format suitable for AI model inference.
*   Example: `SubjectBodyPreparer` (combines ticket subject and body text).

**AI Inference Services:**
*   Located in `run/ai_models/`.
*   These services execute the AI models to generate predictions.
*   Example: `HFAIInferenceService` (placeholder for a Hugging Face transformer model).

**Modifiers:**
*   Located in `run/modifiers/`.
*   These components apply the predictions made by the AI back to the ticket system.
*   Examples: `QueueModifier`, `PriorityModifier`.

**Ticket System Integration:**
*   Located in `ticket_system_integration/`.
*   Contains adapters for communicating with different ticket systems.
*   `TicketSystemAdapter` is the abstract base class defining the interface.
*   Example: `OTOBOAdapter` (provides methods to find and update tickets in OTOBO).

## 4. Coding Conventions and Style

*   **Dependency Injection:** The `injector` library is heavily used for DI. This promotes loose coupling between components and enhances testability. New services and components should be injectable.
*   **Configuration-Driven:** Components are designed to be highly configurable via `config.yml`. Pydantic models in `core/config_models.py` are used for strict configuration validation.
*   **Abstract Base Classes (ABCs):** Core components like `DataFetcher`, `DataPreparer`, `AIInferenceService`, `Modifier`, and `TicketSystemAdapter` are defined as ABCs (`abc.ABC`). This ensures a consistent interface for all concrete implementations. Implementations *must* inherit from these ABCs and implement their abstract methods.
*   **Mixins:** Utility mixins like `ConfigurableMixin` (for components that need access to their configuration section) and `DescriptionMixin` (for providing a human-readable description) are used to provide common functionality.
*   **Type Hinting:** Python's type hinting is used throughout the codebase for clarity, static analysis, and improved maintainability. All new code *must* include type hints.
*   **Modularity:** Components are designed to be modular and interchangeable.

## 5. How to Accomplish Common Tasks

### Adding a New Attribute Predictor (e.g., for Sentiment)

1.  **Create Predictor Class:**
    *   Define a new class, e.g., `SentimentPredictor`, in `run/attribute_predictors/`.
    *   This class *must* inherit from `AttributePredictor`.
    *   Implement the `run_attribute_prediction` method, detailing the logic for fetching data, preparing it, generating a sentiment prediction, and applying it.

2.  **Create Supporting Components (if needed):**
    *   **Modifier:** Create a `SentimentModifier` class in `run/modifiers/` inheriting from `Modifier`. Implement its logic to update the ticket with the sentiment.
    *   **Fetcher/Preparer:** If existing fetchers/preparers are not suitable, create new ones (e.g., `SentimentDataFetcher`, `SentimentDataPreparer`) inheriting from their respective ABCs.

3.  **Register New Classes:**
    *   Add the new `SentimentPredictor`, `SentimentModifier`, and any new fetcher/preparer classes to the registry in `core/create_registry.py`. This makes them discoverable by the application.

4.  **Update Configuration:**
    *   Add a new section for the `SentimentPredictor` in `config.yml`.
    *   Configure its `fetcher`, `preparer`, `ai_service`, and `modifier` (pointing to the newly created `SentimentModifier`).
    *   Define any necessary parameters for the new components.

### Integrating a New Ticket System (e.g., for Zammad)

1.  **Create Adapter Class:**
    *   Define a new class, e.g., `ZammadAdapter`, in `ticket_system_integration/`.
    *   This class *must* inherit from `TicketSystemAdapter`.
    *   Implement all abstract methods defined in `TicketSystemAdapter` (e.g., `update_ticket`, `find_tickets`, `get_ticket_by_id`, etc.) using the Zammad REST API.

2.  **Register New Adapter:**
    *   Add the `ZammadAdapter` class to the registry in `core/create_registry.py`.

3.  **Update Configuration:**
    *   In `config.yml`, update the `system` section:
        *   Set the `adapter_class` to `ZammadAdapter`.
        *   Provide any necessary parameters for the `ZammadAdapter` (e.g., API URL, API key, etc.).
    *   Ensure that data fetchers and modifiers are compatible with the data format and update mechanisms of Zammad. Adjust or create new ones as necessary.

---
**Note to AI:** Adhere to the conventions and patterns described above when generating or modifying code for this project. Pay close attention to dependency injection, configuration-driven design, and the use of abstract base classes. Always update the registry and configuration when adding new components.
