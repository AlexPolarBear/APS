class Item(object):
    """
    A class representing an item in the game world. Each item has health points that change the user's 
    character health. When the user comes to a cell with the item, the item is added to the user's backpack.
    The user can activate or deactivate each item from the backpack. If the item is activated, 
    it increases health points of the user's character.
    """

##########public##########

    def __init__(self, health_point: int):
        """Create item with appropriate health points."""
        self._health_point = health_point
        self._activated = False
    
    def activate(self) -> bool:
        """Activate item."""
        if self._activated:
            return False
        self._activated = True
        return True
    
    def deactivate(self) -> bool:
        """Deactivate item."""
        if not self._activated:
            return False
        self._activated = False
        return True
    
    @property
    def health_point(self) -> int:
        """Return health points."""
        return self._health_point
    
    @property
    def activated(self) -> bool:
        """Return if the item is activated."""
        return self._activated

    def get_map_symbol(self) -> str:
        """Return symbol of the item for printing map."""
        return '0'

    def get_item_name(self) -> str:
        """Return item name."""
        return 'Item placeholder'
