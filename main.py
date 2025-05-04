from typing import Optional

import colors
import constants.actions
from blue_cell import CellManager
from activity import Activity


def main():
    import pygame

    from sudoku_activity import SudokuActivity
    from menu import Menu

    pygame.init()
    display = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
    pygame.display.set_caption(constants.GAME_NAME)
    clock = pygame.time.Clock()

    game_finish_activity = Menu([])
    sudoku_activity = SudokuActivity({constants.activities_names.GAME_FINISH: game_finish_activity})

    next_active_activity: Activity = sudoku_activity

    running = True
    while running:
        active_activity = next_active_activity

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                active_activity\
                    .get_event_handler()\
                    .process_event_mousebuttondown(event.button, event.pos)
            elif event.type == pygame.KEYDOWN:
                active_activity\
                    .get_event_handler()\
                    .process_event_keydown(event.key, event.mod, event.unicode)
            elif event.type == pygame.QUIT:
                active_activity\
                    .get_event_handler()\
                    .process_event_quit()

        next_active_activity = active_activity.update()
        if not next_active_activity:
            running = False

        display.fill(colors.BLACK)
        active_activity.get_view().draw(display)

        pygame.display.flip()

        clock.tick(constants.FPS)


if __name__ == "__main__":
    main()
