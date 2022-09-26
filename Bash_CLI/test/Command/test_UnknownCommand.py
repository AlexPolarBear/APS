from src.Controller import Controller
from src.Command import UnknownCommand


def test_unknown_command_run_1():
    controller = Controller()
    command = UnknownCommand(name='echo', args=['hello', 'world'])

    stdout, _, _ = command.run('', controller)

    assert stdout == 'hello world\n'
