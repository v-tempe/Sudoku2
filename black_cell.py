from typing import Optional
from cell import Cell


class BlackCell(Cell):
    def __init__(self, true_value: Optional[int]):
        Cell.__init__(self, true_value)

    @Cell.true_value.setter
    def true_value(self, new_value):
        self._true_value = new_value

    @property
    def announced_value(self):
        return self._true_value

    def is_filled(self) -> bool:
        return self._true_value is not None
