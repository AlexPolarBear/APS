from src.Controller import Controller
from src.Substitutor import Substitutor


def test_resolve_env_vars_1():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['echo', 'aboba']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'echo aboba'


def test_resolve_env_vars_2():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['echo', "'$HOME'"]

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == "echo '$HOME'"
