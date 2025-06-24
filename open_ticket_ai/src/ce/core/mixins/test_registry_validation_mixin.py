import pytest
from pydantic import ValidationError

from open_ticket_ai.src.ce.core.mixins.registry_validation_mixin import Registerable


def test_registerable_valid_provider_key():
    """
    Tests that Registerable model accepts a valid provider_key.
    """
    data = {"provider_key": "valid_key"}
    reg = Registerable(**data)
    assert reg.provider_key == "valid_key"


def test_registerable_provider_key_is_required():
    """
    Tests that provider_key is a required field in Registerable model.
    """
    with pytest.raises(ValidationError) as excinfo:
        Registerable()  # type: ignore
    assert "provider_key" in str(excinfo.value)
    # Pydantic v2 error messages have "Field required"
    assert "Field required" in str(excinfo.value)


def test_registerable_provider_key_min_length():
    """
    Tests that provider_key must have a minimum length of 1.
    """
    with pytest.raises(ValidationError) as excinfo:
        Registerable(provider_key="")
    assert "provider_key" in str(excinfo.value)
    # Pydantic v2 message for min_length is "String should have at least %s characters"
    # Using .lower() to make the check case-insensitive for "String".
    assert "string should have at least 1 character" in str(excinfo.value).lower()


def test_registerable_provider_key_various_valid_keys():
    """
    Tests Registerable with various valid provider_key values.
    """
    valid_keys = ["a", "1", "_", "long-provider-key_123"]
    for key in valid_keys:
        reg = Registerable(provider_key=key)
        assert reg.provider_key == key


def test_registerable_with_extra_fields():
    """
    Tests that Registerable model allows extra fields by default Pydantic behavior,
    if not configured otherwise. The mixin itself doesn't restrict this.
    """
    data = {"provider_key": "valid_key", "extra_field": "some_value"}
    # By default, Pydantic models ignore extra fields unless config forbids it.
    # If this test fails, it might be due to global Pydantic settings or a
    # future change in the Registerable model itself.
    try:
        reg = Registerable(**data)
        assert reg.provider_key == "valid_key"
        # Check if extra_field was ignored or accepted based on Pydantic version/config
        # For default Pydantic V2, extra fields are ignored unless model_config has extra = 'allow'
        assert not hasattr(reg, "extra_field")
    except ValidationError:
        # This would happen if extra fields were forbidden
        pytest.fail("Registerable model unexpectedly raised ValidationError for extra fields.")

class SubclassOfRegisterable(Registerable):
    specific_field: int

def test_subclass_of_registerable():
    """
    Tests that a subclass of Registerable correctly inherits and validates
    the provider_key, and also handles its own fields.
    """
    # Valid case
    data_valid = {"provider_key": "sub_key", "specific_field": 100}
    sub_reg_valid = SubclassOfRegisterable(**data_valid)
    assert sub_reg_valid.provider_key == "sub_key"
    assert sub_reg_valid.specific_field == 100

    # Invalid provider_key
    data_invalid_provider = {"provider_key": "", "specific_field": 100}
    with pytest.raises(ValidationError) as excinfo_provider:
        SubclassOfRegisterable(**data_invalid_provider)
    assert "provider_key" in str(excinfo_provider.value)
    assert "string should have at least 1 character" in str(excinfo_provider.value).lower()


    # Missing specific_field (should also fail)
    data_missing_specific = {"provider_key": "sub_key_2"}
    with pytest.raises(ValidationError) as excinfo_specific:
        SubclassOfRegisterable(**data_missing_specific) # type: ignore
    assert "specific_field" in str(excinfo_specific.value)
    assert "field required" in str(excinfo_specific.value).lower()
