from typing import List, Optional, Tuple

from src.Command import Command
from src.Controller import Controller


class EchoCommand(Command):
    """Class representing the echo command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__('echo', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of echo command."""
        try:
            result = ' '.join(self.args)
        except Exception as exc:
            return '', str(exc), -1
        return result, '', 0
