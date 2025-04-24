from typing import Optional

from cell import Cell


class BlueCell(Cell):
    def __init__(self, true_value: Optional[int]):
        Cell.__init__(self, true_value)

        self._supplied_value: Optional[int] = None

    @property
    def supplied_value(self):
        return self._supplied_value

    @supplied_value.setter
    def supplied_value(self, value: int):
        self._supplied_value = value

    @property
    def announced_value(self):
        return self._supplied_value

    def is_filled(self) -> bool:
        return self._supplied_value is not None


class CellManager:
    """
    A public API for a 'Cell' class
    """
    def __init__(self, cell: BlueCell):
        self._cell = cell

    @property
    def true_value(self):
        return self._cell.true_value

    @property
    def supplied_value(self):
        return self._cell.supplied_value

    def supply_value(self, value):
        self._cell.supplied_value = value
