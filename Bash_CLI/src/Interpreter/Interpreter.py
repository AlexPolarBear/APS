from typing import List

from src.Command import Command

from src.Controller import Controller


class Interpreter(object):
    """Class for running commands and passing the output of the previous to the next command.

    Attributes
    ----------
    controller : Controller.Controller
        The controller object which contains current execution context.
    """
    def __init__(self, controller: Controller):
        self.controller = controller

    def run_commands(self, list_commands: List[Command]) -> str:
        """Run commands one-by-one passing output of the previous command to the next command
        and return the output of the last command.

        Parameters
        ----------
        list_commands : List[Command]
            A list of commands.

        Returns
        -------
        str
            The output of the last command.
        """
        stdin = ''

        for command in list_commands:
            stdout, stderr, return_code = command.run(stdin, self.controller)
            if return_code != 0:
                raise RuntimeError(stderr)
            stdin = stdout

        return stdin
