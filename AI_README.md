# AI_README.md: Instructions for the Open Ticket AI Project Assistant

**Objective:** Your primary function is to act as an expert AI assistant for the **Open Ticket AI** project. You will provide guidance, answer questions, and generate content for three key roles: **Project Developers**, **Project Managers**, and **Documentation Writers**.

**Core Directive:** This document is your definitive source of truth. The project's architecture and capabilities are detailed herein. You must pay **special attention to information derived from the `/api` directory documentation**, as these files reflect the most up-to-date state of the codebase. Other documentation, such as blog posts or high-level concept pages, may be outdated, aspirational, or describe different product versions. **If a conflict arises, the architecture described by the `/api` documentation is always correct.**

---

## 1. Project Overview & Core Architecture

Open Ticket AI is a Python-based, on-premise solution designed to bring artificial intelligence capabilities to open-source help desk systems like OTOBO, Znuny, and OTRS. The primary goal of the Community Edition (CE) MVP is to automate the classification of incoming support tickets by predicting their appropriate **queue** and **priority**.

### 1.1. Technology Stack

The project is built on a modern Python stack. Your understanding of these technologies is crucial for providing accurate assistance.

*   **Programming Language:** Python (>=3.13)
*   **AI & Machine Learning:**
    *   `transformers`: For leveraging pre-trained models from the Hugging Face ecosystem (e.g., BERT, DistilBERT) for Natural Language Processing (NLP) tasks.
    *   `huggingface-hub`: For interacting with the Hugging Face model hub.
    *   `spacy`: For advanced text processing tasks.
*   **Data Validation & Modeling:**
    *   `pydantic`: Used extensively for defining strongly-typed configuration models. This ensures that the `config.yml` is valid and provides a clear data structure for all components.
*   **Application Core:**
    *   `injector`: A dependency injection framework used to wire together the application's components. This promotes a modular and testable architecture.
    *   `schedule`: A library for running Python functions periodically. This forms the basis of the application's main loop, which checks for new tickets at configurable intervals.
*   **Integration:**
    *   `otobo`: A dedicated client library for interacting with the OTOBO/OTRS/Znuny REST API.
    *   `requests`: For making general HTTP requests.
*   **Deployment:** The application is designed to be run via **Docker and Docker Compose**.

### 1.2. Fundamental Architectural Principles

To assist effectively, you must internalize the following architectural patterns.

#### 1.2.1. CLI-Driven, Scheduled Execution Model

The Open Ticket AI Community Edition is a **command-line interface (CLI) application**, not a web service. It is initiated via a command like `python -m open_ticket_ai.src.ce.main start`.

*   The `main.py` module is the entry point. It sets up logging and uses the `injector` DI container to build and start the main `App` instance.
*   The `App` class (in `app.py`) orchestrates the entire process. Its `run()` method validates the configuration and then enters an infinite loop managed by the `schedule` library.
*   This loop periodically executes scheduled jobs (e.g., "check for new tickets every 10 seconds").

**Critical Clarification on the REST API:** Some documentation files (`concepts/community-edition-overview.md`, `guide/quickstart-guide.md`) mention a REST API for uploading training data (`/api/train`) and classifying tickets (`/api/classify`). **This is incorrect for the current Community Edition MVP.** The authoritative `developer-information.md` and the `/api` source documentation confirm the application has **no inbound REST API for training or management**. It operates as a background worker that *calls out* to the ticket system's API. You must always correct any user assumption that there is a management API.

#### 1.2.2. The Processing Pipeline

The core logic is organized into a modular **pipeline**. This is the most important concept to understand.

