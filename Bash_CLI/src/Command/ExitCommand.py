from typing import Tuple, Optional, List

from src.Command import Command
from src.Controller import Controller


class ExitCommand(Command):
    """Class representing the exit command.
    After running this command, the program will exit.
    """
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__('exit', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        raise SystemExit
