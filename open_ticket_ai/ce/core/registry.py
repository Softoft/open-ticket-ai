# --- registry + decorator ---------------------------------------------
from typing import Type, Dict

from open_ticket_ai.ce.run.classification.attribute_predictors.attribute_predictor import AttributePredictor
from open_ticket_ai.ce.run.fetchers.data_fetcher import DataFetcher
from open_ticket_ai.ce.run.modifiers.modifier import Modifier
from open_ticket_ai.ce.run.preparers.data_preparer import DataPreparer

REGISTRY: Dict[str, type] = {}


def provide_fetcher(key: str):
    """
    Decorator to register a DataFetcher subclass under a string key.
    """

    def decorator(cls: Type[DataFetcher]):
        REGISTRY[key] = cls
        return cls

    return decorator


def provide_modifier(key: str):
    """
    Decorator to register a DataFetcher subclass under a string key.
    """

    def decorator(cls: Type[Modifier]):
        REGISTRY[key] = cls
        return cls

    return decorator


def provide_preparer(key: str):
    """
    Decorator to register a DataFetcher subclass under a string key.
    """

    def decorator(cls: Type[DataPreparer]):
        REGISTRY[key] = cls
        return cls

    return decorator


def provide_attribute_predictor(key: str):
    """
    Decorator to register a DataFetcher subclass under a string key.
    """

    def decorator(cls: Type[AttributePredictor]):
        REGISTRY[key] = cls
        return cls

    return decorator


def does_registry_contain(key: str):
    return key in REGISTRY
