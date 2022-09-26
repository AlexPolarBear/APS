from typing import List

from src.Command import Command, AssignCommand, CatCommand, EchoCommand, ExitCommand, PwdCommand, UnknownCommand, \
    WcCommand
from src.Controller import Controller


class CommandFactory(object):
    """Class for generating commands from their tokenized representations.

    Attributes
    ----------
    controller : Controller
        The controller object which contains current execution context.
    """
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_commands(self, str_commands: List[List[str]]) -> List[Command]:
        """Generate a list of commands from a list of tokenized commands.

        Parameters
        ----------
        str_commands : List[List[str]]
            A list of tokenized commands. Each tokenized command is a list of strings where one string (usually first)
            is the name of the command and the rest are the arguments.

        Returns
        -------
        List[Command]
            A list of commands.
        """
        commands = []

        for command in str_commands:
            if command[0] == 'cat':
                commands.append(CatCommand(args=command[1:]))
            elif command[0] == 'echo':
                commands.append(EchoCommand(args=command[1:]))
            elif command[0] == 'exit':
                commands.append(ExitCommand())
            elif command[0] == 'pwd':
                commands.append(PwdCommand(args=command[1:]))
            elif command[0] == 'wc':
                commands.append(WcCommand(args=command[1:]))
            elif len(commands) > 1 and command[1] == '=':
                commands.append(AssignCommand(args=[command[0], command[2]]))
            else:
                commands.append(UnknownCommand(name=command[0], args=command[1:]))

        return commands
