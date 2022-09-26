from typing import List, Optional

from src.Command import Command


class CatCommand(Command):
    """Class representing the cat command.
    The execution of this command is completely delegated to the subshell.
    """
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__('cat', args)
