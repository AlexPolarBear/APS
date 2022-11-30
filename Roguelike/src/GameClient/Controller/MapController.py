from typing import Tuple, Dict, Any

from src.GameClient.Controller import Controller
from src.GameClient.UI import MapUI
from src.Model.Map import Direction
from src.dataclasses import Button

key_to_direction = {
    'up': Direction.UP,
    'left': Direction.LEFT,
    'right': Direction.RIGHT,
    'down': Direction.DOWN,
}


class MapController(Controller):
    def __init__(self, model):
        super(MapController, self).__init__(model)
        self.ui = MapUI(model.get_map().width, model.get_map().height)

    def process_button(self, button: Button) -> Tuple[Controller, Dict[str, Any]]:
        if button.key == 'tab':
            from src.GameClient.Controller import BackpackController
            return BackpackController(self.model), dict(selected_item_index=0)

        elif button.key in {'up', 'left', 'down', 'right'}:
            self.model.move(key_to_direction[button.key])

        return self, dict()
