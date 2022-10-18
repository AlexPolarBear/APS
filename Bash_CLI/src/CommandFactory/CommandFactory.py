from typing import List

from src.Command import Command, AssignCommand, CatCommand, EchoCommand, ExitCommand, PwdCommand, UnknownCommand, \
    WcCommand, GrepCommand
from src.Controller import Controller
from src.Token import Token


class CommandFactory(object):
    """Class for generating commands from their tokenized representations.

    Attributes
    ----------
    controller : Controller
        The controller object which contains current execution context.
    """
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_commands(self, str_commands: List[List[Token]]) -> List[Command]:
        """Generate a list of commands from a list of tokenized commands.

        Parameters
        ----------
        str_commands : List[List[Token]]
            A list of tokenized commands. Each tokenized command is a list of strings where one string (usually first)
            is the name of the command and the rest are the arguments.

        Returns
        -------
        List[Command]
            A list of commands.
        """
        commands = []

        for command in str_commands:
            if command[0].data == 'cat':
                commands.append(CatCommand(args=command[1:]))
            elif command[0].data == 'echo':
                commands.append(EchoCommand(args=command[1:]))
            elif command[0].data == 'exit':
                commands.append(ExitCommand())
            elif command[0].data == 'pwd':
                commands.append(PwdCommand(args=command[1:]))
            elif command[0].data == 'wc':
                commands.append(WcCommand(args=command[1:]))
            elif command[0].data == 'grep':
                commands.append(GrepCommand(args=command[1:]))
            elif len(command) > 1 and command[1].data == '=':
                commands.append(AssignCommand(args=[command[0], command[2]]))
            else:
                commands.append(UnknownCommand(name=command[0].data, args=command[1:]))

        return commands
