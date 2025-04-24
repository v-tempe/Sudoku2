from abc import ABC
from typing import Optional


class Cell(ABC):
    def __init__(self, true_value: Optional[int]):
        self._true_value: int = true_value

    @property
    def true_value(self):
        return self._true_value

    @property
    def announced_value(self):
        raise TypeError(f"Method 'announced_value' must be overwritten in subclass")

    def is_filled(self) -> bool:
        raise TypeError(f"Method 'is_filled' must be overwritten in subclass")

    def is_filled_correctly(self):
        raise TypeError(f"Method 'is_filled_correctly' must be overwritten in subclass")

    def __repr__(self):
        return f"Cell({self._true_value})"

    def __str__(self):
        return self.__repr__()
