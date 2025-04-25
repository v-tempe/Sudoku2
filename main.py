from typing import Optional

import colors
import constants.actions
from blue_cell import CellManager


def main():
    import pygame

    from sudoku import Sudoku

    def process_actions():
        nonlocal running, sudoku, chosen_cell

        def process_choose():
            nonlocal chosen_cell
            chosen_cell = sudoku.get_cell_manager(int(action['x']), int(action['y']))
            print(f"{chosen_cell=}")

        def process_set_value():
            nonlocal chosen_cell
            if chosen_cell:
                chosen_cell.supply_value(int(action['value']))

        def process_exit():
            nonlocal running
            running = False

        for action in actions:
            if constants.actions.keywords.INCORRECT_ACTION in action:
                continue

            if constants.actions.keywords.ACTION not in action:
                raise ValueError(f"Neither {constants.actions.keywords.ACTION} "
                                 f"nor {constants.actions.keywords.INCORRECT_ACTION} was provided")

            command = action[constants.actions.keywords.ACTION]
            if command == constants.actions.commands.CHOOSE:
                process_choose()
            elif command == constants.actions.commands.SET_VALUE:
                process_set_value()
            elif command == constants.actions.commands.EXIT:
                process_exit()

    def process_game_finishing():
        print(f"Sudoku is solved! Congratulations!")

    pygame.init()
    display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption(constants.GAME_NAME)
    clock = pygame.time.Clock()

    sudoku = Sudoku()

    chosen_cell: Optional[CellManager] = None

    running = True
    while running:
        is_sudoku_solved = sudoku.is_solved()
        if is_sudoku_solved:
            process_game_finishing()
            running = False
            continue

        actions: list[dict[str: str]] = list()

        for event in pygame.event.get():

            incorrect_action: dict[str: str] = {constants.actions.keywords.INCORRECT_ACTION: ""}
            next_action: dict[str: str] = incorrect_action.copy()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_coors: tuple[int, int] = event.pos

                coor_x, coor_y = sudoku.to_cell_dimensionality(click_coors)
                next_action = {constants.actions.keywords.ACTION: constants.actions.commands.CHOOSE,
                               constants.actions.keywords.X: coor_x,
                               constants.actions.keywords.Y: coor_y}
            elif event.type == pygame.KEYDOWN:
                key_char = event.unicode
                print(f"{key_char=}")

                if int(key_char) in range(1, 10):
                    next_action = {constants.actions.keywords.ACTION: constants.actions.commands.SET_VALUE,
                                   constants.actions.keywords.VALUE: key_char}
            elif event.type == pygame.QUIT:
                next_action = {constants.actions.keywords.ACTION: constants.actions.commands.EXIT}

            if next_action != incorrect_action:
                print(f"{next_action=}")
            actions.append(next_action)

        process_actions()

        display.fill(colors.BLACK)
        sudoku.draw(display)

        pygame.display.flip()

        clock.tick(constants.FPS)


if __name__ == "__main__":
    main()
