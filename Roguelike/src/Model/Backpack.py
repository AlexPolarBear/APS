from typing import List
from src.Model.Item import Item


class Backpack(object):
    """
    A class representing a backpack in the game world. An user has one backpack during the game
    and can add items to it.
    """

##########public##########

    def __init__(self):
        """Create empty backpack."""
        self._backpack = []

    def __len__(self):
        """Return number of items in the backpack."""
        return len(self._backpack)

    def add_item(self, item: Item) -> None:
        """Add item to the backpack."""
        self._backpack.append(item)
    
    def get_item(self, index: int) -> Item:
        """Get item with appropriate index."""
        return self._backpack[index]

    def get_all_items(self) -> List[Item]:
        """Get list of all items."""
        return self._backpack
