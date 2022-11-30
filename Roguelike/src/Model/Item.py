MAX_HEALTH_POINT = 10


class Item(object):
    """
    Class representing an item in game world. Each item has health points that change
    the user's character health. When user come to cell with the item, item is added to user's backpack.
    Each item user can activate or deactivate from the backpack.
    """
    def __init__(self, health_point: int):
        self._health_point = health_point
        self._activated = False
    
    def activate(self) -> bool:
        if self._activated:
            return False
        self._activated = True
        return True
    
    def deactivate(self) -> bool:
        if not self._activated:
            return False
        self._activated = False
        return True
    
    def get_health_point(self) -> int:
        return self._health_point
    
    def get_activated(self) -> bool:
        return self._activated

    def get_map_symbol(self) -> str:
        return '0'

    def get_item_name(self) -> str:
        return 'Item placeholder'
