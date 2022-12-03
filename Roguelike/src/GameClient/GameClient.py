from src import Model
from src.GameClient.Controller.MapController import MapController
from src.GameClient.KeyboardHandler import KeyboardHandler


class GameClient(object):
    """
    Main class which is responsible for running the game.
    Starts a game loop and handles user input.

    Parameters
    ----------
    model : Model
        Model instance which contains all the game data and logic.

    Attributes
    ----------
    model : Model
        Model instance which contains all the game data and logic.
    controller : Controller
        Starting controller which takes control of the game. Initially it is MapController.
    keyboard_handler : KeyboardHandler
        Handler reads user input and converts it to Button instances.
    """
    def __init__(self, model: Model):
        self.model = model
        self.controller = MapController(model)
        self.keyboard_handler = KeyboardHandler(
            keys_to_track={'w', 'a', 's', 'd', 'up', 'left', 'down', 'right', 'tab', 'space'},
            key_mapping={'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'},
        )

        self.controller.ui.print(self.model, erase_before=False)

    def play(self) -> None:
        """Start a game loop and handle user input."""
        while True:
            user_button = self.keyboard_handler.get_user_button()
            self.controller, print_kwargs = self.controller.process_button(user_button)
            self.controller.ui.print(self.model, erase_before=True, **print_kwargs)
