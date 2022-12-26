from typing import Set, Dict

import keyboard

from src.GameClient.InputProvider import InputProvider
from src.dataclasses import Button


class KeyboardInputProvider(InputProvider):
    """
    KeyboardInputProvider class is responsible for handling keyboard events.
    It reads user input and converts it to Button instances.

    Parameters
    ----------
    keys_to_track : Set[str]
        Set of keyboard keys which are tracked by the handler.
    key_mapping : Dict[str, str]
        Mapping of tracked keys to their aliases.
    """

    def __init__(self, keys_to_track: Set[str], key_mapping: Dict[str, str]):
        self._keys_to_track = keys_to_track
        self._key_mapping = key_mapping

    def get_user_button(self) -> Button:
        """Wait for user input and return Button instance."""
        while True:
            event = keyboard.read_event()
            if event.name in self._keys_to_track and event.event_type == keyboard.KEY_DOWN:
                pressed_key = event.name
                if pressed_key in self._key_mapping:
                    pressed_key = self._key_mapping[pressed_key]
                return Button(pressed_key)
