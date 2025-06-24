import importlib
import pytest


def pytest_collection_modifyitems(config, items):
    """Skip heavy experimental tests if dependencies are missing.
    
    This pytest hook function checks for the availability of SpaCy and the German language model.
    If either is missing, it marks all tests in 'test_anonymize_data.py' to be skipped.
    
    Args:
        config (pytest.Config): The pytest configuration object.
        items (list[pytest.Item]): List of test items collected by pytest.
    """
    try:
        importlib.import_module("spacy")
        importlib.import_module("de_core_news_sm")
    except Exception:
        skip_reason = "SpaCy or the German model is not available"
        for item in list(items):
            if "test_anonymize_data.py" in str(item.fspath):
                item.add_marker(pytest.mark.skip(reason=skip_reason))