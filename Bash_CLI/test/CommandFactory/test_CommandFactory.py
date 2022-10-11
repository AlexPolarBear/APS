from typing import List

from src.Command import CatCommand, EchoCommand, ExitCommand, PwdCommand, WcCommand, AssignCommand, UnknownCommand
from src.CommandFactory import CommandFactory
from src.Controller import Controller
from src.Token import Token

def equals_token(list1: List[Token], list2: List[str]) -> bool:
    if len(list1) != len(list2):
        return False

    for index, token in enumerate(list1):
        if token.data != list2[index]:
            return False
    return True

def test_generate_commands_1():
    controller = Controller()
    command_factory = CommandFactory(controller)

    str_commands = [
        [Token('cat', '', ''), Token('file1.txt', '', ''), Token('file2.txt', '', '')],
        [Token('echo', '', ''), Token('Hello', '', ''), Token('World!', '', '')],
        [Token('pwd', '', '')],
        [Token('wc', '', '')],
        [Token('a', '', ''), Token('=', '', ''), Token('b', '', '')],
        [Token('aboba', '', ''), Token('a1', '', '')],
        [Token('exit', '', '')],
    ]
    commands = command_factory.generate_commands(str_commands)

    assert len(commands) == 7

    assert isinstance(commands[0], CatCommand)
    assert isinstance(commands[1], EchoCommand)
    assert isinstance(commands[2], PwdCommand)
    assert isinstance(commands[3], WcCommand)
    assert isinstance(commands[4], AssignCommand)
    assert isinstance(commands[5], UnknownCommand)
    assert isinstance(commands[6], ExitCommand)

    assert equals_token(commands[0].args, ['file1.txt', 'file2.txt'])

    assert equals_token(commands[1].args, ['Hello', 'World!'])

    assert commands[2].args == []

    assert commands[3].args == []

    assert equals_token(commands[4].args, ['a', 'b'])

    assert commands[5].name == 'aboba'
    assert equals_token(commands[5].args, ['a1'])


def test_generate_commands_2():
    controller = Controller()
    command_factory = CommandFactory(controller)

    str_commands = [
        [Token('aboba', '', '')],
    ]
    commands = command_factory.generate_commands(str_commands)

    assert len(commands) == 1
    assert isinstance(commands[0], UnknownCommand)
    assert commands[0].name == 'aboba'
    assert commands[0].args == []


def test_generate_commands_3():
    controller = Controller()
    command_factory = CommandFactory(controller)

    str_commands = []
    commands = command_factory.generate_commands(str_commands)

    assert commands == []
