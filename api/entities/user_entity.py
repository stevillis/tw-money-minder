"""User entity module."""


class User:
    """User entity."""

    def __init__(self, name: str, email: str, password: str) -> None:
        self.__name = name
        self.__email = email
        self.__password = password

    @property
    def name(self):
        """Name getter."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Name setter."""
        self.__name = name

    @property
    def email(self) -> str:
        """Email getter."""
        return self.__email

    @email.setter
    def email(self, email: str) -> None:
        """Email setter."""
        self.__email = email

    @property
    def password(self) -> str:
        """Password getter."""
        return self.__password

    @password.setter
    def password(self, password: str) -> None:
        """Password setter."""
        self.__password = password
