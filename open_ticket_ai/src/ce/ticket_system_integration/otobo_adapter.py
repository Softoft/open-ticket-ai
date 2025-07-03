"""Package for integrating with OTOBO systems.

This module provides the primary interface for OTOBO integration by exposing
the `OTOBOAdapter` class. It serves as the public API entry point for
interacting with OTOBO services.
"""

from ..otobo_integration.otobo_adapter import OTOBOAdapter

__all__ = ["OTOBOAdapter"]