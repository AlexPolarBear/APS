from src.Controller import Controller


class Parser(object):
    """Class for splitting the list of tokens into separate commands."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def parse_commands(self, list_tokens):
        """Split list_tokens into separate commands."""

        return [list_tokens]
