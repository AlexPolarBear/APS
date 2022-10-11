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
        EchoCommand(args=['one two three']),
    ]
    output = interpreter.run_commands(commands)

    assert output == 'one two three'


def test_run_commands_3():
    controller = Controller()
    interpreter = Interpreter(controller)

    commands = [
        EchoCommand(args=['one two three\n']),
        WcCommand(),
    ]
    output = interpreter.run_commands(commands)

    assert output == '2  3  14'
