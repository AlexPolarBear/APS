from abc import ABC, abstractmethod

from src.Model import Model


class Command(ABC):
    """Base class for all commands."""
    def __init__(self, model: Model):
        self._model: Model = model

    @abstractmethod
    def execute(self):
        raise NotImplementedError
