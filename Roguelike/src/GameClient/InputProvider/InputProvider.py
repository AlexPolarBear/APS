from abc import ABC, abstractmethod

from src.dataclasses import Button


class InputProvider(ABC):
    """InputProvider class is responsible for reading user input and converting it to Button instances."""

    @abstractmethod
    def get_user_button(self) -> Button:
        """Wait for user input and return Button instance."""
        raise NotImplementedError
