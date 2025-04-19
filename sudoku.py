from cell import Cell
from black_cell import BlackCell


class Sudoku:
    def __init__(self):
        self.grid: dict[tuple[int, int]: Cell] = {(i // 9, i % 9): BlackCell(None) for i in range(81)}

    def print(self):
        for j in range(9):
            for i in range(9):
                next_cell = self.grid[(j, i)]
                print(next_cell.true_value if next_cell.is_filled() else '_', '', end='')
            print()
