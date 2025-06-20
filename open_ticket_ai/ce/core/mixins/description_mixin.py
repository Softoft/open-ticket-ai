import abc


class DescriptionMixin:
    """
    Mixin to add a description to a class.
    """

    @staticmethod
    def get_description() -> str:
        return "No description provided."
