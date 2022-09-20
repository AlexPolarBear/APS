from typing import List, Optional

from src.Command.Command import Command


class EchoCommand(Command):
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__(name, args)
        self.name = 'echo'
