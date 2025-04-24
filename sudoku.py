from typing import Optional

from cell import Cell
from black_cell import BlackCell
from blue_cell import BlueCell, CellManager


class Sudoku:
    def __init__(self):
        def fill_grid():
            for j in range(9):
                for i in range(9):
                    cell_value = (i + (j // 3) + j * 3) % 9 + 1
                    self._grid[(j, i)].true_value = cell_value

        def weed_grid():
            from random import randint

            amount_left_cells = 79
            amount_discarded_cells = 81 - amount_left_cells
            coors_discarded_cells: set[tuple[int, int]] = set()
            for _ in range(amount_discarded_cells):
                coors_next: tuple[int, int] = randint(0, 8), randint(0, 8)
                if coors_next not in coors_discarded_cells:
                    self._replace_black_cell_with_blue_cell(coors_next)
                    coors_discarded_cells.add(coors_next)

        self._grid: dict[tuple[int, int]: Cell] = {(i % 9, i // 9): BlackCell(None) for i in range(81)}

        fill_grid()
        weed_grid()

    def _replace_black_cell_with_blue_cell(self, coors: tuple[int, int]):
        old_cell = self._grid[coors]
        new_cell = BlueCell(old_cell.true_value)
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
