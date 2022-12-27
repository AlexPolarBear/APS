import pytest

from src import Model
from src.GameClient.Controller import BackpackController, MapController
from src.dataclasses import Button


def test_backpack_controller_exit():
    model = Model()
    backpack_controller = BackpackController(model)
    with pytest.raises(SystemExit):
        backpack_controller.process_button(Button('esc'))


def test_backpack_controller_tab():
    model = Model()
    backpack_controller = BackpackController(model)
    next_controller, next_controller_params = backpack_controller.process_button(Button('tab'))
    assert isinstance(next_controller, MapController)
    assert next_controller_params == dict()
