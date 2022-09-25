from typing import Tuple

import src.Command.Command as Command
import src.Controller.Controller as Controller


class ExitCommand(Command):
    """Class representing the exit command.
    After running this command, the program will exit.
    """
    def run(self, stdin: str, controller: Controller.Controller) -> Tuple[str, str, int]:
        raise SystemExit