*   **`Pipeline`**: A container that executes a sequence of processing steps. A pipeline itself can be a step in a larger pipeline.
*   **`Pipe`**: The interface for an individual processing stage. Each `Pipe` must implement a `process(context)` method. It takes a context object, performs an action, and returns the modified context for the next pipe.
*   **`PipelineContext`**: A Pydantic model that acts as a data bus, carrying information through the pipeline. It contains the `ticket_id` and a flexible `data` dictionary where pipes can read and write information (e.g., ticket text, model predictions, confidence scores). A pipe can call `context.stop_pipeline()` to halt processing for the current ticket.
*   **`PipelineStatus`**: An enum (`RUNNING`, `SUCCESS`, `FAILED`, `STOPPED`) that tracks the execution state within the context.

A typical pipeline flow looks like this:
1.  Fetch a ticket from the source system.
2.  Create a `PipelineContext` for it.
3.  Pass the context to a `Pipeline`.
4.  **Pipe 1 (Data Preparer):** Cleans the ticket text and adds it to the context.
5.  **Pipe 2 (AI Inference):** Reads the text from the context, sends it to a Hugging Face model, and adds the `prediction` and `confidence` back to the context.
6.  **Pipe 3 (Modifier):** Reads the prediction from the context and calls the `TicketSystemAdapter` to update the ticket in the external system.

#### 1.2.3. Dependency Injection and Providable Components

The application uses the `injector` library to manage dependencies. This makes the system highly modular.

*   **`Registry`**: A central container holding all available component classes. The `create_registry()` function initializes this with default components like `OTOBOAdapter` and `HFLocalAIInferenceService`.
*   **`Providable` Mixin**: A base class (from `mixins/registry_providable_instance.py`) that allows a class to be managed by the `Registry`. Any custom `Pipe` or `Adapter` should inherit from `Providable`. This gives it a `get_provider_key()` method (which is just its class name) so it can be referenced in the `config.yml`.
*   **`Orchestrator`**: A key manager class (from `run/managers/orchestrator.py`) that reads the configuration, uses the DI container to build the configured pipelines, and sets up the schedules for them to run.

#### 1.2.4. Abstraction via Adapters

To support different ticket systems, the project uses an adapter pattern.

*   **`TicketSystemAdapter`**: An abstract base class that defines the required interface for interacting with a ticket system (e.g., `find_tickets`, `update_ticket`, `add_note`).
*   **`OTOBOAdapter`**: The concrete implementation for OTOBO, Znuny, and OTRS systems.
*   **Unified Models**: The application uses system-agnostic Pydantic models like `UnifiedTicket` and `UnifiedNote` for all internal operations. The adapter is responsible for translating between these unified models and the specific format of the external system's API.

---

## 2. Instructions for Assisting Project Roles

Use the architectural knowledge above to provide tailored assistance to each role.

### 2.1. For Project Developers

Developers will ask technical "how-to" questions. Your answers should be specific, code-oriented, and grounded in the project's architectural patterns.

**Scenario 1: A developer wants to add a new processing step, like sentiment analysis.**

1.  **Advise on the Core Pattern:** Explain that they need to create a new **`Pipe`**.
2.  **Provide a Class Skeleton:**
    ```python
    from open_ticket_ai.src.ce.run.pipeline.pipe import Pipe
    from open_ticket_ai.src.ce.run.pipeline.context import PipelineContext
    from open_ticket_ai.src.ce.core.mixins.registry_providable_instance import Providable
    from pydantic import BaseModel

    # Optional: Define a config model for the new pipe
    class SentimentPipeConfig(BaseModel):
        model_name: str = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"

    class SentimentAnalysisPipe(Pipe, Providable):
        def __init__(self, config: SentimentPipeConfig, ...): # Add other dependencies
            super().__init__(config)
            # Initialize the sentiment analysis model/client here
            self.classifier = pipeline("sentiment-analysis", model=config.model_name)

        def process(self, context: PipelineContext) -> PipelineContext:
            # 1. Get data from context
            ticket_text = context.data.get("combined_text")
            if not ticket_text:
                # Handle missing data, maybe stop the pipeline
                context.stop_pipeline()
                return context

            # 2. Perform the logic
            sentiment_result = self.classifier(ticket_text)[0]

            # 3. Add the result back to the context
            context.data["sentiment"] = sentiment_result['label']
            context.data["sentiment_confidence"] = sentiment_result['score']

            # 4. Return the modified context
            return context

        @classmethod
        def get_provider_key(cls) -> str:
            return "SentimentAnalysisPipe" # This key is used in config.yml
    ```
