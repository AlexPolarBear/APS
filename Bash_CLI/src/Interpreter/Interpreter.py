from typing import List

from src.Command.Command import Command

import src.Controller.Controller as Controller


class Interpreter(object):
    def __init__(self, controller: Controller.Controller):
        self.controller = controller

    def run_commands(self, list_commands: List[Command]) -> str:
        stdin = ''

        for command in list_commands:
            stdout = command.run(stdin, self.controller)
            stdin = stdout

        return stdin
