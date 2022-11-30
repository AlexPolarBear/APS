from src import Model
import sys
from abc import ABC, abstractmethod


class UI(ABC):
    @abstractmethod
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    @abstractmethod
    def print(self, model: Model, erase_before: bool = True, **kwargs) -> None:
        pass

    def erase(self) -> None:
        for _ in range(self.height + 2):
            sys.stdout.write('\x1b[1A\x1b[2K')
            sys.stdout.flush()
