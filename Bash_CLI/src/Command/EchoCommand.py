from typing import List, Optional, Tuple

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class EchoCommand(Command):
    """Class representing the echo command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('echo', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of echo command."""
        try:
            result = ''
            for token in self.args:
                result += token.data + token.separator
        except Exception as exc:
            return '', str(exc), -1
        return result, '', 0