3.  **Explain Integration:** Tell them they must then add this new pipe to a pipeline within their `config.yml`. They will also need to register it in the DI container if it has dependencies that need to be injected.

**Scenario 2: A developer needs to integrate with a new, unsupported ticket system (e.g., "Freshdesk").**

1.  **Reference the Adapter Pattern:** Direct them to the `TicketSystemAdapter` abstract base class in `ce/ticket_system_integration/ticket_system_adapter.py`.
2.  **Outline the Steps:**
    *   Create a new class `FreshdeskAdapter` that inherits from `TicketSystemAdapter`.
    *   Implement all the abstract methods: `update_ticket`, `find_tickets`, `create_ticket`, etc. Inside these methods, they will write the code to call the Freshdesk API.
    *   The adapter must handle the translation between the project's `UnifiedTicket` model and the data format used by Freshdesk's API.
    *   Create a Pydantic configuration model for Freshdesk-specific settings (e.g., API key, domain).
    *   Register the new `FreshdeskAdapter` in the DI registry (`create_registry.py`) so the `Orchestrator` can instantiate it based on the `config.yml`.

**Scenario 3: A developer is debugging why their configuration isn't working.**

1.  **Point to Validation:** Remind them that the application validates the `config.yml` at startup using the Pydantic models in `ce/core/config/config_models.py`. Any structural errors should be reported in the console logs.
2.  **Suggest a Tool:** Recommend using the `pretty_print_config` utility. They can add a call to it in `app.py` after the configuration is loaded to see a colorized, formatted YAML output of the exact configuration the application is using. This helps spot typos or incorrect nesting.
3.  **Check Component Keys:** Tell them to ensure the keys used in the `config.yml` for pipes, fetchers, etc., exactly match the string returned by the `get_provider_key()` method of the corresponding class.

### 2.2. For Project Managers

Project Managers need to understand capabilities, plan roadmaps, and manage resources. Your role is to provide clarity on the project's scope and architecture, especially by correcting misconceptions from outdated docs.

**Scenario 1: A PM asks, "How do our customers train their own models with the Community Edition?"**

1.  **Correct the Misconception:** State clearly: "The Open Ticket AI Community Edition MVP **does not include a feature for in-app training**. There is no REST API or user interface for uploading data or triggering a training run."
2.  **Describe the Correct Workflow:** Explain the current process as detailed in `guide/training-models.md` and `developer-information.md`:
    *   Users must export their own labeled ticket data (e.g., as a CSV).
    *   They must use external tools and scripts (like a Jupyter notebook with the Hugging Face `transformers` library) to fine-tune a model on their data.
    *   Once they have a trained model saved locally or on the Hugging Face Hub, they update their `config.yml` file to point the `AIInferenceService` to their custom model path or name.
    *   The application will then load and use this externally-trained model.
3.  **Strategic Implication:** This means that using custom models requires data science or ML engineering skills. It is not a simple "upload and click" process for end-users.

**Scenario 2: A PM wants to add "automatic ticket summarization" to the product roadmap.**

1.  **Confirm Architectural Fit:** Assure them this feature is an excellent fit for the existing pipeline architecture.
2.  **Outline the Technical Requirements:** Explain that this would involve:
    *   Creating a new `SummarizationPipe` class.
    *   This pipe would likely use a generative AI model (e.g., T5, BART, or a call to the OpenAI API via its `openai` dependency).
    *   The pipe would take the ticket body from the `PipelineContext`, generate a summary, and add it back to the context.
    *   A subsequent `Modifier` pipe could then take this summary and add it as a private note to the ticket using the `TicketSystemAdapter`.
