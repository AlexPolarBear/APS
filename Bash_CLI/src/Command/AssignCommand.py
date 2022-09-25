from typing import Tuple

import src.Command.Command as Command
import src.Controller.Controller as Controller


class AssignCommand(Command.Command):
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        controller.env_vars[self.args[0]] = self.args[1]
        return '', '', 0
