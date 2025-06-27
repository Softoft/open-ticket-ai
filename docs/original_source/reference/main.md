# Documentation for `**/ce/*.py`

## Module: `open_ticket_ai\src\ce\app.py`


### <span style='color: #8E44AD;'>class</span> `App`

Main application entry point.


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `__init__(self, config: OpenTicketAIConfig, validator: OpenTicketAIConfigValidator, orchestrator: Orchestrator)`</summary>

Initialize the application.

**Parameters:**

- **`config`** () - Loaded configuration for the application.
- **`validator`** () - Validator used to check the configuration.
- **`orchestrator`** () - Orchestrator used to run attribute predictors.

</details>


<details>
<summary>#### <span style='font-size: 0.7em; background-color: #34495E; color: white; padding: 2px 6px; border-radius: 4px; vertical-align: middle;'>method</span> <span style='color: #2980B9;'>def</span> `run(self)`</summary>

Validate configuration and start the scheduler loop.
This method:
1. Validates the application configuration
2. Sets up scheduled jobs using the orchestrator
3. Enters an infinite loop to run pending scheduled tasks

</details>


---

## Module: `open_ticket_ai\src\ce\main.py`

Open Ticket AI CLI entry point.
This module provides the command-line interface for the Open Ticket AI application.
It configures logging levels and launches the main application.


### <span style='color: #2980B9;'>def</span> `main(verbose: bool, debug: bool)`

Configure logging based on CLI options.

**Parameters:**

- **`verbose`** (`bool`) - Enable INFO-level logging when True.
- **`debug`** (`bool`) - Enable DEBUG-level logging when True.



### <span style='color: #2980B9;'>def</span> `start()`

Initialize the container and start the application.



---
