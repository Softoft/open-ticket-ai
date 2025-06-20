import abc


class DescriptionMixin:
    """
    Mixin to add a description to a class.
    """

    @staticmethod
    @abc.abstractmethod
    def get_description() -> str:
        pass
