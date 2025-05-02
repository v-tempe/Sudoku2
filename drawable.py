import pygame


class Drawable:
    def draw(self, surf: pygame.surface.Surface):
        raise ValueError(f"Method 'draw' must be overwritten in implementation")
