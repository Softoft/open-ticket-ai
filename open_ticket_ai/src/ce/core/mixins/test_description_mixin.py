import pytest

from open_ticket_ai.src.ce.core.mixins.description_mixin import DescriptionMixin


class DescribedClass(DescriptionMixin):
    pass


class CustomDescribedClass(DescriptionMixin):
    @staticmethod
    def get_description() -> str:
        return "This is a custom description."


def test_description_mixin_default_description():
    """
    Tests that a class using DescriptionMixin returns the default description
    if get_description is not overridden.
    """
    assert DescribedClass.get_description() == "No description provided."
    # Test instance access as well, though it's a static method
    instance = DescribedClass()
    assert instance.get_description() == "No description provided."


def test_description_mixin_custom_description():
    """
    Tests that a class using DescriptionMixin can override the get_description
    method to provide a custom description.
    """
    assert CustomDescribedClass.get_description() == "This is a custom description."
    # Test instance access as well
    instance = CustomDescribedClass()
    assert instance.get_description() == "This is a custom description."


def test_description_mixin_direct_call():
    """
    Tests calling get_description directly on the DescriptionMixin.
    """
    assert DescriptionMixin.get_description() == "No description provided."

class AnotherDescribedClass(DescriptionMixin):
    # No override
    pass

def test_description_mixin_multiple_classes():
    """
    Tests that multiple classes using DescriptionMixin work as expected,
    one with default and one with custom description.
    """
    assert DescribedClass.get_description() == "No description provided."
    assert CustomDescribedClass.get_description() == "This is a custom description."
    assert AnotherDescribedClass.get_description() == "No description provided."

    # Ensure they don't interfere
    custom_instance = CustomDescribedClass()
    default_instance = DescribedClass()
    another_default_instance = AnotherDescribedClass()

    assert custom_instance.get_description() == "This is a custom description."
    assert default_instance.get_description() == "No description provided."
    assert another_default_instance.get_description() == "No description provided."
