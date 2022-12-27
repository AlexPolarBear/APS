import pytest

from src import Model
from src.GameClient.Controller import InspectionController, MapController
from src.dataclasses import Button


def test_inspection_controller_exit():
    model = Model()
    backpack_controller = InspectionController(model)
    with pytest.raises(SystemExit):
        backpack_controller.process_button(Button('esc'))


def test_inspection_controller_shift():
    model = Model()
    inspection_controller = InspectionController(model)
    next_controller, next_controller_params = inspection_controller.process_button(Button('shift'))
    assert isinstance(next_controller, MapController)
    assert next_controller_params == dict()
