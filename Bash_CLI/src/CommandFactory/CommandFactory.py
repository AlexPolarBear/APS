from typing import List

from src.Command.AssignCommand import AssignCommand
from src.Command.CatCommand import CatCommand
from src.Command.Command import Command
from src.Command.EchoCommand import EchoCommand
from src.Command.ExitCommand import ExitCommand
from src.Command.PwdCommand import PwdCommand
from src.Command.UnknownCommand import UnknownCommand
from src.Command.WcCommand import WcCommand
import src.Controller.Controller as Controller


class CommandFactory(object):
    def __init__(self, controller: Controller):
        self.controller = controller

    def generate_commands(self, str_commands: List[List[str]]) -> List[Command]:
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
            elif command[1] == '=':
                commands.append(AssignCommand(args=[command[0], command[2]]))
            else:
                commands.append(UnknownCommand(name=command[0], args=command[1:]))

        return commands
