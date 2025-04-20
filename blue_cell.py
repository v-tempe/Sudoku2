from typing import Optional

from cell import Cell


class BlueCell(Cell):
    def __init__(self, true_value: Optional[int]):
        Cell.__init__(self, true_value)

        self._supplied_value: Optional[int] = None

    @property
    def supplied_value(self):
        return self._supplied_value

    @property
    def announced_value(self):
        return self._supplied_value

    def is_filled(self) -> bool:
        return self._supplied_value is not None
