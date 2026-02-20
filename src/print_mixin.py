from typing import Any


class PrintMixin:
    """
    Mixin class that prints information about the object creation to the console.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        Logs the class name and initialization arguments upon creation.
        """
        # Note: We represent the object being created.
        # Per requirements: "prints information to the console about which class
        # and with what parameters the object was created."
        print(f"{self.__class__.__name__}({', '.join([repr(a) for a in args])})")
