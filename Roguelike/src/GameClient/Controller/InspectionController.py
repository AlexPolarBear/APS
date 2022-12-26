from typing import Tuple, Dict, Any, List

from src.Model import Model, Backpack
from src.GameClient.Controller import Controller
from src.GameClient.UI import BackpackUI, InspectionUI
from src.Model.Map.Map import GridCell
from src.dataclasses import Button


def _get_enemies_number(world_map: List[List[GridCell]]) -> int:
    enemies_n = 0
    for row in world_map:
        for cell in row:
            if cell in {
                GridCell.AGGRESSIVE_ENEMY, GridCell.NEUTRAL_ENEMY, GridCell.COWARD_ENEMY,
                GridCell.CONFUSED_ENEMY, GridCell.ENEMY, GridCell.MOLD
            }:
                enemies_n += 1
    return enemies_n


class InspectionController(Controller):
    """
    Controller specialization for the enemy inspection view.
    Responsible for processing user input and updating model when player is in the enemy inspection view.

    Parameters
    ----------
    model : Model
        Model instance which is controlled by this controller.

    Attributes
    ----------
    model : Model
        Model instance which is controlled by this controller.
    ui : MapUI
        UI instance responsible for rendering backpack view.
    selected_enemy_index : int
        Index of currently selected enemy for the inspection.
    """
    def __init__(self, model: Model):
        super(InspectionController, self).__init__(model)
        self._enemy_n = _get_enemies_number(model.world_map.get_map())
        self.ui = InspectionUI(model.world_map.width, model.world_map.height)
        self.selected_enemy_index = 0

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
        if button.key == 'shift':
            from src.GameClient.Controller import MapController
            return MapController(self.model), dict()

        elif button.key in {'up', 'down'} and self._enemy_n:
            if button.key == 'up':
                self.selected_enemy_index -= 1
            else:
                self.selected_enemy_index += 1
            self.selected_enemy_index %= self._enemy_n

        elif button.key == 'esc':
            raise SystemExit

        return self, dict(selected_enemy_index=self.selected_enemy_index)
