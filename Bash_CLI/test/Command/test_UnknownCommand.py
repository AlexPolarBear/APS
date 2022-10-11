from src.Controller import Controller
from src.Command import UnknownCommand
from src.Token import Token

def test_unknown_command_run_1():
    controller = Controller()
    command = UnknownCommand(name='echo', args=[Token('hello', ' ', ''), Token('world', '\n', '')])

    stdout, _, _ = command.run('', controller)

    assert stdout == 'hello world\n'
