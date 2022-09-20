from typing import List

from src.Command.Command import Command
from src.Controller.Controller import Controller


class CommandFactory(object):
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_commands(self, list_commands: List[List[str]]) -> List[Command]:
        for command in list_commands:
            # TODO
            pass
        return []
