from src.dataclasses import Button


class KeyboardHandler(object):
    def get_user_button(self) -> Button:
        raise NotImplementedError
