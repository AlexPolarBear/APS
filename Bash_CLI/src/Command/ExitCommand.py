from typing import List, Optional, Tuple

from src.Command.Command import Command


class ExitCommand(Command):
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__(name, args)
        self.name = 'exit'

    def run(self, stdin: str) -> Tuple[str, str, int]:
        raise SystemExit
