"""Account entity module."""


class Account:
    """Account entity."""

    def __init__(self, name: str, description: str, balance: float) -> None:
        self.__name = name
        self.__description = description
        self.__balance = balance

    @property
    def name(self) -> str:
        """Name getter."""
        return self.__name

    @name.setter
    def name(self, name):
        """Name setter."""
        self.__name = name

    @property
    def description(self) -> str:
        """Description getter."""
        return self.__description

    @description.setter
    def description(self, description: str):
        """Description setter."""
        self.__description = description

    @property
    def balance(self) -> float:
        """Balance getter."""
        return self.__balance

    @balance.setter
    def balance(self, balance: float):
        """Expiration date setter."""
        self.__balance = balance
