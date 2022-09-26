import platform

from src.Controller import Controller
from src.Command import WcCommand


def test_wc_command_run_1():
    controller = Controller()
    input_text = 'one two three\nfour five six\n'

    command = WcCommand()

    stdout, _, _ = command.run(input_text, controller)

    if platform.system() == 'Windows':
        assert stdout == '      2       6      30\n'
    else:
        assert stdout == '      2       6      28\n'
