from typing import Tuple

import src.Command.Command as Command
import src.Controller.Controller as Controller


class ExitCommand(Command.Command):
    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        raise SystemExit
