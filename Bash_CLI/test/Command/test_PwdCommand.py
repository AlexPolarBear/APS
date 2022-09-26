import os

from src.Controller import Controller
from src.Command import PwdCommand


def test_pwd_command_run_1():
    controller = Controller()
    command = PwdCommand()

    stdout, _, _ = command.run('', controller)

    assert stdout.endswith(os.path.basename(os.getcwd()) + '\n')
