from typing import List, Optional, Tuple
import os

from src.Command import Command
from src.Controller import Controller
from src.Token import Token


class PwdCommand(Command):
    """Class representing the pwd command."""
    def __init__(self, name: Optional[str] = None, args: Optional[List[Token]] = None):
        super().__init__('pwd', args)

    def run(self, stdin: str, controller: Controller) -> Tuple[str, str, int]:
        """Custom realization of pwd command."""
        try:
            cur_dir = os.getcwd()
        except Exception as exc:
            return '', str(exc), -1
        return cur_dir, '', 0
