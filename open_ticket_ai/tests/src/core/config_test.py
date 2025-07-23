# FILE_PATH: open_ticket_ai\tests\src\core\config_test.py
# tests/core/config_test.py
"""Tests for the configuration models and loading functionality.

This module contains unit tests for the configuration models (`SchedulerConfig`,
`OpenTicketAIConfig`) and the `load_config` function in the
`open_ticket_ai.src.ce.core.config.config_models` module.

The tests cover:
  - Validation of the `SchedulerConfig` model.
  - Validation of the `OpenTicketAIConfig` model, including:
      * Required components (non-empty lists for core components).
      * Correct parsing of a valid configuration.
      * Cross-referencing of components in pipelines.
      * Handling of duplicate component IDs.
  - The `load_config` function's behavior when the configuration file is missing the root key.

The tests use pytest fixtures and parametrization to cover various scenarios.
"""

import pytest
from pydantic import ValidationError

from open_ticket_ai.src.core.config import config_models

# --- Test Fixtures and Helper Functions ---

@pytest.fixture
def minimal_config_dict():
    """Build the smallest valid dict for ``OpenTicketAIConfig``.

    The config now follows the new pipe_ids and filters structure with
    ``pipelines`` instead of ``attribute_predictors``.

    Returns:
        dict: Minimal valid configuration dictionary for testing.
    """
    return {
        "system": {
            "id": "system_id",
            "provider_key": "dummy_sys",
            "params": {}
        },
        "fetchers": [
            {
                "id": "fetcher_id_1",
                "provider_key": "dummy_fetcher",
                "params": {}
            }
        ],
        "data_preparers": [
            {
                "id": "preparer_id_1",
                "provider_key": "dummy_preparer",
                "params": {}
            }
        ],
        "ai_inference_services": [
            {
                "id": "ai_inference_service_id_1",
                "provider_key": "dummy_model",
                "params": {}
            }
        ],
        "modifiers": [
            {
                "id": "modifier_id_1",
                "provider_key": "dummy_modifier",
                "params": {}
            }
        ],
        "pipelines": [
            {
                "id": "pipeline_id_1",
                "provider_key": "dummy_pipeline",
                "schedule": {"interval": 1, "unit": "seconds"},
                "pipe_ids": [
                    "fetcher_id_1",
                    "preparer_id_1",
                    "ai_inference_service_id_1",
                    "modifier_id_1",
                ],
                "params": {}
            }
        ]
    }


# --- Tests for SchedulerConfig ---

class TestSchedulerConfig:
    """Test cases for validating the SchedulerConfig model."""

    def test_valid_scheduler_config(self):
        """Tests that a valid scheduler configuration is parsed correctly."""
        sc = config_models.SchedulerConfig(interval=1, unit="seconds")
        assert sc.interval == 1
        assert sc.unit == "seconds"

    @pytest.mark.parametrize("interval", [0, -5])
    def test_scheduler_config_invalid_interval_raises_validation_error(self, interval):
        """Tests validation error when scheduler interval is non-positive.

        Args:
            interval (int): Invalid interval value to test.
        """
        with pytest.raises(ValidationError):
            config_models.SchedulerConfig(interval=interval, unit="minutes")

    def test_scheduler_config_invalid_unit_raises_validation_error(self):
        """Tests validation error when scheduler unit is invalid."""
        with pytest.raises(ValidationError):
            config_models.SchedulerConfig(interval=5, unit="")


# --- Tests for OpenTicketAIConfig ---

