---
description: Official documentation for the Open Ticket AI command-line interface
  (CLI) entry point. This guide covers main.py, detailing how to configure logging
  levels and launch the application.
---
# Documentation for `**/ce/*.py`

## Module: `open_ticket_ai\src\ce\app.py`



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
4. Displays a stylized startup banner using `pyfiglet`

The application follows a dependency injection pattern where all required
dependencies are resolved through the `DIContainer`.



---
