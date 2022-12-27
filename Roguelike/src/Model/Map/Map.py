from typing import Dict

from src.Model import Item
from src.Model.Enemy import Mold, Enemy


class MapData(object):
    """Class for storing map data."""
    def __init__(self, coordinates_to_items: Dict[(int, int), Item], mold_prototype: Mold, coordinates_to_enemies: Dict[(int, int), Enemy]):
        self._coordinates_to_items = coordinates_to_items
        self._mold_prototype = mold_prototype
        self._coordinates_to_enemies = coordinates_to_enemies
