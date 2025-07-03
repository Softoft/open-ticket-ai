# AI_README.md: A Guide for LLM Assistants

## 1. Introduction for the LLM

Hello. Your purpose is to act as an expert assistant for the **Open Ticket AI** project (also referred to as ATC - Automated Ticket Classification). You will help three primary user groups: **Project Developers**, **Project Managers**, and **Documentation Writers**.

This document is your primary source of knowledge. It synthesizes the project's official documentation, source code structure, and architectural principles into a comprehensive guide.

**Your Most Important Instruction:**

The project's documentation is distributed across various files and formats, and some parts may be outdated. **You must treat the documentation found in the `/api` directory as the single source of truth.** These files are generated from the source code's docstrings and are always up-to-date. When providing information about the system's classes, methods, and core interfaces, prioritize the details from these files:

*   `docs/vitepress_docs/docs_src/en/en/api/core/ce_core_config.md`
*   `docs/vitepress_docs/docs_src/en/en/api/core/di.md`
*   `docs/vitepress_docs/docs_src/en/en/api/core/mixins.md`
*   `docs/vitepress_docs/docs_src/en/en/api/core/util.md`
*   `docs/vitepress_docs/docs_src/en/en/api/main.md`
*   `docs/vitepress_docs/docs_src/en/en/api/run/managers.md`
*   `docs/vitepress_docs/docs_src/en/en/api/run/pipeline.md`
*   `docs/vitepress_docs/docs_src/en/en/api/run/pipes.md`
*   `docs/vitepress_docs/docs_src/en/en/api/run/ticket_system_integration.md`

Use other documents like blog posts, architecture overviews, and guides to understand the project's intent, use cases, and high-level concepts, but always defer to the `/api` documentation for technical specifics.

## 2. Project Overview: Open Ticket AI

**Open Ticket AI** is a self-hosted, on-premise background service designed to bring artificial intelligence capabilities to open-source help desk and ticket systems. Its primary function is to automate the classification and routing of support tickets, thereby increasing efficiency, reducing manual triage, and improving response times.

### Key Features

*   **Automated Classification:** Uses Hugging Face transformer models to predict ticket attributes like **queue** (e.g., Sales, IT Support) and **priority** (e.g., Low, High).
*   **On-Premise Deployment:** Runs entirely within the user's infrastructure via Docker containers. This ensures data privacy and security, as sensitive ticket data never leaves the local environment.
*   **Extensible Pipeline Architecture:** The core logic is a modular pipeline that processes tickets in stages. Developers can easily add, remove, or replace components to customize workflows.
*   **Ticket System Integration:** Designed to be system-agnostic through a dedicated adapter pattern. It includes a ready-to-use integration for **OTOBO**, **Znuny**, and **OTRS**, with a clear path for integrating other systems like Zendesk, Freshdesk, or Zammad.
*   **Configuration-Driven:** The entire application behavior, from pipeline composition to model selection and scheduling, is controlled by a central `config.yml` file.
*   **REST API:** Provides an HTTP REST API for integration, allowing external systems to send data for classification and, in some configurations, to manage training data and trigger model training.

### Core Technology Stack

Based on the `pyproject.toml` file, the key technologies you should be aware of are:

*   **Language:** Python (>=3.13)
*   **AI/ML:** `transformers`, `huggingface-hub`, `spacy`, `openai`
*   **Core Framework:** Dependency injection via `injector`, job scheduling with `schedule`.
*   **Data Handling:** `pydantic` for robust data modeling and validation.
*   **Integration:** `requests` for HTTP clients, and a dedicated `otobo` client library.
*   **Deployment:** Docker and Docker Compose.
*   **CLI:** Built using standard Python libraries.
*   **Documentation:** `mkdocs` with `mkdocs-material` and `mkdocstrings`.

## 3. Core Architectural Principles

To effectively assist users, you must have a deep understanding of the three pillars of the Open Ticket AI architecture: the **Pipeline System**, **Dependency Injection**, and **Configuration**.

### 3.1. The Pipeline Architecture

