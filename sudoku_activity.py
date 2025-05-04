from typing import Optional

from activity import Activity
from drawable import Drawable
from pygame_event_handler import PygameEventHandler
from sudoku import Sudoku
from blue_cell import CellManager
import constants


class SudokuActivity(Activity):
    def __init__(self, another_activities: Optional[dict] = None):
        self._sudoku: Sudoku = Sudoku()
        self._event_handler: PygameEventHandler = SudokuActivityEventHandler()
        self._chosen_cell: Optional[CellManager] = None
        self._actions_for_update: list[dict[str: str]] = list()
        self._known_activities: dict[str: SudokuActivity] = \
            another_activities.copy() if another_activities else dict()

    def _load_actions_for_update(self) -> None:
        self._actions_for_update.extend(self._event_handler.get_loaded_data())

    def get_event_handler(self) -> PygameEventHandler:
        self._load_actions_for_update()
        return self._event_handler

    def get_view(self) -> Drawable:
        return self._sudoku

    def update(self):
        def process_choose():
            self._chosen_cell = self._sudoku.get_cell_manager(int(action['x']), int(action['y']))
            self._chosen_cell.activate()

        def process_set_value():
            nonlocal value_for_return
            if self._chosen_cell:
                self._chosen_cell.supply_value(int(action['value']))

            if self._sudoku.is_solved():
                value_for_return = self._known_activities[constants.activities_names.GAME_FINISH]

        def process_exit():
            nonlocal value_for_return
            value_for_return = None

        self._load_actions_for_update()

        value_for_return = self
        for action in self._actions_for_update:
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
        return value_for_return


class SudokuActivityEventHandler(PygameEventHandler):
    def __init__(self):
        self._loaded_data: list[dict[str: str]] = list()

    def process_event_mousebuttondown(self, button: int, click_coors: tuple[int, int]):
        coor_x, coor_y = Sudoku.to_cell_dimensionality(click_coors)
        next_action = {
            constants.actions.keywords.ACTION: constants.actions.commands.CHOOSE,
            constants.actions.keywords.X: coor_x,
            constants.actions.keywords.Y: coor_y
        }
        self._loaded_data.append(next_action)

    def process_event_keydown(self, key, mod, key_char: str):
        if key_char.isdigit() and int(key_char) in range(1, 10):
            next_action = {
                constants.actions.keywords.ACTION: constants.actions.commands.SET_VALUE,
                constants.actions.keywords.VALUE: key_char
            }
            self._loaded_data.append(next_action)

    def process_event_quit(self):
        next_action = {
            constants.actions.keywords.ACTION: constants.actions.commands.EXIT
        }
        self._loaded_data.append(next_action)

    def get_loaded_data(self):
        return self._loaded_data.copy()
