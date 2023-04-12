"""Operation Type module."""

from enum import Enum


class OperationTypeEnum(Enum):
    """Operation Type definition."""

    INSERT = 1
    UPDATE = 2
    DELETE = 3
