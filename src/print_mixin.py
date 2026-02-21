from typing import Any


class PrintMixin:
    """
    Mixin class that prints information about the object creation to the console.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Logs the class name and initialization arguments upon creation.
        Calls super().__init__() without arguments to safely reach object.__init__.
        """
        # Print the class name and all arguments used for creation
        print(f"{self.__class__.__name__}({', '.join([repr(a) for a in args])})")
        
        # super() here helps in multiple inheritance chains.
        # We call it without arguments because eventually it hits object.__init__
        # which takes no arguments.
        super().__init__()

    def __repr__(self) -> str:
        """Official string representation for debugging."""
        return f"{self.__class__.__name__}({self.__dict__})"
