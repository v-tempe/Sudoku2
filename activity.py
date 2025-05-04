from pygame_event_handler import PygameEventHandler
from drawable import Drawable


class Activity:
    def get_event_handler(self) -> PygameEventHandler:
        raise TypeError(f"Method 'get_event_handler' must be overwritten in implementation")

    def get_view(self) -> Drawable:
        raise TypeError(f"Method 'get_view' must be overwritten in implementation")

    def update(self):
        raise TypeError(f"Method 'update' must be overwritten in implementation")
