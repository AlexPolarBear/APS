from typing import Tuple, Dict, Any

from src import Model
from src.GameClient.Controller import Controller
from src.GameClient.UI import BackpackUI
from src.dataclasses import Button


class BackpackController(Controller):
    def __init__(self, model: Model):
        super(BackpackController, self).__init__(model)
        self.backpack = model.get_backpack()
        self.ui = BackpackUI(model.get_map().width, model.get_map().height)
        self.selected_item_index = 0

    def process_button(self, button: Button) -> Tuple[Controller, Dict[str, Any]]:
        if button.key == 'tab':
            from src.GameClient.Controller import MapController
            return MapController(self.model), dict()

        elif button.key == 'space' and self.backpack:
            selected_item = self.backpack.get_item(self.selected_item_index)
            if selected_item.get_activated():
                selected_item.deactivate()
            else:
                selected_item.activate()

        elif button.key in {'up', 'down'} and self.backpack:
            if button.key == 'up':
                self.selected_item_index -= 1
            else:
                self.selected_item_index += 1
            self.selected_item_index %= len(self.backpack)

        return self, dict(selected_item_index=self.selected_item_index)
