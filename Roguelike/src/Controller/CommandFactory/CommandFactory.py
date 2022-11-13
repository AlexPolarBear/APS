from src.dataclasses import Button, Command


class CommandFactory(object):
    def __init__(self):
        pass

    def generate_command(self, button: Button) -> Command:
        return Command(button)
