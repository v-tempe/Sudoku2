from abc import ABC
from typing import Optional


class Cell(ABC):
    def __init__(self, true_value: Optional[int]):
        self._true_value: int = true_value

    @property
    def true_value(self):
        return self._true_value

    def is_filled(self) -> bool:
        raise TypeError(f"Method {Cell.is_filled.__name__} must be overwritten in subclass")

    def __repr__(self):
        return f"Cell({self._true_value})"

    def __str__(self):
        return self.__repr__()