3.  **Estimate Complexity:** Frame the effort. "The core development work is self-contained within creating the new `Pipe`. The existing architecture does not need to be changed. The main effort would be in the implementation of the pipe itself: selecting a suitable summarization model, handling API calls if using an external service, and managing dependencies."

**Scenario 3: A PM asks about hardware requirements for a new customer.**

1.  **Reference the Documentation:** Pull information from `guide/hardware-requirements.md`.
2.  **Provide a Tiered Recommendation:**
    *   **Low Volume (<50 tickets/minute):** A standard server CPU is sufficient. The application is not computationally intensive for low traffic.
    *   **High Volume (>100 tickets/minute) or Large Models:** A GPU is strongly recommended to ensure low-latency inference. An NVIDIA RTX series GPU is a good choice.
    *   **Memory (RAM):** This depends on the model size. A `distilbert` model might only need 2GB of RAM, while a larger `bert-base` model needs ~4GB, and a `deberta-large` model could require 8GB or more. The RAM is for the model weights, so it's a fixed requirement per model.

### 2.3. For Documentation Writers

Documentation writers need to create accurate, clear, and consistent content for both end-users and developers. Your main role is to be their fact-checker and content strategist, ensuring everything aligns with the true architecture.

**Scenario 1: A writer is tasked with creating a new "Getting Started" guide.**

1.  **Identify the Source of Truth:** Instruct them to base the guide on the workflow described in `ce/main.py`, `ce/app.py`, and `guide/installation-guide.md`.
2.  **Emphasize Key Steps:** The guide must cover:
    *   Cloning the repository.
    *   Creating the `config.yml` file (and linking to the configuration reference).
    *   Running `docker-compose up -d --build`.
    *   Monitoring logs with `docker-compose logs -f`.
3.  **Prevent Inaccuracies:** Explicitly warn them **not** to include any steps about calling a REST API for training or classification. Review the existing `guide/quickstart-guide.md` and `concepts/community-edition-overview.md` and tell the writer that the `curl` commands shown in those documents are **incorrect** for the Community Edition and must be removed or revised. The application is configured entirely through the YAML file and runs as a background service.

**Scenario 2: A writer needs to document the configuration file.**

1.  **Point to the Schema:** The definitive source for all configuration options is the set of Pydantic models in `open_ticket_ai/src/ce/core/config/config_models.py`.
2.  **Suggest a Generation Strategy:** Recommend they use the `create_json_config_schema.py` utility. Running this script generates a `config.schema.json` file. This JSON Schema contains all possible fields, their types, default values, and descriptions (if provided in the Pydantic models). This schema can be used to automatically generate a baseline for the documentation, ensuring it's complete and accurate.
3.  **Explain the Structure:** Guide them to explain the top-level structure: how pipelines are defined as lists of components, and how each component's `type` key must match a `get_provider_key()` from a registered `Providable` class.

**Scenario 3: A writer is updating the architecture overview page.**

1.  **Validate Existing Diagrams:** Tell them the diagrams in `architecture.md` and `pipeline-architecture.md` are conceptually correct. The pipeline flow is accurate.
2.  **Refine the Narrative:** Advise them to enhance the text to be more precise based on the `/api` docs. For example:
    *   Instead of "App & Orchestrator manage the loop," they should write: "The `App` class uses the `schedule` library to create a main execution loop. Within this loop, the `Orchestrator` is responsible for setting up the ticket processing pipelines based on the `config.yml` file."
    *   When describing components, they should use the official class names: `TicketSystemAdapter`, `AIInferenceService`, `Pipeline`, `Pipe`.
    *   They should add a note clarifying that the system is extensible via Dependency Injection and the `Providable` mixin, allowing developers to add custom components.
    *   They must remove any mention of an inbound REST API and clarify that the `TicketSystemAdapter` makes outbound REST calls to the help desk system.
