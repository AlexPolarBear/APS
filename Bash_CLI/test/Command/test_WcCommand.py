from src.Controller import Controller
from src.Command import WcCommand


def test_wc_command_run_1():
    controller = Controller()
    input_text = 'one two three\nfour five six\n'

    command = WcCommand()

    stdout, _, _ = command.run(input_text, controller)
    
    assert stdout == '3  6  28'
