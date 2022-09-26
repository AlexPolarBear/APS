from src.Command import CatCommand, EchoCommand, ExitCommand, PwdCommand, WcCommand, AssignCommand, UnknownCommand
from src.CommandFactory import CommandFactory
from src.Controller import Controller


def test_generate_commands_1():
    controller = Controller()
    command_factory = CommandFactory(controller)

    str_commands = [
        ['cat', 'file1.txt', 'file2.txt'],
        ['echo', 'Hello', 'World!'],
        ['pwd'],
        ['wc'],
        ['a', '=', 'b'],
        ['aboba', 'a1'],
        ['exit'],
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

    assert commands[0].args == ['file1.txt', 'file2.txt']

    assert commands[1].args == ['Hello', 'World!']

    assert commands[2].args == []

    assert commands[3].args == []

    assert commands[4].args == ['a', 'b']

    assert commands[5].name == 'aboba'
    assert commands[5].args == ['a1']
