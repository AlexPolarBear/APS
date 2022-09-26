from typing import Tuple

from src.Command import Command
from src.Controller import Controller


class ExitCommand(Command):
    """Class representing the exit command.
    After running this command, the program will exit.
    """
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        raise SystemExit
