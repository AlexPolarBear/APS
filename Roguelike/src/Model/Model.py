from src.Model.Map import Direction, Map, Status
from src.Model.Backpack import Backpack
from src.Model.UserHero import UserHero


START_HERO_HEALTH = 10
START_HERO_ATTACK = 1
MAX_ENEMY_HEALTH = 10
MAX_ENEMY_ATTACK = 2
MAX_ITEM_HEALTH_POINT = 10
MAP_HEIGHT = 10
MAP_WIDTH = 30


class Model(object):
    """
    Class representing the game world. It contains information about user's hero, map, enemies, items and so on. 
    """

##########public##########

    def __init__(self):
        """Create new level."""
        self._map = Map(MAP_WIDTH, MAP_HEIGHT, MAX_ITEM_HEALTH_POINT, MAX_ENEMY_HEALTH, MAX_ENEMY_ATTACK)
        self._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)

    # @classmethod
    # def from_save(cls, save_path: str) -> 'Model':
    #     model = cls()
    #     # TODO: Load the save file
    #     return model

    def move(self, direction: Direction):
        """Move the user's hero to the appropriate direction. If the user finishes the current level, then generate new level."""
        self._map.move(direction, self._user_hero)
        if self._map.status == Status.FINISH or self._map.status == Status.DEATH:
            self._map = Map(MAP_WIDTH, MAP_HEIGHT, MAX_ITEM_HEALTH_POINT, MAX_ENEMY_HEALTH, MAX_ENEMY_ATTACK)
            self._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)

    @property
    def world_map(self) -> Map:
        """Return the game map."""
        return self._map

    @property
    def backpack(self) -> Backpack:
        """Return the user's backpack."""
        return self._user_hero.backpack
    
    @property
    def user_hero(self) -> UserHero:
        """Return the user's hero."""
        return self._user_hero

    def activate_item(self, index: int) -> None:
        """Activate item with appropriate index."""
        self._user_hero.activate_item(index)

    def deactivate_item(self, index: int) -> None:
        """Deactivate item with appropriate index."""
        self._user_hero.deactivate_item(index)
    
    # def save_to_file(self, save_path: str):
    #     pass
