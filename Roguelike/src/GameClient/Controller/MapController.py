from typing import Tuple, Dict, Any

from src.GameClient.Controller import Controller
from src.GameClient.UI import MapUI
from src.Model.Map.Map import Direction
from src.dataclasses import Button

"""Maps user inputs to model API calls."""
key_to_direction = {
    'up': Direction.UP,
    'left': Direction.LEFT,
    'right': Direction.RIGHT,
    'down': Direction.DOWN,
}


class MapController(Controller):
    """
    Controller specialization for the map view.
    Responsible for processing user input and updating model when player is in the map view.

    Parameters
    ----------
    model : Model
        Model instance which is controlled by this controller.

    Attributes
    ----------
    model : Model
        Model instance which is controlled by this controller.
    ui : MapUI
        UI instance responsible for rendering map view.
    """
    def __init__(self, model):
        super(MapController, self).__init__(model)
        self.ui = MapUI(model.world_map.width, model.world_map.height)

    def process_button(self, button: Button) -> Tuple[Controller, Dict[str, Any]]:
        """
        Process user input and update model accordingly in the map view.

        Parameters
        ----------
        button : Button
            Button instance which represents user input.

        Returns
        -------
        Tuple[Controller, Dict[str, Any]]
            Returns controller which takes control and dict with UI rendering info.
        """
        if button.key == 'shift':
            from src.GameClient.Controller import InspectionController
            return InspectionController(self.model), dict(selected_enemy_index=0)

        if button.key == 'tab':
            from src.GameClient.Controller import BackpackController
            return BackpackController(self.model), dict(selected_item_index=0)

        elif button.key in {'up', 'left', 'down', 'right'}:
            self.model.move(key_to_direction[button.key])

        return self, dict()
