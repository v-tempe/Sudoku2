from typing import Optional

import pygame

import colors
from pygame_draw_text import draw_text


class BlueCellView(pygame.sprite.Sprite):
    size = 100
    border_padding = 1

    STANDARD_COLOUR = colors.LIGHT_GREY

    def __init__(self, i: int, j: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((BlueCellView.size - BlueCellView.border_padding,
                                             BlueCellView.size - BlueCellView.border_padding))
        self.image.fill(BlueCellView.STANDARD_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (i * BlueCellView.size + BlueCellView.size // 2,
                            j * BlueCellView.size + BlueCellView.size // 2)

    def draw(self, surf: pygame.surface.Surface, value: Optional[int]):
        self.image.fill(BlueCellView.STANDARD_COLOUR)
        if value is not None:
            draw_text(self.image, str(value), int(self.size * 0.8), self.size // 2, self.size // 2,
                      colors.BLUE)
        surf.blit(self.image, self.rect.topleft)
