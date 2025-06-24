# tests/core/config_test.py

import pytest
from pydantic import ValidationError

from open_ticket_ai.src.ce.core.config import config_models


# --- Test Fixtures and Helper Functions ---

@pytest.fixture
def minimal_config_dict():
    """
    Build the smallest valid dict for OpenTicketAIConfig,
    with one fetcher, one preparer, one modifier and one predictor.
    """
    return {
        "system": {
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
                "id": "attribute_predictor_id_1",
                "provider_key": "dummy_predictor",
                "fetcher_id": "fetcher_id_1",
                "preparer_id": "preparer_id_1",
                "ai_inference_service_id": "ai_inference_service_id_1",
                "modifier_id": "modifier_id_1",
                "schedule": {"interval": 1, "unit": "seconds"},
                "params": {}
            }
        ]
    }


# --- Tests for SchedulerConfig ---

class TestSchedulerConfig:
    def test_valid_scheduler_config(self):
        sc = config_models.SchedulerConfig(interval=1, unit="seconds")
        assert sc.interval == 1
        assert sc.unit == "seconds"

    @pytest.mark.parametrize("interval", [0, -5])
    def test_scheduler_config_invalid_interval_raises_validation_error(self, interval):
        with pytest.raises(ValidationError):
            config_models.SchedulerConfig(interval=interval, unit="minutes")

    def test_scheduler_config_invalid_unit_raises_validation_error(self):
        with pytest.raises(ValidationError):
            config_models.SchedulerConfig(interval=5, unit="")


# --- Tests for OpenTicketAIConfig ---

class TestOpenTicketAIConfig:
    @pytest.mark.parametrize("list_name", [
        "fetchers", "data_preparers", "modifiers", "attribute_predictors", "ai_inference_services"
    ])
    def test_empty_list_for_core_components_raises_validation_error(self, list_name,
                                                                    minimal_config_dict):
        minimal_config_dict[list_name] = []
        with pytest.raises(ValidationError):
            config_models.OpenTicketAIConfig(**minimal_config_dict)

    def test_valid_open_ticket_ai_config_parses_correctly(self, minimal_config_dict):
        cfg = config_models.OpenTicketAIConfig(**minimal_config_dict)
        assert cfg.system.provider_key == "dummy_sys"
        assert len(cfg.fetchers) == 1
        assert cfg.fetchers[0].id == "fetcher_id_1"
        assert cfg.attribute_predictors[0].schedule.interval == 1

    @pytest.mark.parametrize(
        "list_name_to_alter, ref_id_field_in_predictor, expected_error_message_part",
        [
            ("fetchers", "fetcher_id", "refs unknown fetcher"),
            ("data_preparers", "preparer_id", "refs unknown preparer"),
            ("ai_inference_services", "ai_inference_service_id", "refs unknown model"),
            ("modifiers", "modifier_id", "refs unknown modifier"),
        ],
    )
    def test_invalid_cross_reference_raises_value_error(
        self, list_name_to_alter, ref_id_field_in_predictor, expected_error_message_part,
        minimal_config_dict
    ):
        # Make the reference invalid by changing the ID in the referenced list
        original_id = minimal_config_dict[list_name_to_alter][0]["id"]
        minimal_config_dict[list_name_to_alter][0]["id"] = "invalid_id_for_ref"

        # Update the predictor's reference to a non-existent ID
        minimal_config_dict["attribute_predictors"][0][
            ref_id_field_in_predictor] = "non_existent_id"

        with pytest.raises(ValueError) as exc:
            config_models.OpenTicketAIConfig(**minimal_config_dict)

        assert expected_error_message_part in str(exc.value)
        predictor_id = minimal_config_dict["attribute_predictors"][0]["id"]
        assert f"attribute_predictor '{predictor_id}'" in str(exc.value)
        assert "'non_existent_id'" in str(exc.value)

        # Restore original id to prevent interference with other parametrized tests if dict is somehow reused
        # (though pytest fixtures should typically prevent this for dicts)
        minimal_config_dict[list_name_to_alter][0]["id"] = original_id
        minimal_config_dict["attribute_predictors"][0][ref_id_field_in_predictor] = original_id

    def test_duplicate_ids_in_component_list_allowed_by_basemodel_but_picked_by_set_logic(self,
                                                                                          minimal_config_dict):
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
        # If a predictor references "fetcher_id_1", it should still be considered valid.
        minimal_config_dict["attribute_predictors"][0]["fetcher_id"] = "fetcher_id_1"
        cfg_instance_ref_ok = config_models.OpenTicketAIConfig(**minimal_config_dict)
        assert cfg_instance_ref_ok.attribute_predictors[0].fetcher_id == "fetcher_id_1"
        # Note: To strictly prevent duplicate IDs within a single list (e.g., two fetchers with the same ID),
        # a dedicated validator in `OpenTicketAIConfig` would be needed.


# --- Tests for load_config function ---

class TestLoadConfig:
    def test_load_config_missing_root_key_raises_key_error(self, tmp_path):
        p = tmp_path / "c.yaml"
        p.write_text("something_else: {}")
        with pytest.raises(KeyError) as exc:
            config_models.load_config(str(p))
        assert "Missing 'open_ticket_ai' root fetcher_key" in str(
            exc.value)  # Note: message is "root fetcher_key" which is a bit confusing
        # but this is the existing message. Consider revising if it's a typo.
