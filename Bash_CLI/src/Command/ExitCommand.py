from typing import Tuple

from src.Command.Command import Command
import src.Controller.Controller as Controller


class ExitCommand(Command):
    def run(self, stdin: str, controller: Controller.Controller) -> Tuple[str, str, int]:
        raise SystemExit
