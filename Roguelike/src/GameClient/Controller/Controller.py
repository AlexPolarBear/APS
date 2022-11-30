from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any

from src import Model
from src.dataclasses import Button


class Controller(ABC):
    @abstractmethod
    def __init__(self, model: Model):
        self.model = model

    @abstractmethod
    def process_button(self, button: Button) -> Tuple['Controller', Dict[str, Any]]:
        pass
