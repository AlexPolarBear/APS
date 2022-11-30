from src.Model.Map import Direction, Map, Status
from src.Model.Backpack import Backpack
from src.Model.UserHero import UserHero


START_HERO_HEALTH = 10
MAP_HEIGHT = 10
MAP_WIDTH = 30


class Model(object):
    def __init__(self):
        self._map = Map(MAP_WIDTH, MAP_HEIGHT)
        self._user_hero = UserHero(START_HERO_HEALTH)

    # @classmethod
    # def from_save(cls, save_path: str) -> 'Model':
    #     model = cls()
    #     # TODO: Load the save file
    #     return model

    def move(self, direction: Direction):
        self._map.move(direction, self._user_hero)
        if self._map.get_status() == Status.FINISH:
            self._map = Map(MAP_WIDTH, MAP_HEIGHT)
            self._user_hero = UserHero(START_HERO_HEALTH)

    def get_map(self) -> Map:
        return self._map

    def get_backpack(self) -> Backpack:
        return self._user_hero.get_backpack()

    def activate_item(self, index: int) -> None:
        self._user_hero.activate_item(index)

    def deactivate_item(self, index: int) -> None:
        self._user_hero.deactivate_item(index)
    
    # def save_to_file(self, save_path: str):
    #     pass
