from src.Controller import Controller
from src.Command import ExitCommand


def test_exit_command_run_1():
    controller = Controller()
    command = ExitCommand()

    try:
        _, _, _ = command.run('', controller)
    except SystemExit:
        pass
    else:
        assert False, 'SystemExit not raised'
