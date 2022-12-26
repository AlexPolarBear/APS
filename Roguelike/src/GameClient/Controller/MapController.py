from typing import Tuple, Dict, Any

from src.GameClient.Command import Command, MoveUpCommand, MoveDownCommand, MoveRightCommand, MoveLeftCommand
from src.GameClient.Controller import Controller
from src.GameClient.UI import MapUI
from src.dataclasses import Button


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
        self.move_down_command = MoveDownCommand(model)
        self.move_up_command = MoveUpCommand(model)
        self.move_left_command = MoveLeftCommand(model)
        self.move_right_command = MoveRightCommand(model)

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
            command = self._choose_move_command(button)
            command.execute()

        elif button.key == 'esc':
            raise SystemExit

        return self, dict()

    def _choose_move_command(self, button: Button) -> Command:
        """
        Choose move command based on user input.

        Parameters
        ----------
        button : Button
            Button instance which represents user input.

        Returns
        -------
        Command
            Move command instance.
        """
        if button.key == 'up':
            return self.move_up_command
        elif button.key == 'down':
            return self.move_down_command
        elif button.key == 'left':
            return self.move_left_command
        elif button.key == 'right':
            return self.move_right_command
