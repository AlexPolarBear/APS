import platform

from src.Command import WcCommand, CatCommand, EchoCommand
from src.Interpreter import Interpreter
from src.Controller import Controller


def test_run_commands_1():
    controller = Controller()
    interpreter = Interpreter(controller)

    assert interpreter.run_commands([]) == ''


def test_run_commands_2():
    controller = Controller()
    interpreter = Interpreter(controller)

    commands = [
        EchoCommand(args=['one two three\n']),
    ]
    output = interpreter.run_commands(commands)

    assert output == 'one two three\n'


def test_run_commands_3():
    controller = Controller()
    interpreter = Interpreter(controller)

    commands = [
        EchoCommand(args=['one two three\n']),
        WcCommand(),
    ]
    output = interpreter.run_commands(commands)

    if platform.system() == 'Windows':
        assert output == '      1       3      15\n'
    else:
        assert output == '      1       3      14\n'
