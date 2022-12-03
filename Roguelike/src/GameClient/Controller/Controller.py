from abc import ABC, abstractmethod
from typing import Tuple, Dict, Any

from src import Model
from src.dataclasses import Button


class Controller(ABC):
    """
    Base class for all controllers.
    Interacts with user, converts user inputs to model API calls and manages UI.

    Parameters
    ----------
    model : Model
        Model instance which is controlled by this controller.

    Attributes
    ----------
    model : Model
        Model instance which is controlled by this controller.
    """
    @abstractmethod
    def __init__(self, model: Model):
        self.model = model

    @abstractmethod
    def process_button(self, button: Button) -> Tuple['Controller', Dict[str, Any]]:
        """Base method for processing user inputs."""
        pass
