---
description: Discover the Dependency Injection (DI) architecture of Open Ticket AI.
  This documentation explains how to create and use a Python class registry to manage
  core services like OTOBO integration, data preparation, and local Hugging Face AI
  inference.
---
# Documentation for `**/ce/core/dependency_injection/**/*.py`

## Module: `open_ticket_ai\src\ce\core\dependency_injection\abstract_container.py`



---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\container.py`



---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\create_registry.py`



### <span class='text-warning'>def</span> `create_registry() -> Registry`

Creates and configures the default class registry.
This function initializes a `Registry` instance and registers essential classes
required for the application's dependency injection system. The registered classes
include integration adapters, data preparers, and AI inference services.

The following classes are registered:
- `OTOBOAdapter`: Handles integration with the OTOBO ticket system.
- `SubjectBodyPreparer`: Prepares subject and body content for ticket processing.
- `HFLocalAIInferenceService`: Provides local AI inference using Hugging Face models.

**Returns:** (`Registry`) - A configured registry instance with all necessary classes registered.



---

## Module: `open_ticket_ai\src\ce\core\dependency_injection\registry.py`



---
