from typing import Optional

import pygame

import colors
from pygame_draw_text import draw_text


class BlueCellView(pygame.sprite.Sprite):
    size = 100
    border_padding = 1

    STANDARD_COLOR = colors.LIGHT_GREY
    ACTIVE_COLOR = colors.AS_IF_WHITE

    def __init__(self, i: int, j: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((BlueCellView.size - BlueCellView.border_padding,
                                             BlueCellView.size - BlueCellView.border_padding))
        self.image.fill(BlueCellView.STANDARD_COLOR)
        self.rect = self.image.get_rect()
        self.rect.center = (i * BlueCellView.size + BlueCellView.size // 2,
                            j * BlueCellView.size + BlueCellView.size // 2)

    def draw(self, surf: pygame.surface.Surface, value: Optional[int], is_active: bool):
        self.image.fill(BlueCellView.ACTIVE_COLOR if is_active else BlueCellView.STANDARD_COLOR)
        if value is not None:
            draw_text(self.image, str(value), int(self.size * 0.8), self.size // 2, self.size // 2,
                      colors.BLUE)
        surf.blit(self.image, self.rect.topleft)
