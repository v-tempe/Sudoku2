from typing import Iterable

import pygame

import colors
import constants
from activity import Activity
from pygame_event_handler import PygameEventHandler
from drawable import Drawable
from pygame_draw_text import draw_text


class Menu(Activity, Drawable):
    def __init__(self, inscriptions: list[dict[str: str | int]]):
        self._event_handler = MenuEventHandler()
        self._view = MenuView()
        self._inscriptions: dict[str: tuple[int, int]] = inscriptions.copy()

    def get_event_handler(self) -> PygameEventHandler:
        return self._event_handler

    def get_view(self) -> Drawable:
        return self

    def _check_for_exit(self) -> bool:
        loaded_data = self._event_handler.get_loaded_data()
        for action in loaded_data:
            if action[constants.actions.keywords.ACTION] == constants.actions.commands.EXIT:
                return True
        return False

    def update(self):
        is_exit = self._check_for_exit()
        if is_exit:
            return None
        else:
            return self

    def draw(self, surf: pygame.surface.Surface):
        self._view.image.fill(colors.NAVY)
        for inscription in self._inscriptions:
            inscription: dict
            draw_text(self._view.image,
                      inscription[constants.menu.keywords.TEXT],
                      inscription[constants.menu.keywords.SIZE],
                      inscription[constants.menu.keywords.X],
                      inscription[constants.menu.keywords.Y],
                      inscription[constants.menu.keywords.COLOR])
        surf.blit(self._view.image, (0, 0))


class MenuEventHandler(PygameEventHandler):
    def __init__(self):
        self._loaded_data: list[dict[str: str]] = list()

    def process_event_quit(self):
        next_action = {
            constants.actions.keywords.ACTION: constants.actions.commands.EXIT
        }
        self._loaded_data.append(next_action)

    def get_loaded_data(self):
        return self._loaded_data.copy()


class MenuView(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((constants.WIDTH, constants.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.topleft = 0, 0
