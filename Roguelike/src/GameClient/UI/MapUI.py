from src import Model
from src.GameClient.UI import UI


class MapUI(UI):
    def __init__(self, width: int, height: int):
        super(MapUI, self).__init__(width, height)

    def print(self, model: Model, erase_before: bool = True, **kwargs) -> None:
        if erase_before:
            self.erase()

        print('#' * self.width * 2)
        model.get_map().print_map()
        print('#' * self.width * 2)
