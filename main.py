from typing import Optional

import constants.actions
from blue_cell import CellManager


def main():
    import user_interface
    from sudoku import Sudoku

    def process_actions():
        nonlocal running, sudoku, chosen_cell

        def process_choose():
            nonlocal chosen_cell
            chosen_cell = sudoku.get_cell_manager(int(action['x']), int(action['y']))

        def process_set_value():
            nonlocal chosen_cell
            if chosen_cell:
                chosen_cell.supply_value(action['value'])

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
            print(f"{command}")
            if command == constants.actions.commands.CHOOSE:
                process_choose()
            elif command == constants.actions.commands.SET_VALUE:
                process_set_value()
            elif command == constants.actions.commands.EXIT:
                process_exit()

    sudoku = Sudoku()

    chosen_cell: Optional[CellManager] = None

    running = True
    while running:
        actions: list[dict[str: str]] = list()
        raw_user_response = user_interface.text.get_raw_text_from_stdin(constants.actions.INPUT_PROMPT)
        next_action: dict[str: str] = user_interface.text.process_text_user_response(raw_user_response)
        actions.append(next_action)

        process_actions()


if __name__ == "__main__":
    main()