The heart of the application is a data processing pipeline. A ticket enters the pipeline and is passed sequentially through a series of stages, each performing a specific task.

*   **Source of Truth:** `docs/vitepress_docs/docs_src/en/en/api/run/pipeline/*.md`

#### Key Components:

*   **`Pipeline`**:
    *   **Purpose:** A specialized `Pipe` that orchestrates the execution of a sequence of other `Pipe`s.
    *   **Functionality:** It manages the overall execution flow, handles status transitions (e.g., from `RUNNING` to `SUCCESS` or `FAILED`), propagates errors, and respects stop requests from individual pipes.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/pipeline/pipeline.py`

*   **`Pipe`**:
    *   **Purpose:** An abstract base class representing a single, modular processing stage in the pipeline.
    *   **Interface:** Every `Pipe` must implement the `process(self, context: PipelineContext) -> PipelineContext` method. This method contains the core logic of the stage.
    *   **Extensibility:** It inherits from the `Providable` mixin, making it manageable by the dependency injection system.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/pipeline/pipe.py`

*   **`PipelineContext`**:
    *   **Purpose:** A Pydantic model that acts as a stateful container, passed between each `Pipe` in the `Pipeline`.
    *   **Structure:** It holds two main attributes:
        1.  `data`: A generic, Pydantic-validated payload where pipes read their input and write their output (e.g., ticket text, model predictions, transformed data).
        2.  `meta_info`: An object of type `MetaInfo` that tracks the pipeline's execution state.
    *   **Control Flow:** A pipe can call `context.stop_pipeline()` to signal a controlled halt to the execution.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/pipeline/context.py`

*   **`MetaInfo` and `PipelineStatus`**:
    *   **Purpose:** These components track the live status of a pipeline execution.
    *   **`PipelineStatus` (Enum):** Defines the possible states: `RUNNING`, `SUCCESS`, `FAILED`, `STOPPED`.
    *   **`MetaInfo` (Pydantic Model):** Stores the current `status`, an `error_message`, and the `failed_pipe` identifier if an error occurs.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/pipeline/meta_info.py` and `status.py`.

**How to Explain the Pipeline:** When a user asks how the system processes a ticket, describe it as a factory assembly line. The `Pipeline` is the conveyor belt, the `Pipe`s are the workstations, and the `PipelineContext` is the part being assembled, with data being added at each station.

### 3.2. Dependency Injection (DI)

The application is built on a dependency injection framework to promote modularity and testability. Instead of components creating their own dependencies, they are "injected" at runtime by a central container.

*   **Source of Truth:** `docs/vitepress_docs/docs_src/en/en/api/core/di.md`

#### Key Components:

*   **`DIContainer` and `AbstractContainer`**: The container is the central object that holds the registry of all available components and knows how to construct them.
*   **`Registry`**: A dictionary-like object that maps provider keys (strings) to component classes.
*   **`create_registry()`**: This is a critical function. It initializes the `Registry` and registers all the default, core components of the application. **When a developer asks what components are available out-of-the-box, you should refer them to the body of this function.** As per the documentation, it registers:
    *   `OTOBOAdapter`: For OTOBO integration.
    *   `SubjectBodyPreparer`: A pipe for preparing ticket text.
    *   `HFLocalAIInferenceService`: A service for running local Hugging Face models.
*   **`Providable` Mixin**:
    *   **Purpose:** A base class that makes any object manageable by the DI system.
    *   **Key Method:** `get_provider_key(cls) -> str`. This class method returns a unique string identifier (by default, the class name) used to register and request the component from the container. Any custom component a developer creates (like a new `Pipe` or `TicketSystemAdapter`) must inherit from `Providable`.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/core/mixins.md`

**How to Explain DI:** Tell developers that instead of writing `my_adapter = OTOBOAdapter(config)`, they should define the adapter in `config.yml` and let the system build it for them. The DI container reads the configuration, finds the correct class in its registry using the provider key, and automatically passes in any required dependencies (like configuration objects).

### 3.3. Configuration

The application is highly configurable through a single YAML file and Pydantic models for validation.

*   **Source of Truth:** `docs/vitepress_docs/docs_src/en/en/api/core/ce_core_config.md`

#### Key Components:

*   **`config.yml`**: The main configuration file where users define everything: pipeline structures, model names, ticket system credentials, and scheduling intervals.
*   **Pydantic Models (`config_models.py`)**: The structure of `config.yml` is strictly defined by a set of Pydantic models. This ensures that the configuration is valid at startup and provides type-safe access to settings within the code.
*   **JSON Schema Generation (`create_json_config_schema.py`)**: The project includes a utility script to generate a `config.schema.json` file from the Pydantic models. **You should inform developers that this schema can be used in their IDEs (like VS Code) to get autocompletion and validation when editing `config.yml`.**
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/core/util.md`

