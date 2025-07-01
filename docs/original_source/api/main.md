---
description: Explore the documentation for the OpenTicketAI core engine. This guide
  details the main `App` class in `app.py`, which orchestrates configuration validation
  and job scheduling. It also covers `main.py`, the command-line interface (CLI) entry
  point that initializes the application, configures logging, and launches the system
  using dependency injection.
---
# Documentation for `**/ce/*.py`

## Starting the application

Run the service from the command line:

```bash
python -m open_ticket_ai.src.ce.main start
```

This command initializes the dependency injection container and launches the
configured pipelines.

## Module: `open_ticket_ai\src\ce\app.py`

Main application module for OpenTicketAI.
This module contains the `App` class which serves as the primary entry point
for the OpenTicketAI system. It orchestrates configuration validation, job
scheduling, and continuous execution of scheduled tasks.

### <span style='text-info'>class</span> `App`

Main application entry point for the OpenTicketAI system.
This class initializes and runs the core application components including:
- Configuration management
- Configuration validation
- Job orchestration and scheduling

The application follows a scheduled execution model where jobs are run at
predefined intervals.

**Parameters:**

- **`config`** () - Loaded application configuration.
- **`validator`** () - Configuration validator instance.
- **`orchestrator`** () - Job orchestration manager.


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `__init__(self, config: OpenTicketAIConfig, validator: OpenTicketAIConfigValidator, orchestrator: Orchestrator)`
Initialize the application with dependencies.

**Parameters:**

- **`config`** () - Loaded configuration for the application containing all
necessary parameters and settings.
- **`validator`** () - Validator instance used to check the integrity and
correctness of the configuration.
- **`orchestrator`** () - Orchestrator instance responsible for setting up and
managing scheduled jobs and attribute predictors.

:::


::: details #### <Badge type="info" text="method"/> <span class='text-warning'>def</span> `run(self)`
Main execution method for the application.
Performs the following operations:
1. Validates the application configuration
2. Sets up scheduled jobs using the orchestrator
3. Enters an infinite loop to execute pending scheduled tasks

The method first validates the configuration registry. If validation fails,
an error is logged and the application proceeds to setup schedules without
valid configuration (which may cause runtime errors). On successful validation,
a success message is printed.

After setup, the method enters a continuous loop that:
- Checks for pending scheduled jobs every second
- Executes any pending jobs found

:::


---

## Module: `open_ticket_ai\src\ce\main.py`

Open Ticket AI CLI entry point.
This module provides the command-line interface for the Open Ticket AI application.
It configures logging levels and launches the main application.


### <span class='text-warning'>def</span> `main(verbose: bool, debug: bool)`

Configure logging based on CLI options.
This function sets the logging level for the application based on the provided command-line flags.
It supports two levels of verbosity:
- `--verbose` for INFO level logging
- `--debug` for DEBUG level logging

If no flags are provided, the default logging level is WARNING. The function also configures
log formatting and suppresses noisy libraries (e.g., urllib3).

**Parameters:**

- **`verbose`** (`bool`) - Enable INFO-level logging when True.
- **`debug`** (`bool`) - Enable DEBUG-level logging when True.



### <span class='text-warning'>def</span> `start()`

Initialize the container and start the application.
This command performs the following actions:
1. Configures the dependency injection container
2. Retrieves the main application instance from the container
3. Runs the application
4. Displays a stylized startup banner using pyfiglet

The application follows a dependency injection pattern where all required
dependencies are resolved through the DIContainer.



---
