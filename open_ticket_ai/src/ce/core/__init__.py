"""Lazy import helpers for dependency injection modules."""

__all__ = ["AbstractContainer", "Registry", "create_registry", "DIContainer"]

def __getattr__(name: str):
    if name == "AbstractContainer":
        from .dependency_injection.abstract_container import AbstractContainer
        return AbstractContainer
    if name == "Registry":
        from .dependency_injection.registry import Registry
        return Registry
    if name == "create_registry":
        from .dependency_injection.create_registry import create_registry
        return create_registry
    if name == "DIContainer":
        from .dependency_injection.container import DIContainer
        return DIContainer
    raise AttributeError(name)
