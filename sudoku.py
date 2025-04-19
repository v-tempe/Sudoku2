from cell import Cell
from black_cell import BlackCell
from blue_cell import BlueCell


class Sudoku:
    def __init__(self):
        def fill_grid():
            for j in range(9):
                for i in range(9):
                    cell_value = (i + (j // 3) + j * 3) % 9 + 1
                    self.grid[(j, i)].true_value = cell_value

        def weed_grid():
            from random import randint

            amount_left_cells = 50
            amount_discarded_cells = 81 - amount_left_cells
            coors_discarded_cells: set[tuple[int, int]] = set()
            for _ in range(amount_discarded_cells):
                coors_next: tuple[int, int] = randint(0, 8), randint(0, 8)
                if coors_next not in coors_discarded_cells:
                    self.replace_black_cell_with_blue_cell(coors_next)
                    coors_discarded_cells.add(coors_next)

        self.grid: dict[tuple[int, int]: Cell] = {(i // 9, i % 9): BlackCell(None) for i in range(81)}

        fill_grid()
        weed_grid()

    def replace_black_cell_with_blue_cell(self, coors: tuple[int, int]):
        old_cell = self.grid[coors]
        new_cell = BlueCell(old_cell.true_value)
        self.grid[coors] = new_cell

    def print(self):
        for j in range(9):
            for i in range(9):
                next_cell = self.grid[(j, i)]
                print(next_cell.announced_value if next_cell.is_filled() else '_', '', end='')
            print()
