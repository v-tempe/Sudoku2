from typing import Optional
import pygame

import constants
import colors
from cell import Cell
from black_cell import BlackCell
from blue_cell import BlueCell, CellManager
from drawable import Drawable


class Sudoku(Drawable):
    def __init__(self):
        def fill_grid():
            for j in range(9):
                for i in range(9):
                    cell_value = (i + (j // 3) + j * 3) % 9 + 1
                    self._grid[(j, i)].true_value = cell_value

        def weed_grid():
            from random import randint

            amount_left_cells = 70
            amount_discarded_cells = 81 - amount_left_cells
            coors_discarded_cells: set[tuple[int, int]] = set()
            for _ in range(amount_discarded_cells):
                coors_next: tuple[int, int] = (randint(0, 8),
                                               randint(0, 8))
                if coors_next not in coors_discarded_cells:
                    self._replace_black_cell_with_blue_cell(coors_next)
                    coors_discarded_cells.add(coors_next)

        self._grid: dict[tuple[int, int]: Cell] = {
            (i % 9, i // 9):
            BlackCell(None, i % 9, i // 9) for i in range(81)
        }
        self._view = SudokuView()

        fill_grid()
        weed_grid()

    def _replace_black_cell_with_blue_cell(self, coors: tuple[int, int]):
        old_cell = self._grid[coors]
        new_cell = BlueCell(old_cell.true_value, old_cell.i, old_cell.j)
        self._grid[coors] = new_cell

    def print(self):
        for i in range(9):
            for j in range(9):
                next_cell = self._grid[(j, i)]
                print(next_cell.announced_value if next_cell.is_filled() else '_', '', end='')
            print()

    def get_cell_manager(self, x, y) -> Optional[CellManager]:
        if not (0 <= x <= 8):
            raise ValueError(f"'x' value must be an integer in [0; 8]; got {x}")
        if not (0 <= y <= 8):
            raise ValueError(f"'y' value must be an integer in [0; 8]; got {y}")

        target_cell = self._grid[(x, y)]
        if isinstance(target_cell, BlueCell):
            return CellManager(target_cell)
        else:
            return None

    def is_solved(self) -> bool:
        return all(map(lambda cell: cell.is_filled_correctly(), self._grid.values()))

    def draw(self, surf: pygame.surface.Surface):
        for coors in self._grid:
            cell = self._grid[coors]
            cell.draw(surf)
        self._view.draw(surf)

    @staticmethod
    def to_cell_dimensionality(coors: tuple[int, int]) -> tuple[int, int]:
        return coors[0] // Cell.size, coors[1] // Cell.size

    @staticmethod
    def to_display_dimensionality(coors: tuple[int, int]) -> tuple[int, int]:
        return coors[0] * Cell.size + Cell.size // 2, coors[1] * Cell.size + Cell.size // 2


class SudokuView:
    def __init__(self):
        self.borders = pygame.sprite.Group()
        self.make_borders()

    def make_borders(self):
        class Border(pygame.sprite.Sprite):
            def __init__(self, kind, x_or_y, width: int = 2):
                pygame.sprite.Sprite.__init__(self)
                if kind == 'v':
                    self.image = pygame.Surface((width, constants.HEIGHT))
                elif kind == 'h':
                    self.image = pygame.Surface((constants.WIDTH, width))
                else:
                    raise ValueError("the 'kind' value must be 'v' or 'h'")
                self.image.fill(colors.BLACK)
                self.rect = self.image.get_rect()
                if kind == 'v':
                    self.rect.center = (x_or_y, constants.HEIGHT // 2)
                elif kind == 'h':
                    self.rect.center = (constants.WIDTH // 2, x_or_y)
                else:
                    raise ValueError("the 'kind' value must be 'v' or 'h'")

        for i in range(1, 9):
            new_border = Border('v', i * Cell.size, 3 + (i % 3 == 0) * 3)
            new_border.add(self.borders)
        for j in range(1, 9):
            new_border = Border('h', j * Cell.size, 3 + (j % 3 == 0) * 3)
            new_border.add(self.borders)

    def draw(self, surf: pygame.surface.Surface):
        self.borders.draw(surf)
