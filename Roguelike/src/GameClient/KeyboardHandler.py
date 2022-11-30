from typing import Set, Dict

from src.dataclasses import Button
import keyboard


class KeyboardHandler(object):
    def __init__(self, keys_to_track: Set[str], key_mapping: Dict[str, str]):
        self.keys_to_track = keys_to_track
        self.key_mapping = key_mapping

    def get_user_button(self) -> Button:
        while True:
            event = keyboard.read_event()
            if event.name in self.keys_to_track and event.event_type == keyboard.KEY_DOWN:
                pressed_key = event.name
                if pressed_key in self.key_mapping:
                    pressed_key = self.key_mapping[pressed_key]
                return Button(pressed_key)
