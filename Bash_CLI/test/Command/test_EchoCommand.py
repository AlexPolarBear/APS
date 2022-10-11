from src.Controller import Controller
from src.Command import EchoCommand
from src.Token import Token


def test_echo_command_run_1():
    controller = Controller()

    input_text = 'Aboba'

    command = EchoCommand(args=[Token(input_text, '', '')])

    stdout, _, _ = command.run('', controller)

    assert stdout == input_text


def test_echo_command_run_2():
    controller = Controller()

    text1, text2, text3 = 'Aboba', 'boba', 'abobo'

    command = EchoCommand(args=[Token(text1, ' ', ''), Token(text2, ' ', ''), Token(text3, '', '')])

    stdout, _, _ = command.run('', controller)

    assert stdout == f'{text1} {text2} {text3}'
