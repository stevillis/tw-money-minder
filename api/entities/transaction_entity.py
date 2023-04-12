"""Transaction entity module."""


class Transaction:
    """Transaction entity."""

    def __init__(
        self,
        name: str,
        description: str,
        value: float,
        transaction_type: str,
        account_id: int,
    ) -> None:
        self.__name = name
        self.__description = description
        self.__value = value
        self.__transaction_type = transaction_type
        self.__account_id = account_id

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
    def value(self) -> float:
        """Value getter."""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Value setter."""
        self.__value = value

    @property
    def transaction_type(self) -> str:
        """Transaction type getter."""
        return self.__transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type: str):
        """Transaction type setter."""
        self.__transaction_type = transaction_type

    @property
    def account_id(self) -> int:
        """Account id getter."""
        return self.__account_id

    @account_id.setter
    def account_id(self, account_id: int):
        """Account id setter."""
        self.__account_id = account_id
