from typing import Tuple

from src.Command.Command import Command
from src.Controller.Controller import Controller


class AssignCommand(Command):
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        controller.env_vars[self.args[0]] = self.args[1]
        return '', '', 0
