from src.dataclasses import Button, Command


class CommandFactory(object):
    def generate_command(self, button: Button) -> Command:
        raise NotImplementedError
