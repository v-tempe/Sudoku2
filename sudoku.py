from cell import Cell
from black_cell import BlackCell


class Sudoku:
    def __init__(self):
        def fill_grid():
            for j in range(9):
                for i in range(9):
                    cell_value = (i + (j // 3) + j * 3) % 9 + 1
                    self.grid[(j, i)].true_value = cell_value

        self.grid: dict[tuple[int, int]: Cell] = {(i // 9, i % 9): BlackCell(None) for i in range(81)}
        fill_grid()

    def print(self):
        for j in range(9):
            for i in range(9):
                next_cell = self.grid[(j, i)]
                print(next_cell.true_value if next_cell.is_filled() else '_', '', end='')
            print()
