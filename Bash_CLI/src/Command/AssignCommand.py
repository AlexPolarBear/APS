from typing import Tuple

from src.Command import Command
from src.Controller import Controller


class AssignCommand(Command):
    """Class representing the variable assignment command."""
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Assigns a value to an environment variable in the `controller`."""
        controller.env_vars[self.args[0]] = self.args[1]
        return '', '', 0
