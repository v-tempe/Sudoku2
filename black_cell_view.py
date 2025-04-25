import pygame

import colors
from pygame_draw_text import draw_text


class BlackCellView(pygame.sprite.Sprite):
    size = 100
    border_padding = 1

    STANDARD_COLOUR = colors.LIGHT_GREY

    def __init__(self, i: int, j: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((BlackCellView.size - BlackCellView.border_padding,
                                             BlackCellView.size - BlackCellView.border_padding))
        self.image.fill(BlackCellView.STANDARD_COLOUR)
        self.rect = self.image.get_rect()
        self.rect.center = (i * BlackCellView.size + BlackCellView.size // 2,
                            j * BlackCellView.size + BlackCellView.size // 2)

    def draw(self, surf: pygame.surface.Surface, value: int):
        self.image.fill(BlackCellView.STANDARD_COLOUR)
        draw_text(self.image, str(value), int(self.size * 0.9), self.size // 2, self.size // 2,
                  colors.BLACK)
        surf.blit(self.image, self.rect.topleft)
