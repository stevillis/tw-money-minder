"""Transaction Type module."""

from enum import Enum


class TransactionTypeEnum(Enum):
    """Transaction Type definition."""

    IN = 1
    OUT = 2
