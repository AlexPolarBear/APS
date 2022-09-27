from src.Controller import Controller


class UI(object):
    """Class for interaction with user."""

    def __init__(self, controller: Controller):
        self.controller = controller

    def read_input(self):
        """Read user's command."""
        
        return input('>>> ')

    def print_result(self, result: str):
        """Print the result of processing user's command."""

        print(result, end='')
