from typing import List, Optional

import src.Command.Command as Command


class EchoCommand(Command):
    """Class representing the echo command.
    The execution of this command is completely delegated to the subshell.
    """
    def __init__(self, name: Optional[str] = None, args: Optional[List[str]] = None):
        super().__init__(name, args)
        self.name = 'echo'