## 4. Key System Components

Here is a breakdown of the primary runtime components you should be familiar with.

### 4.1. Application Entry Point (`main.py`)

*   **Purpose:** The command-line interface (CLI) for starting the application.
*   **Command:** `python -m open_ticket_ai.src.ce.main start`
*   **Functionality:** The `start()` function initializes the DI container, which in turn reads `config.yml` and builds all necessary objects. It then retrieves the main `App` instance and runs it. The `main()` function handles CLI flags like `--verbose` and `--debug` to control logging levels.
*   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/main.md`

### 4.2. Orchestration (`Orchestrator.py`)

*   **Purpose:** The top-level manager that orchestrates the entire ticket processing workflow.
*   **Functionality:**
    1.  **`build_pipelines()`**: Reads the pipeline configurations from `config.yml` and uses the DI container to instantiate all the `Pipeline` and `Pipe` objects.
    2.  **`set_schedules()`**: Iterates through the configured pipelines and uses the `schedule` library to set up their periodic execution (e.g., "run every 5 minutes").
    3.  **`process_ticket()`**: Executes a single pipeline for a specific ticket ID. This is the core method for processing one ticket.
*   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/managers.md`

### 4.3. Ticket System Integration

This is the most important area for extensibility. The system is designed to connect to any ticket system via a custom adapter.

*   **Source of Truth:** `docs/vitepress_docs/docs_src/en/en/api/run/ticket_system_integration/*.md`

#### Key Components:

*   **`TicketSystemAdapter` (Abstract Base Class)**:
    *   **Purpose:** Defines the standard interface (a contract) for all ticket system integrations.
    *   **Abstract Methods:** Any concrete adapter **must** implement the following `async` methods:
        *   `create_ticket(self, ticket_data: UnifiedTicket) -> UnifiedTicket`
        *   `update_ticket(self, ticket_id: str, updates: dict) -> bool`
        *   `find_tickets(self, criteria: SearchCriteria) -> list[UnifiedTicket]`
        *   `find_first_ticket(self, criteria: SearchCriteria) -> UnifiedTicket | None`
        *   `add_note(self, ticket_id: str, note: UnifiedNote) -> UnifiedNote`
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/ticket_system_integration/ticket_system_adapter.py`

*   **Unified Data Models (`unified_models.py`)**:
    *   **Purpose:** A set of Pydantic models (`UnifiedTicket`, `UnifiedUser`, `UnifiedNote`, etc.) that provide a system-agnostic representation of ticket data.
    *   **Functionality:** Adapters are responsible for translating between their system's native data format and these unified models. This keeps the core pipeline logic independent of any specific ticket system.
    *   **Reference:** `docs/vitepress_docs/docs_src/en/en/api/run/ticket_system_integration/unified_models.py`

*   **`OTOBOAdapter`**: The default, built-in implementation for OTOBO, Znuny, and OTRS systems.

## 5. The AI/ML Workflow

The project's approach to machine learning is practical and focused on leveraging pre-trained models.

### 5.1. Model Training and Fine-Tuning

**This is a critical point:** Model training is an **external process**. The application itself does not provide tools for training. You must guide users through the following workflow, referencing the `guide/training-models.md` and the blog post `fine-tuning-an-ai-model-with-own-ticket-data.md`.

1.  **Export Data:** The user must export labeled ticket data from their help desk system into a structured format like CSV (e.g., with `text` and `label` columns).
2.  **Fine-Tune a Model:** Using a separate environment (like a Jupyter Notebook), the user fine-tunes a pre-trained transformer model (e.g., `distilbert-base-uncased`) from the Hugging Face Hub on their exported data. The `transformers` library is the recommended tool for this.
3.  **Publish or Save:** The fine-tuned model is either uploaded to the Hugging Face Hub or saved to a local directory accessible by the application.
4.  **Configure:** The user updates `config.yml`, changing the `model_name` in the relevant pipeline to point to their new custom model.
5.  **Restart:** The application is restarted to load the new model.

### 5.2. Data Labeling

For users who need to create a labeled dataset from scratch, you should recommend the semi-automated workflow described in the `automatic_ticket_labeling.md` blog post.

1.  **Pre-label with an LLM:** Use a powerful LLM (like GPT-4 via the OpenAI or OpenRouter API) with zero-shot or few-shot prompting to generate initial labels for the raw ticket data.
2.  **Review and Correct:** Import the pre-labeled data into an annotation tool like **Label Studio**. Human annotators then review the AI-generated labels, correcting them where necessary. This is significantly faster than labeling from scratch.

### 5.3. Model Evaluation

When users ask how to evaluate their models, you must steer them away from using simple accuracy. Refer to the `ai_classifiers_metrics.md` blog post.

*   **Problem:** Ticket datasets are almost always **imbalanced** (e.g., 90% "General Inquiry," 5% "Billing," 5% "Urgent Bug"). A model that only predicts the majority class can achieve 90% accuracy while being useless in practice.
*   **Solution:** Advise them to use a `classification_report` (from scikit-learn) and focus on these metrics, especially for minority classes:
    *   **Precision:** Of all the tickets predicted as "Urgent Bug," how many actually were? (Minimizes false positives).
    *   **Recall:** Of all the actual "Urgent Bug" tickets, how many did the model find? (Minimizes false negatives).
    *   **F1-Score:** The harmonic mean of precision and recall, providing a balanced measure.
    *   **Macro Average:** When evaluating multi-class performance, recommend the **macro average F1-score**, as it treats all classes equally, regardless of their size, giving a better sense of performance on rare but important categories.

## 6. Your Role: How to Assist Project Stakeholders

Use the knowledge above to provide targeted assistance.

### For Project Developers

*   **"How do I add a new processing step to the pipeline?"**
    1.  Guide them to create a new Python class that inherits from `Pipe` and the `Providable` mixin.
    2.  Tell them to implement the core logic inside the `process(self, context)` method. They should read data from `context.data` and write their results back to it.
    3.  If the pipe needs configuration, they should create a Pydantic `BaseModel` for its settings.
    4.  They must register their new pipe class in the DI registry (e.g., in `create_registry.py`).
    5.  Finally, they add the pipe's provider key to a pipeline definition in `config.yml`.
    6.  Reference the `SentimentAnalysisPipe` example in `developer-information.md`.

*   **"How do I integrate a new ticket system like Jira?"**
    1.  Explain the `TicketSystemAdapter` pattern. They need to create a `JiraAdapter` class that inherits from `TicketSystemAdapter`.
    2.  Instruct them to implement all the abstract `async` methods (`update_ticket`, `find_tickets`, etc.) by making calls to the Jira REST API.
    3.  They will need to translate data between Jira's JSON format and the project's `UnifiedTicket` models.
    4.  They must register their `JiraAdapter` in `create_registry.py`.
    5.  Finally, they update `config.yml` to use their new adapter.
    6.  Point them to the blog posts on integrating **Freshdesk**, **Zendesk**, and **Zammad** as practical examples of this pattern.

*   **"How do I debug my code?"**
    1.  Advise them to start the application with the `--debug` flag for verbose logging: `python -m open_ticket_ai.src.ce.main start --debug`.
    2.  If using Docker, they can monitor logs with `docker-compose logs -f`.
    3.  Suggest adding print statements or using a debugger within their custom `Pipe` or `Adapter` methods.

### For Project Managers

*   **"What are the main selling points of this project?"**
    *   Summarize the key features: On-premise deployment for maximum data security, significant time and cost savings through automation of manual ticket triage, high extensibility to fit custom workflows, and seamless integration with OTOBO-family help desks.

*   **"What are the hardware requirements?"**
    *   Reference `guide/hardware-requirements.md`. For small ticket volumes or simple models like DistilBERT, a CPU-only server is sufficient. For high volumes or larger models (like BERT-base), a GPU is recommended.
    *   Provide RAM estimates: ~2 GB for DistilBERT, ~4 GB for BERT-base, plus overhead for the OS and other services.

*   **"Can we customize the classification logic?"**
    *   Yes, absolutely. Explain that the system is designed for this. They can fine-tune AI models on their own historical ticket data to recognize company-specific categories. The pipeline itself is also fully customizable, allowing for unique business rules to be implemented as custom `Pipe`s.

### For Documentation Writers

*   **"Where can I find the most accurate information?"**
    *   Reiterate the golden rule: **The `/api` directory documentation is the source of truth for all technical details.** It is generated directly from the code. Use other documents for context and high-level explanations, but always verify technical claims against the API docs.

*   **"I need to document a new feature. How should I proceed?"**
    *   Advise them to follow the existing structure. If a new module or class is added, ensure it has comprehensive Python docstrings so `mkdocstrings` can generate its API page.
    *   For new concepts, create a page in the `concepts` directory.
    *   For user-facing workflows, create a page in the `guide` directory.
    *   Encourage the use of Mermaid.js for flowcharts and diagrams to visually explain complex processes like the pipeline architecture.
DIRECTORY STRUCTURE:
open-ticket-ai
├── .editorconfig
├── .git
├── .github
│   └── workflows
│       └── python-app.yml
├── .gitignore
├── .idea
│   ├── .gitignore
│   ├── codeStyles
│   │   └── codeStyleConfig.xml
│   ├── dictionaries
│   │   └── project.xml
│   ├── inspectionProfiles
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   ├── open-ticket-ai.iml
│   ├── shelf
│   ├── vcs.xml
│   └── workspace.xml
├── .pytest_cache
├── .ruff_cache
├── AI_README.md
├── cli
│   └── activate.sh
├── docs
│   ├── _documentation_summaries.json
│   └── vitepress_docs
│       ├── .idea
│       │   ├── .gitignore
│       │   ├── inspectionProfiles
│       │   │   └── Project_Default.xml
│       │   ├── vcs.xml
│       │   ├── watcherTasks.xml
│       │   └── workspace.xml
│       ├── .vitepress
│       │   ├── components
│       │   │   ├── ContactFormModal.vue
│       │   │   ├── demoExamples.ts
│       │   │   ├── OTAIPredictionDemo.vue
│       │   │   ├── ProductCards.vue
│       │   │   ├── ServicePackagesComponent.vue
│       │   │   └── SupportPlansComponent.vue
│       │   ├── config.mts
│       │   ├── dist
│       │   ├── navbarUtil.ts
│       │   └── theme
│       │       ├── index.ts
│       │       └── styles
│       │           ├── theme.scss
│       │           └── vitepress-styles.scss
│       ├── docs_src
│       │   ├── _IMPORTANT.md
│       │   ├── de
│       │   │   ├── api
│       │   │   │   ├── core
│       │   │   │   │   ├── ce_core_config.md
│       │   │   │   │   ├── di.md
│       │   │   │   │   ├── mixins.md
│       │   │   │   │   └── util.md
│       │   │   │   ├── main.md
│       │   │   │   └── run
│       │   │   │       ├── managers.md
│       │   │   │       ├── pipeline.md
│       │   │   │       ├── pipes.md
│       │   │   │       └── ticket_system_integration.md
│       │   │   ├── architecture.md
│       │   │   ├── blog
│       │   │   │   ├── ai-in-open-source-ticketsystems.md
│       │   │   │   ├── ai-in-ticketsystems.md
│       │   │   │   ├── ai_classifiers_metrics.md
│       │   │   │   ├── automatic_ticket_labeling.md
│       │   │   │   └── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │   │   ├── concepts
│       │   │   │   ├── community-edition-overview.md
│       │   │   │   ├── default-integrations-overview.md
│       │   │   │   ├── key-features.md
│       │   │   │   └── pipeline-architecture.md
│       │   │   ├── developer-information.md
│       │   │   ├── get-started.md
│       │   │   ├── guide
│       │   │   │   ├── hardware-requirements.md
│       │   │   │   ├── installation-guide.md
│       │   │   │   ├── otobo-znuny-otrs-integration.md
│       │   │   │   ├── quickstart-guide.md
│       │   │   │   ├── running-classifier.md
│       │   │   │   └── training-models.md
│       │   │   ├── index.md
│       │   │   └── messages.ts
│       │   └── en
│       │       ├── _config_examples
│       │       │   ├── config.schema.json
│       │       │   ├── queue_priority_hf_endpoint_config.yml
│       │       │   └── queue_priority_local_config.yml
│       │       ├── api
│       │       │   ├── core
│       │       │   │   ├── ce_core_config.md
│       │       │   │   ├── di.md
│       │       │   │   ├── mixins.md
│       │       │   │   └── util.md
│       │       │   ├── main.md
│       │       │   └── run
│       │       │       ├── managers.md
│       │       │       ├── pipeline.md
│       │       │       ├── pipes.md
│       │       │       └── ticket_system_integration.md
│       │       ├── architecture.md
│       │       ├── blog
│       │       │   ├── ai-in-open-source-ticketsystems.md
│       │       │   ├── ai-in-ticketsystems.md
│       │       │   ├── ai_classifiers_metrics.md
│       │       │   ├── automatic_ticket_labeling.md
│       │       │   ├── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │       │   ├── integrating-freshdesk-open-ticket-ai.md
│       │       │   ├── integrating-zammad-open-ticket-ai.md
│       │       │   └── integrating-zendesk-open-ticket-ai.md
│       │       ├── concepts
│       │       │   ├── community-edition-overview.md
│       │       │   ├── key-features.md
│       │       │   ├── mvp-technical-overview.md
│       │       │   └── pipeline-architecture.md
│       │       ├── de
│       │       │   ├── api
│       │       │   │   ├── core
│       │       │   │   │   ├── ce_core_config.md
│       │       │   │   │   ├── di.md
│       │       │   │   │   ├── mixins.md
│       │       │   │   │   └── util.md
│       │       │   │   ├── main.md
│       │       │   │   └── run
│       │       │   │       ├── managers.md
│       │       │   │       ├── pipeline.md
│       │       │   │       ├── pipes.md
│       │       │   │       └── ticket_system_integration.md
│       │       │   ├── architecture.md
│       │       │   ├── blog
│       │       │   │   ├── ai-in-open-source-ticketsystems.md
│       │       │   │   ├── ai-in-ticketsystems.md
│       │       │   │   ├── ai_classifiers_metrics.md
│       │       │   │   ├── automatic_ticket_labeling.md
│       │       │   │   ├── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │       │   │   ├── integrating-freshdesk-open-ticket-ai.md
│       │       │   │   ├── integrating-zammad-open-ticket-ai.md
│       │       │   │   └── integrating-zendesk-open-ticket-ai.md
│       │       │   ├── concepts
│       │       │   │   ├── community-edition-overview.md
│       │       │   │   ├── key-features.md
│       │       │   │   ├── mvp-technical-overview.md
│       │       │   │   └── pipeline-architecture.md
│       │       │   ├── developer-information.md
│       │       │   ├── get-started.md
│       │       │   ├── guide
│       │       │   │   ├── hardware-requirements.md
│       │       │   │   ├── installation-guide.md
│       │       │   │   ├── otobo-znuny-otrs-integration.md
│       │       │   │   ├── quickstart-guide.md
│       │       │   │   ├── running-classifier.md
│       │       │   │   └── training-models.md
│       │       │   └── index.md
│       │       ├── developer-information.md
│       │       ├── en
│       │       │   ├── api
│       │       │   │   ├── core
│       │       │   │   │   ├── ce_core_config.md
│       │       │   │   │   ├── di.md
│       │       │   │   │   ├── mixins.md
│       │       │   │   │   └── util.md
│       │       │   │   ├── main.md
│       │       │   │   └── run
│       │       │   │       ├── managers.md
│       │       │   │       ├── pipeline.md
│       │       │   │       ├── pipes.md
│       │       │   │       └── ticket_system_integration.md
│       │       │   ├── architecture.md
│       │       │   ├── blog
│       │       │   │   ├── ai-in-open-source-ticketsystems.md
│       │       │   │   ├── ai-in-ticketsystems.md
│       │       │   │   ├── ai_classifiers_metrics.md
│       │       │   │   ├── automatic_ticket_labeling.md
│       │       │   │   ├── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │       │   │   ├── integrating-freshdesk-open-ticket-ai.md
│       │       │   │   ├── integrating-zammad-open-ticket-ai.md
│       │       │   │   └── integrating-zendesk-open-ticket-ai.md
│       │       │   ├── concepts
│       │       │   │   ├── community-edition-overview.md
│       │       │   │   ├── key-features.md
│       │       │   │   ├── mvp-technical-overview.md
│       │       │   │   └── pipeline-architecture.md
│       │       │   ├── developer-information.md
│       │       │   ├── get-started.md
│       │       │   ├── guide
│       │       │   │   ├── hardware-requirements.md
│       │       │   │   ├── installation-guide.md
│       │       │   │   ├── otobo-znuny-otrs-integration.md
│       │       │   │   ├── quickstart-guide.md
│       │       │   │   ├── running-classifier.md
│       │       │   │   └── training-models.md
│       │       │   └── index.md
│       │       ├── get-started.md
│       │       ├── guide
│       │       │   ├── hardware-requirements.md
│       │       │   ├── installation-guide.md
│       │       │   ├── otobo-znuny-otrs-integration.md
│       │       │   ├── quickstart-guide.md
│       │       │   ├── running-classifier.md
│       │       │   └── training-models.md
│       │       ├── index.md
│       │       └── messages.ts
│       ├── node_modules
│       ├── package-lock.json
│       ├── package.json
│       └── public
│           ├── ai-in-ticket-system.png
│           ├── diagrams
│           │   ├── diagram-gen.puml
│           │   ├── mvp-software-design.puml
│           │   ├── pipes-data-flow.puml
│           │   └── ticket_system_integration.puml
│           ├── images
│           │   ├── application_class_diagram.png
│           │   ├── mv-no-data-collection.png
│           │   ├── mvp-design.png
│           │   ├── mvp-software-design.png
│           │   └── overview.png
│           ├── open-source-ticket-system.png
│           └── openapi.json
├── installation
│   └── otobo
│       ├── compose.yml
│       ├── OTAI_OTOBO_webservice.yml
│       └── webservice-setup.sh
├── LICENSE
├── LICENSE_DE.md
├── LICENSE_EN.md
├── netlify.toml
├── open_ticket_ai
│   ├── .pytest_cache
│   ├── __init__.py
│   ├── __pycache__
│   ├── config.schema.json
│   ├── config.yml
│   ├── experimental
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── anonymize_data.py
│   │   └── email_extraction.py
│   ├── scripts
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   ├── doc_generation
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   ├── add_docstrings.py
│   │   │   ├── generate_api_reference.py
│   │   │   ├── generate_multi_lang_docs.py
│   │   │   ├── translation_instruction.txt
│   │   │   └── update_frontmatter.py
│   │   ├── doc_generation_facade.py
│   │   ├── documentation_summary.py
│   │   ├── license_script.py
│   │   ├── readme_updater.py
│   │   ├── update_file_path_comments.py
│   │   └── util
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       └── display_file_structure.py
│   ├── src
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── ce
│   │       ├── __init__.py
│   │       ├── __pycache__
│   │       ├── app.py
│   │       ├── core
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   ├── config
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __pycache__
│   │       │   │   ├── config_models.py
│   │       │   │   └── config_validator.py
│   │       │   ├── dependency_injection
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __pycache__
│   │       │   │   ├── abstract_container.py
│   │       │   │   ├── container.py
│   │       │   │   ├── create_registry.py
│   │       │   │   └── registry.py
│   │       │   ├── mixins
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __pycache__
│   │       │   │   └── registry_providable_instance.py
│   │       │   └── util
│   │       │       ├── __init__.py
│   │       │       ├── __pycache__
│   │       │       ├── create_json_config_schema.py
│   │       │       ├── path_util.py
│   │       │       └── pretty_print_config.py
│   │       ├── main.py
│   │       ├── otobo_integration
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   ├── otobo_adapter.py
│   │       │   └── unified_models.py
│   │       ├── run
│   │       │   ├── __init__.py
│   │       │   ├── __pycache__
│   │       │   ├── managers
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __pycache__
│   │       │   │   └── orchestrator.py
│   │       │   ├── pipe_implementations
│   │       │   │   ├── __init__.py
│   │       │   │   ├── __pycache__
│   │       │   │   ├── ai_text_model_input.py
│   │       │   │   ├── empty_data_model.py
│   │       │   │   ├── generic_ticket_updater
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __pycache__
│   │       │   │   │   └── generic_ticket_updater.py
│   │       │   │   ├── hf_cloud_inference_service.py
│   │       │   │   ├── hf_inference_services
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── hf_cloud_inference_service.py
│   │       │   │   │   └── hf_local_ai_inference_service.py
│   │       │   │   ├── hf_local_ai_inference_service.py
│   │       │   │   ├── subject_body_preparer
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── __pycache__
│   │       │   │   │   └── subject_body_preparer.py
│   │       │   │   └── ticket_fetcher
│   │       │   │       ├── __init__.py
│   │       │   │       └── basic_ticket_fetcher.py
│   │       │   └── pipeline
│   │       │       ├── __init__.py
│   │       │       ├── __pycache__
│   │       │       ├── context.py
│   │       │       ├── meta_info.py
│   │       │       ├── pipe.py
│   │       │       ├── pipeline.py
│   │       │       └── status.py
│   │       └── ticket_system_integration
│   │           ├── __init__.py
│   │           ├── __pycache__
│   │           ├── otobo_adapter.py
│   │           ├── otobo_adapter_config.py
│   │           ├── ticket_system_adapter.py
│   │           └── unified_models.py
│   └── tests
│       ├── __init__.py
│       ├── __pycache__
│       ├── conftest.py
│       ├── experimental
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   └── test_anonymize_data.py
│       ├── otobo_adapter_test.py
│       ├── scripts
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   ├── test_doc_generation
│       │   │   ├── __init__.py
│       │   │   ├── __pycache__
│       │   │   ├── example_docs_output
│       │   │   │   └── example_package.md
│       │   │   ├── example_package
│       │   │   │   ├── __init__.py
│       │   │   │   ├── main_module.py
│       │   │   │   └── submodule
│       │   │   │       └── __init__.py
│       │   │   └── test_add_docstrings_generator.py
│       │   └── test_license_script.py
│       ├── src
│       │   ├── __init__.py
│       │   ├── __pycache__
│       │   ├── core
│       │   │   ├── __init__.py
│       │   │   ├── __pycache__
│       │   │   ├── config_test.py
│       │   │   └── util_test.py
│       │   ├── run
│       │   │   ├── __init__.py
│       │   │   ├── __pycache__
│       │   │   ├── fetchers
│       │   │   │   └── __pycache__
│       │   │   ├── pipeline
│       │   │   │   ├── __init__.py
│       │   │   │   ├── __pycache__
│       │   │   │   └── test_pipeline.py
│       │   │   ├── test_pipeline.py
│       │   │   └── test_preparers
│       │   │       └── __pycache__
│       │   └── test_app_main.py
│       ├── test_orchestrator.py
│       ├── test_ticket_system_adapter.py
│       └── test_unified_models.py
├── open_ticket_ai.egg-info
├── package-lock.json
├── pyproject.toml
├── pytest.ini
├── README.md
└── uv.lock