from src.Controller import Controller
from src.Command import AssignCommand


def test_assign_command_run_1():
    controller = Controller()
    command = AssignCommand(args=['a', '1'])

    command.run('', controller)

    assert controller.env_vars == {'a': '1'}
