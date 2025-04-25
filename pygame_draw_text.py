import pygame

import colors


font_name = pygame.font.match_font('arial')


def draw_text(surf: pygame.Surface, text: str | bytes, size: int, x: int, y: int,
              colour: tuple[int, int, int] = colors.WHITE):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)
