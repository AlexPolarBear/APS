from src.GameClient.Command import Command
from src.Model import Model


class SwitchItemCommand(Command):
    def __init__(self, model: Model, item_index: int):
        super().__init__(model)
        self._item_index = item_index

    def execute(self):
        backpack = self._model.backpack
        selected_item = backpack.get_item(self._item_index)
        if selected_item.activated:
            self._model.deactivate_item(self._item_index)
        else:
            self._model.activate_item(self._item_index)
