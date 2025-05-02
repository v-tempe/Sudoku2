from typing import Optional
import pygame

from cell import Cell
from black_cell_view import BlackCellView
from drawable import Drawable


class BlackCell(Cell, Drawable):
    def __init__(self, true_value: Optional[int], i: int, j: int):
        Cell.__init__(self, true_value, i, j)
        self._view = BlackCellView(i, j)

    @Cell.true_value.setter
    def true_value(self, new_value):
        self._true_value = new_value

    @property
    def announced_value(self):
        return self._true_value

    def is_filled(self) -> bool:
        return self._true_value is not None

    def is_filled_correctly(self):
        return True

    def draw(self, surf: pygame.surface.Surface):
        self._view.draw(surf, self.true_value)
