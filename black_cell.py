from typing import Optional
from cell import Cell


class BlackCell(Cell):
    def __init__(self, true_value: Optional[int]):
        Cell.__init__(self, true_value)

    def is_filled(self) -> bool:
        return self._true_value is not None
