from src.Controller.CommandFactory import CommandFactory
from src import Model, UI
from src.Controller.KeyboardHandler import KeyboardHandler


class Controller(object):
    def __init__(self, model: Model):
        self.ui = UI()
        self.model = model
        self.keyboard_handler = KeyboardHandler(keys_to_track={'w', 'a', 's', 'd', 'up', 'left', 'down', 'right'})
        self.command_factory = CommandFactory()

    def run(self) -> None:
        while True:
            user_button = self.keyboard_handler.get_user_button()
            command = self.command_factory.generate_command(user_button)

            game_map = self.model.process_command(command)

            self.ui.print_map(game_map)
