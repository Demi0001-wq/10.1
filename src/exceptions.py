class QuantityError(Exception):
    """
    Exception raised when a product has an invalid quantity (e.g., zero).
    """
    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"{self.message}"
