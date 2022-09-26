from typing import List, Optional

from src.Command import Command


class WcCommand(Command):
    """Class representing the wc command.
    The execution of this command is completely delegated to the subshell.
    """
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__('wc', args)
