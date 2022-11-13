from typing import Set

from src.dataclasses import Button
import keyboard


class KeyboardHandler(object):
    def __init__(self, keys_to_track: Set[str]):
        self.keys_to_track = keys_to_track

    def get_user_button(self) -> Button:
        while True:
            event = keyboard.read_event()
            if event.name in self.keys_to_track and event.event_type == keyboard.KEY_DOWN:
                return Button(event.name)
