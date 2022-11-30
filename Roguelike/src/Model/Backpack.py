from typing import List
from src.Model.Item import Item


class Backpack(object):
    def __init__(self):
        self._backpack = []

    def __len__(self):
        return len(self._backpack)

    def add_item(self, item: Item) -> None:
        self._backpack.append(item)
    
    def get_item(self, index: int) -> Item:
        return self._backpack[index]

    def get_all_items(self) -> List[Item]:
        return self._backpack
