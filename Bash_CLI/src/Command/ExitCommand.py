from typing import Tuple

from src.Command.Command import Command
from src.Controller.Controller import Controller


class ExitCommand(Command):
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        raise SystemExit
