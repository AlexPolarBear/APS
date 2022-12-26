from time import sleep
from typing import List

from src.GameClient.InputProvider import InputProvider
from src.dataclasses import Button


class StrSequenceInputProvider(InputProvider):
    """
    StrSequenceInputProvider class is responsible for generating user input from a string sequence.

    Parameters
    ----------
    str_sequence : List[str]
        List of strings which are used to generate user input.
    """

    def __init__(self, str_sequence: List[str]):
        self._str_sequence = str_sequence
        self._str_sequence_index = 0

    def get_user_button(self) -> Button:
        """Generate user input and return Button instance."""
        if self._str_sequence_index >= len(self._str_sequence):
            return Button('esc')
        button = Button(self._str_sequence[self._str_sequence_index])
        self._str_sequence_index += 1
        return button
