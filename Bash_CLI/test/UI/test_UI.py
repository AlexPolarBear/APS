from io import StringIO

from src.Controller import Controller
from src.UI import UI


def test_read_input_1(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda msg: print(msg) or 'aboba')
    stdout = StringIO()
    monkeypatch.setattr('sys.stdout', stdout)

    controller = Controller()
    ui = UI(controller)

    assert ui.read_input() == 'aboba'
    assert stdout.getvalue() == '>>> \n'


def test_print_result_1(monkeypatch):
    stdout = StringIO()
    monkeypatch.setattr('sys.stdout', stdout)

    controller = Controller()
    ui = UI(controller)

    ui.print_result('aboba')

    assert stdout.getvalue() == 'aboba\n'
