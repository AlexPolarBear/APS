from typing import Optional

from src import Model
from src.GameClient.UI import UI


class BackpackUI(UI):
    def __init__(self, width: int, height: int):
        super(BackpackUI, self).__init__(width, height)

    def print(
            self, model: Model, erase_before: bool = True, selected_item_index: Optional[int] = None, **kwargs,
    ) -> None:
        if selected_item_index is None:
            selected_item_index = 0

        backpack = model.get_backpack()
        if erase_before:
            self.erase()

        print('#' * self.width * 2)

        title_left_offset = (self.width * 2 - 8) // 2
        print(title_left_offset * ' ' + 'Backpack\n')
        for index, item in enumerate(backpack.get_all_items()):
            if index == selected_item_index:
                print(f'-> {index + 1} ', end='')
            else:
                print(f'   {index + 1} ', end='')
            print(item.get_item_name(), end='')
            if item.get_activated():
                print(' ■')
            else:
                print(' □')
        print('\n' * (self.height - len(backpack) - 4))
        print('Press space to activate/deactivate item')
        print('#' * self.width * 2)
