import pytest

from src import Model
from src.GameClient.Controller import MapController, BackpackController
from src.dataclasses import Button


def test_map_controller_exit():
    model = Model()
    backpack_controller = MapController(model)
    with pytest.raises(SystemExit):
        backpack_controller.process_button(Button('esc'))


def test_map_controller_tab():
    model = Model()
    map_controller = MapController(model)
    next_controller, next_controller_params = map_controller.process_button(Button('tab'))
    assert isinstance(next_controller, BackpackController)
    assert next_controller_params == dict(selected_item_index=0)
