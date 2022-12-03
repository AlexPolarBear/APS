from src import Model
import sys
from abc import ABC, abstractmethod


class UI(ABC):
    """
    Base class for all UIs.
    Renders game state for user.

    Parameters
    ----------
    width : int
        Width of the UI.
    height : int
        Height of the UI.

    Attributes
    ----------
    width : int
        Width of the UI.
    height : int
        Height of the UI.
    """
    @abstractmethod
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def print(self, model: Model, erase_before: bool = True, **kwargs) -> None:
        """
        Base method for rendering game to user.

        Parameters
        ----------
        model : Model
            Model instance which contains necessary for rendering data.
        erase_before : bool
            If True, erase previous UI frame before rendering new one.
        kwargs : dict
            Additional keyword arguments for rendering customization.
        """
        pass

    def erase(self) -> None:
        """
        Erase UI from the screen.
        Works only on ANSI-capable terminals.
        """
        for _ in range(self.height + 4):
            sys.stdout.write('\x1b[1A\x1b[2K')
            sys.stdout.flush()
