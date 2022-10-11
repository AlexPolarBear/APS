from typing import List, Optional, Tuple

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class CatCommand(Command):
    """Class representing the cat command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('cat', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of cat command."""
        try:
            if len(self.args) > 0:
                with open(str(self.args[0]), 'r') as input_file:
                    result = input_file.read()
            else:
                result = stdin
        except Exception as exc:
            return '', str(exc), -1
        return result, '', 0