class TestOpenTicketAIConfig:
    """Test cases for validating the OpenTicketAIConfig model."""

    @pytest.mark.parametrize("list_name", [
        "fetchers",
        "data_preparers",
        "modifiers",
        "ai_inference_services",
        "pipelines",
    ])
    def test_empty_list_for_core_components_raises_validation_error(self, list_name,
                                                                    minimal_config_dict):
        """Tests validation error when core component lists are empty.

        Args:
            list_name (str): Name of the component list to empty.
            minimal_config_dict (dict): Minimal valid configuration fixture.
        """
        minimal_config_dict[list_name] = []
        with pytest.raises(ValidationError):
            config_models.OpenTicketAIConfig(**minimal_config_dict)

    def test_valid_open_ticket_ai_config_parses_correctly(self, minimal_config_dict):
        """Tests successful parsing of a valid configuration.

        Args:
            minimal_config_dict (dict): Minimal valid configuration fixture.
        """
        cfg = config_models.OpenTicketAIConfig(**minimal_config_dict)
        assert cfg.system.provider_key == "dummy_sys"
        assert len(cfg.fetchers) == 1
        assert cfg.fetchers[0].id == "fetcher_id_1"
        assert cfg.pipelines[0].schedule.interval == 1

    @pytest.mark.parametrize(
        "list_name_to_alter, pipe_index, expected_error_message_part",
        [
            ("fetchers", 0, "unknown pipe component"),
            ("data_preparers", 1, "unknown pipe component"),
            ("ai_inference_services", 2, "unknown pipe component"),
            ("modifiers", 3, "unknown pipe component"),
        ],
    )
    def test_invalid_cross_reference_raises_value_error(
        self, list_name_to_alter, pipe_index, expected_error_message_part,
        minimal_config_dict
    ):
        """Tests validation error when pipeline references invalid components.

        Args:
            list_name_to_alter (str): Component list to modify.
            pipe_index (int): Index in pipeline's pipe_ids to modify.
            expected_error_message_part (str): Expected substring in error message.
            minimal_config_dict (dict): Minimal valid configuration fixture.
        """
        # Make the reference invalid by changing the ID in the referenced list
        original_id = minimal_config_dict[list_name_to_alter][0]["id"]
        minimal_config_dict[list_name_to_alter][0]["id"] = "invalid_id_for_ref"

        # Update the pipeline's reference to a non-existent ID
        minimal_config_dict["pipelines"][0]["pipe_ids"][pipe_index] = "non_existent_id"

        with pytest.raises(ValueError) as exc:
            config_models.OpenTicketAIConfig(**minimal_config_dict)

        assert expected_error_message_part in str(exc.value)
        pipeline_id = minimal_config_dict["pipelines"][0]["id"]
        assert pipeline_id in str(exc.value)
        assert "non_existent_id" in str(exc.value)

        # Restore original id to prevent interference with other parametrized tests if dict is somehow reused
        # (though pytest fixtures should typically prevent this for dicts)
        minimal_config_dict[list_name_to_alter][0]["id"] = original_id
        minimal_config_dict["pipelines"][0]["pipe_ids"][pipe_index] = original_id

    def test_duplicate_ids_in_component_list_allowed_by_b_but_picked_by_set_logic(self,
                                                                                          minimal_config_dict):
        """Tests behavior when duplicate component IDs exist in component lists.

        Verifies:
          1. Duplicate IDs are allowed during parsing.
          2. Pipeline references resolve correctly using set-based lookup.

        Args:
            minimal_config_dict (dict): Minimal valid configuration fixture.
        """
        # This test clarifies behavior rather than strictly enforcing a "fail" for duplicates,
        # as Pydantic itself doesn't prevent duplicate dicts in a list by default.
        # The cross-validation logic uses sets, so it will effectively use one of the definitions.
        minimal_config_dict["fetchers"].append({
            "id": "fetcher_id_1",  # Duplicate ID
            "provider_key": "another_fetcher",
            "params": {}
        })

        # Should not raise ValidationError during parsing for duplicates in list
        cfg_instance = config_models.OpenTicketAIConfig(**minimal_config_dict)
        assert len(cfg_instance.fetchers) == 2

        # Cross-validation will use the set of IDs, so "fetcher_id_1" is known.
        # If a pipeline references "fetcher_id_1" it should still be considered valid.
        minimal_config_dict["pipelines"][0]["pipe_ids"][0] = "fetcher_id_1"
        cfg_instance_ref_ok = config_models.OpenTicketAIConfig(**minimal_config_dict)
        assert cfg_instance_ref_ok.pipelines[0].pipe_ids[0] == "fetcher_id_1"
        # Note: To strictly prevent duplicate IDs within a single list (e.g., two fetchers with the same ID),
        # a dedicated validator in `OpenTicketAIConfig` would be needed.


# --- Tests for load_config function ---

class TestLoadConfig:
    """Test cases for the load_config function."""

    def test_load_config_missing_root_key_raises_key_error(self, tmp_path):
        """Tests KeyError when configuration file lacks root key.

        Args:
            tmp_path (pathlib.Path): Temporary directory fixture.
        """
        p = tmp_path / "c.yaml"
        p.write_text("something_else: {}")
        with pytest.raises(KeyError) as exc:
            config_models.load_config(str(p))
        assert "Missing 'open_ticket_ai' root key" in str(exc.value)
