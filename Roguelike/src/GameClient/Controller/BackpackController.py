from typing import Tuple, Dict, Any

from src.Model import Model, Backpack
from src.GameClient.Controller import Controller
from src.GameClient.UI import BackpackUI
from src.dataclasses import Button


class BackpackController(Controller):
    """
    Controller specialization for the backpack view.
    Responsible for processing user input and updating model when player is in the backpack view.

    Parameters
    ----------
    model : Model
        Model instance which is controlled by this controller.

    Attributes
    ----------
    model : Model
        Model instance which is controlled by this controller.
    backpack : Backpack
        Backpack instance which is controlled by this controller.
    ui : MapUI
        UI instance responsible for rendering backpack view.
    selected_item_index : int
        Index of currently selected item in backpack.
    """
    def __init__(self, model: Model):
        super(BackpackController, self).__init__(model)
        self.backpack = model.backpack
        self.ui = BackpackUI(model.world_map.width, model.world_map.height)
        self.selected_item_index = 0

    def process_button(self, button: Button) -> Tuple[Controller, Dict[str, Any]]:
        """
        Process user input and update model accordingly in the backpack view.

        Parameters
        ----------
        button : Button
            Button instance which represents user input.

        Returns
        -------
        Tuple[Controller, Dict[str, Any]]
            Returns controller which takes control and dict with UI rendering info.
        """
        if button.key == 'tab':
            from src.GameClient.Controller import MapController
            return MapController(self.model), dict()

        elif button.key == 'space' and self.backpack:
            selected_item = self.backpack.get_item(self.selected_item_index)
            if selected_item.activated:
                self.model.deactivate_item(self.selected_item_index)
            else:
                self.model.activate_item(self.selected_item_index)

        elif button.key in {'up', 'down'} and self.backpack:
            if button.key == 'up':
                self.selected_item_index -= 1
            else:
                self.selected_item_index += 1
            self.selected_item_index %= len(self.backpack)

        return self, dict(selected_item_index=self.selected_item_index)
