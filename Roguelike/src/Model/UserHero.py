from src.Model.Backpack import Backpack
from src.Model.Item import Item


class UserHero(object):
    def __init__(self, health_point: int):
        self._health_point = health_point
        self._backpack = Backpack()
    
    def get_backpack(self) -> Backpack:
        return self._backpack
    
    def activate_item(self, index: int) -> None:
        item: Item = self._backpack.get_item(index)
        if item.activate():
            self._health_point += item.get_health_point()
    
    def deactivate_item(self, index: int) -> None:
        item: Item = self._backpack.get_item(index)
        if item.deactivate():
            self._health_point -= item.get_health_point()
