from typing import Tuple, Optional, List

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class AssignCommand(Command):
    """Class representing the variable assignment command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('assign', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Assigns a value to an environment variable in the `controller`."""
        controller.env_vars[self.args[0].data] = self.args[1].data
        return '', '', 0