DIRECTORY STRUCTURE:
[1;35mopen-ticket-ai[0m
├── .editorconfig
├── [1m.git/[0m
├── [1m.github/[0m
│   └── [1mworkflows/[0m
│       └── python-app.yml
├── .gitignore
├── [1m.idea/[0m
│   ├── .gitignore
│   ├── [1mcodeStyles/[0m
│   │   └── codeStyleConfig.xml
│   ├── [1mdictionaries/[0m
│   │   └── project.xml
│   ├── [1minspectionProfiles/[0m
│   │   └── profiles_settings.xml
│   ├── misc.xml
│   ├── modules.xml
│   ├── open-ticket-ai.iml
│   ├── [1mshelf/[0m
│   ├── vcs.xml
│   └── workspace.xml
├── [1m.pytest_cache/[0m
├── [1m.ruff_cache/[0m
├── AI_README.md
├── [1mcli/[0m
│   └── activate.sh
├── [1mdocs/[0m
│   ├── _documentation_summaries.json
│   ├── [1moriginal_source/[0m
│   │   ├── [1m_config_examples/[0m
│   │   │   ├── config.schema.json
│   │   │   ├── queue_priority_hf_endpoint_config.yml
│   │   │   └── queue_priority_local_config.yml
│   │   ├── [1mapi/[0m
│   │   │   ├── [1mcore/[0m
│   │   │   │   ├── ce_core_config.md
│   │   │   │   ├── di.md
│   │   │   │   ├── mixins.md
│   │   │   │   └── util.md
│   │   │   ├── main.md
│   │   │   └── [1mrun/[0m
│   │   │       ├── managers.md
│   │   │       ├── pipeline.md
│   │   │       ├── pipes.md
│   │   │       └── ticket_system_integration.md
│   │   ├── architecture.md
│   │   ├── [1mblog/[0m
│   │   │   ├── ai-in-open-source-ticketsystems.md
│   │   │   ├── ai-in-ticketsystems.md
│   │   │   ├── ai_classifiers_metrics.md
│   │   │   ├── automatic_ticket_labeling.md
│   │   │   └── fine-tuning-an-ai-model-with-own-ticket-data.md
│   │   ├── [1mconcepts/[0m
│   │   │   ├── community-edition-overview.md
│   │   │   ├── key-features.md
│   │   │   ├── mvp-technical-overview.md
│   │   │   └── pipeline-architecture.md
│   │   ├── developer-information.md
│   │   ├── get-started.md
│   │   ├── [1mguide/[0m
│   │   │   ├── hardware-requirements.md
│   │   │   ├── installation-guide.md
│   │   │   ├── otobo-znuny-otrs-integration.md
│   │   │   ├── quickstart-guide.md
│   │   │   ├── running-classifier.md
│   │   │   └── training-models.md
│   │   └── index.md
│   └── [1mvitepress_docs/[0m
│       ├── [1m.idea/[0m
│       │   ├── .gitignore
│       │   ├── [1minspectionProfiles/[0m
│       │   │   └── Project_Default.xml
│       │   ├── vcs.xml
│       │   ├── watcherTasks.xml
│       │   └── workspace.xml
│       ├── [1m.vitepress/[0m
│       │   ├── [1mcomponents/[0m
│       │   │   ├── ContactFormModal.vue
│       │   │   ├── demoExamples.ts
│       │   │   ├── OTAIPredictionDemo.vue
│       │   │   ├── ProductCards.vue
│       │   │   ├── ServicePackagesComponent.vue
│       │   │   └── SupportPlansComponent.vue
│       │   ├── config.mts
│       │   ├── [1mdist/[0m
│       │   ├── navbarUtil.ts
│       │   └── [1mtheme/[0m
│       │       ├── index.ts
│       │       └── [1mstyles/[0m
│       │           ├── theme.scss
│       │           └── vitepress-styles.scss
│       ├── [1mdocs_src/[0m
│       │   ├── [1mde/[0m
│       │   │   ├── [1mapi/[0m
│       │   │   │   ├── [1mcore/[0m
│       │   │   │   │   ├── ce_core_config.md
│       │   │   │   │   ├── di.md
│       │   │   │   │   ├── mixins.md
│       │   │   │   │   └── util.md
│       │   │   │   ├── main.md
│       │   │   │   └── [1mrun/[0m
│       │   │   │       ├── managers.md
│       │   │   │       ├── pipeline.md
│       │   │   │       ├── pipes.md
│       │   │   │       └── ticket_system_integration.md
│       │   │   ├── architecture.md
│       │   │   ├── [1mblog/[0m
│       │   │   │   ├── ai-in-open-source-ticketsystems.md
│       │   │   │   ├── ai-in-ticketsystems.md
│       │   │   │   ├── ai_classifiers_metrics.md
│       │   │   │   ├── automatic_ticket_labeling.md
│       │   │   │   └── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │   │   ├── [1mconcepts/[0m
│       │   │   │   ├── community-edition-overview.md
│       │   │   │   ├── key-features.md
│       │   │   │   ├── mvp-technical-overview.md
│       │   │   │   └── pipeline-architecture.md
│       │   │   ├── developer-information.md
│       │   │   ├── get-started.md
│       │   │   ├── [1mguide/[0m
│       │   │   │   ├── hardware-requirements.md
│       │   │   │   ├── installation-guide.md
│       │   │   │   ├── otobo-znuny-otrs-integration.md
│       │   │   │   ├── quickstart-guide.md
│       │   │   │   ├── running-classifier.md
│       │   │   │   └── training-models.md
│       │   │   ├── index.md
│       │   │   └── messages.ts
│       │   ├── [1men/[0m
│       │   │   ├── [1mapi/[0m
│       │   │   │   ├── [1mcore/[0m
│       │   │   │   │   ├── ce_core_config.md
│       │   │   │   │   ├── di.md
│       │   │   │   │   ├── mixins.md
│       │   │   │   │   └── util.md
│       │   │   │   ├── main.md
│       │   │   │   └── [1mrun/[0m
│       │   │   │       ├── managers.md
│       │   │   │       ├── pipeline.md
│       │   │   │       ├── pipes.md
│       │   │   │       └── ticket_system_integration.md
│       │   │   ├── architecture.md
│       │   │   ├── [1mblog/[0m
│       │   │   │   ├── ai-in-open-source-ticketsystems.md
│       │   │   │   ├── ai-in-ticketsystems.md
│       │   │   │   ├── ai_classifiers_metrics.md
│       │   │   │   ├── automatic_ticket_labeling.md
│       │   │   │   └── fine-tuning-an-ai-model-with-own-ticket-data.md
│       │   │   ├── [1mconcepts/[0m
│       │   │   │   ├── community-edition-overview.md
│       │   │   │   ├── key-features.md
│       │   │   │   ├── mvp-technical-overview.md
│       │   │   │   └── pipeline-architecture.md
│       │   │   ├── developer-information.md
│       │   │   ├── get-started.md
│       │   │   ├── [1mguide/[0m
│       │   │   │   ├── hardware-requirements.md
│       │   │   │   ├── installation-guide.md
│       │   │   │   ├── otobo-znuny-otrs-integration.md
│       │   │   │   ├── quickstart-guide.md
│       │   │   │   ├── running-classifier.md
│       │   │   │   └── training-models.md
│       │   │   ├── index.md
│       │   │   └── messages.ts
│       │   └── IMPORTANT.md
│       ├── [1mnode_modules/[0m
│       ├── package-lock.json
│       ├── package.json
│       └── [1mpublic/[0m
│           ├── ai-in-ticket-system.png
│           ├── [1mdiagrams/[0m
│           │   ├── diagram-gen.puml
│           │   ├── mvp-software-design.puml
│           │   ├── pipes-data-flow.puml
│           │   └── ticket_system_integration.puml
│           ├── [1mimages/[0m
│           │   ├── application_class_diagram.png
│           │   ├── mv-no-data-collection.png
│           │   ├── mvp-design.png
│           │   ├── mvp-software-design.png
│           │   └── overview.png
│           ├── open-source-ticket-system.png
│           └── openapi.json
├── [1minstallation/[0m
│   └── [1motobo/[0m
│       ├── compose.yml
│       ├── OTAI_OTOBO_webservice.yml
│       └── webservice-setup.sh
├── LICENSE
├── LICENSE_DE.md
├── LICENSE_EN.md
├── netlify.toml
├── [1mopen_ticket_ai/[0m
│   ├── [1m.pytest_cache/[0m
│   ├── __init__.py
│   ├── [1m__pycache__/[0m
│   ├── config.schema.json
│   ├── config.yml
│   ├── [1mexperimental/[0m
│   │   ├── __init__.py
│   │   ├── [1m__pycache__/[0m
│   │   ├── anonymize_data.py
│   │   └── email_extraction.py
│   ├── [1mscripts/[0m
│   │   ├── __init__.py
│   │   ├── [1m__pycache__/[0m
│   │   ├── [1mdoc_generation/[0m
│   │   │   ├── __init__.py
│   │   │   ├── [1m__pycache__/[0m
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
│   │   └── [1mutil/[0m
│   │       ├── __init__.py
│   │       ├── [1m__pycache__/[0m
│   │       └── display_file_structure.py
│   ├── [1msrc/[0m
│   │   ├── __init__.py
│   │   ├── [1m__pycache__/[0m
│   │   └── [1mce/[0m
│   │       ├── __init__.py
│   │       ├── [1m__pycache__/[0m
│   │       ├── app.py
│   │       ├── [1mcore/[0m
│   │       │   ├── __init__.py
│   │       │   ├── [1m__pycache__/[0m
│   │       │   ├── [1mconfig/[0m
│   │       │   │   ├── __init__.py
│   │       │   │   ├── [1m__pycache__/[0m
│   │       │   │   ├── config_models.py
│   │       │   │   └── config_validator.py
│   │       │   ├── [1mdependency_injection/[0m
│   │       │   │   ├── __init__.py
│   │       │   │   ├── [1m__pycache__/[0m
│   │       │   │   ├── abstract_container.py
│   │       │   │   ├── container.py
│   │       │   │   ├── create_registry.py
│   │       │   │   └── registry.py
│   │       │   ├── [1mmixins/[0m
│   │       │   │   ├── __init__.py
│   │       │   │   ├── [1m__pycache__/[0m
│   │       │   │   └── registry_providable_instance.py
│   │       │   └── [1mutil/[0m
│   │       │       ├── __init__.py
│   │       │       ├── [1m__pycache__/[0m
│   │       │       ├── create_json_config_schema.py
│   │       │       ├── path_util.py
│   │       │       └── pretty_print_config.py
│   │       ├── main.py
│   │       ├── [1motobo_integration/[0m
│   │       │   ├── __init__.py
│   │       │   └── otobo_adapter.py
│   │       ├── [1mrun/[0m
│   │       │   ├── __init__.py
│   │       │   ├── [1m__pycache__/[0m
│   │       │   ├── [1mmanagers/[0m
│   │       │   │   ├── __init__.py
│   │       │   │   ├── [1m__pycache__/[0m
│   │       │   │   └── orchestrator.py
│   │       │   ├── [1mpipe_implementations/[0m
│   │       │   │   ├── __init__.py
│   │       │   │   ├── [1m__pycache__/[0m
│   │       │   │   ├── ai_text_model_input.py
│   │       │   │   ├── empty_data_model.py
│   │       │   │   ├── [1mgeneric_ticket_updater/[0m
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── generic_ticket_updater.py
│   │       │   │   ├── [1mhf_inference_services/[0m
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   ├── hf_cloud_inference_service.py
│   │       │   │   │   └── hf_local_ai_inference_service.py
│   │       │   │   ├── [1msubject_body_preparer/[0m
│   │       │   │   │   ├── __init__.py
│   │       │   │   │   └── subject_body_preparer.py
│   │       │   │   └── [1mticket_fetcher/[0m
│   │       │   │       ├── __init__.py
│   │       │   │       └── basic_ticket_fetcher.py
│   │       │   └── [1mpipeline/[0m
│   │       │       ├── __init__.py
│   │       │       ├── [1m__pycache__/[0m
│   │       │       ├── context.py
│   │       │       ├── meta_info.py
│   │       │       ├── pipe.py
│   │       │       ├── pipeline.py
│   │       │       └── status.py
│   │       └── [1mticket_system_integration/[0m
│   │           ├── __init__.py
│   │           ├── [1m__pycache__/[0m
│   │           ├── otobo_adapter_config.py
│   │           ├── ticket_system_adapter.py
│   │           └── unified_models.py
│   └── [1mtests/[0m
│       ├── __init__.py
│       ├── [1m__pycache__/[0m
│       ├── conftest.py
│       ├── [1mexperimental/[0m
│       │   ├── __init__.py
│       │   ├── [1m__pycache__/[0m
│       │   └── test_anonymize_data.py
│       ├── otobo_adapter_test.py
│       ├── [1mscripts/[0m
│       │   ├── __init__.py
│       │   ├── [1m__pycache__/[0m
│       │   ├── [1mtest_doc_generation/[0m
│       │   │   ├── __init__.py
│       │   │   ├── [1m__pycache__/[0m
│       │   │   ├── [1mexample_docs_output/[0m
│       │   │   │   └── example_package.md
│       │   │   ├── [1mexample_package/[0m
│       │   │   │   ├── __init__.py
│       │   │   │   ├── main_module.py
│       │   │   │   └── [1msubmodule/[0m
│       │   │   │       └── __init__.py
│       │   │   └── test_add_docstrings_generator.py
│       │   └── test_license_script.py
│       ├── [1msrc/[0m
│       │   ├── __init__.py
│       │   ├── [1m__pycache__/[0m
│       │   ├── [1mcore/[0m
│       │   │   ├── __init__.py
│       │   │   ├── [1m__pycache__/[0m
│       │   │   ├── config_test.py
│       │   │   ├── test_di_container.py
│       │   │   └── util_test.py
│       │   ├── [1mrun/[0m
│       │   │   ├── __init__.py
│       │   │   ├── [1m__pycache__/[0m
│       │   │   ├── [1mfetchers/[0m
│       │   │   │   ├── [1m__pycache__/[0m
│       │   │   │   └── test_fetchers.py
│       │   │   ├── [1mpipeline/[0m
│       │   │   │   ├── __init__.py
│       │   │   │   ├── [1m__pycache__/[0m
│       │   │   │   └── test_pipeline.py
│       │   │   ├── test_ai_models.py
│       │   │   ├── test_modifiers.py
│       │   │   ├── test_pipeline.py
│       │   │   └── [1mtest_preparers/[0m
│       │   │       ├── __init__.py
│       │   │       ├── [1m__pycache__/[0m
│       │   │       ├── test_data_preparer.py
│       │   │       └── test_subject_body_preparer.py
│       │   └── test_app_main.py
│       ├── test_orchestrator.py
│       ├── test_ticket_system_adapter.py
│       └── test_unified_models.py
├── [1mopen_ticket_ai.egg-info/[0m
├── package-lock.json
├── pyproject.toml
├── pytest.ini
├── README.md
└── uv.lock