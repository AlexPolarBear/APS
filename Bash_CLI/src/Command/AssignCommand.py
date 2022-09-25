from typing import Tuple

import src.Command.Command as Command
import src.Controller.Controller as Controller


class AssignCommand(Command):
    """Class representing the variable assignment command."""
    def run(self, stdin: str, controller: Controller.Controller) -> Tuple[str, str, int]:
        """Assigns a value to an environment variable in the `controller`."""
        controller.env_vars[self.args[0]] = self.args[1]
        return '', '', 0
