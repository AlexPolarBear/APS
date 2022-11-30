from src import Model
from src.GameClient.Controller.MapController import MapController
from src.GameClient.KeyboardHandler import KeyboardHandler


class GameClient(object):
    def __init__(self, model: Model):
        self.model = model
        self.controller = MapController(model)
        self.keyboard_handler = KeyboardHandler(
            keys_to_track={'w', 'a', 's', 'd', 'up', 'left', 'down', 'right', 'tab', 'space'},
            key_mapping={'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'},
        )

        self.controller.ui.print(self.model, erase_before=False)

    def play(self) -> None:
        while True:
            user_button = self.keyboard_handler.get_user_button()
            self.controller, print_kwargs = self.controller.process_button(user_button)
            self.controller.ui.print(self.model, erase_before=True, **print_kwargs)
