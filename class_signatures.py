import abc

class NoInitDocstring(abc.ABC):
    """This is an abstract base class without a docstring on its `__init__`."""

    def __init__(self, arg1: dict, arg2: list) -> None:
        pass

    @abc.abstractmethod
    def some_method(self) -> None:
        """We need an abstractmethod to make this an abstract base class."""
        
        pass

class WithInitDocstring(abc.ABC):
    """This is an abstract base class with a docstring on its `__init__`."""

    def __init__(self, arg1: dict, arg2: list) -> None:
        """This docstring is added to generate the correct class signature, but 
        it will not be used in the documentation output."""

        pass

    @abc.abstractmethod
    def some_method(self) -> None:
        """We need an abstractmethod to make this an abstract base class."""

        pass





