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
    elif platform.system() == 'Linux':
        assert output == '      1       3      14\n'
    else:
        assert output == '       1       3      14\n'


def test_run_with_error_1():
    controller = Controller()
    interpreter = Interpreter(controller)

    commands = [
        CatCommand(args=['nonexistent_file.txt']),
    ]

    try:
        interpreter.run_commands(commands)
    except RuntimeError as e:
        assert e.args[0] == 'cat: nonexistent_file.txt: No such file or directory\n'
    else:
        raise AssertionError('RuntimeError was not raised')
