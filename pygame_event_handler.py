class PygameEventHandler:
    def pre_process_event(self):
        pass

    def process_event_mousebuttondown(self, button: int, pos: tuple[int, int]):
        print(f"{button=}")
        print(f"{pos=}")

    def process_event_keydown(self, key, mod, unicode: str):
        print(f"{key=}")
        print(f"{mod=}")
        print(f"{unicode=}")

    def process_event_quit(self):
        pass

    def post_process_event(self):
        pass

    def get_loaded_data(self):
        pass
