from typing import Optional
import pygame

from cell import Cell
from blue_cell_view import BlueCellView
from drawable import Drawable


class BlueCell(Cell, Drawable):
    def __init__(self, true_value: Optional[int], i: int, j: int):
        Cell.__init__(self, true_value, i, j)
        self._supplied_value: Optional[int] = None
        self._view = BlueCellView(i, j)
        self._is_active = False

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

    def is_filled_correctly(self):
        return self._true_value == self._supplied_value

    def draw(self, surf: pygame.surface.Surface):
        self._view.draw(surf, self.supplied_value, self._is_active)

    def activate(self):
        self._is_active = True

    def deactivate(self):
        self._is_active = False


class CellManager:
    """
    A public API for a 'Cell' class
    """
    def __init__(self, cell: BlueCell):
        self._cell: BlueCell = cell

    def __del__(self):
        self.deactivate()

    @property
    def true_value(self):
        return self._cell.true_value

    @property
    def supplied_value(self):
        return self._cell.supplied_value

    def supply_value(self, value):
        self._cell.supplied_value = value

    def activate(self):
        self._cell.activate()

    def deactivate(self):
        self._cell.deactivate()
