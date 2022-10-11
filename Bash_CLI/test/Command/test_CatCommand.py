import os

from src.Controller import Controller
from src.Command import CatCommand
from src.Token import Token


def test_cat_command_run_1():
    controller = Controller()
    filename = os.path.join(os.getcwd(), 'test', 'Command', 'test_AssignCommand.py')

    assert os.path.isfile(filename)

    command = CatCommand(args=[Token(filename, '', '')])

    stdout, _, _ = command.run('', controller)

    assert isinstance(stdout, str)
    assert stdout == open(filename).read()


def test_cat_command_run_2():
    controller = Controller()
    command = CatCommand()

    input_text = 'Hello, World!'

    stdout, _, _ = command.run(input_text, controller)

    assert isinstance(stdout, str)
    assert stdout == input_text
