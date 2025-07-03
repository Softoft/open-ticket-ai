"""Public interface for unified models in the ticket system integration.

This module imports all public classes, functions, and variables from the unified_models module
(located in the parent package's `ticket_system_integration` package) using a wildcard import.
This provides convenient access to the unified models without requiring explicit imports.

## Purpose
Provides a single import point for accessing all unified ticket system models, simplifying
integration code and reducing import boilerplate throughout the application.

## Usage
Import this module to access all unified ticket system models:
"""

from .ticket_system_integration.unified_models import *