from typing import List

import src.Command.AssignCommand as AssignCommand
import src.Command.CatCommand as CatCommand
import src.Command.Command as Command
import src.Command.EchoCommand as EchoCommand
import src.Command.ExitCommand as ExitCommand
import src.Command.PwdCommand as PwdCommand
import src.Command.UnknownCommand as UnknownCommand
import src.Command.WcCommand as WcCommand
import src.Controller.Controller as Controller


class CommandFactory(object):
    """Class for generating commands from their tokenized representations.

    Attributes
    ----------
    controller : Controller.Controller
        The controller object which contains current execution context.
    """
    def __init__(self, controller: Controller.Controller):
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
                commands.append(CatCommand.CatCommand(args=command[1:]))
            elif command[0] == 'echo':
                commands.append(EchoCommand.EchoCommand(args=command[1:]))
            elif command[0] == 'exit':
                commands.append(ExitCommand.ExitCommand())
            elif command[0] == 'pwd':
                commands.append(PwdCommand.PwdCommand(args=command[1:]))
            elif command[0] == 'wc':
                commands.append(WcCommand.WcCommand(args=command[1:]))
            elif command[1] == '=':
                commands.append(AssignCommand.AssignCommand(args=[command[0], command[2]]))
            else:
                commands.append(UnknownCommand.UnknownCommand(name=command[0], args=command[1:]))

        return commands
