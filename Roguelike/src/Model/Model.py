from src.Model.Map import RandomMapBuilder, FileMapBuilder
from src.Model.Map.MapController import Direction, MapController, Status
from src.Model.Backpack import Backpack
from src.Model.UserHero import UserHero


START_HERO_HEALTH = 10
START_HERO_ATTACK = 1
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
        self._map = RandomMapBuilder(world_map, MAP_HEIGHT, MAP_WIDTH, MAX_ITEM_HEALTH_POINT, EnemyFactory()).generate_map()  # TODO
        self._map_controller = MapController(MAP_WIDTH, MAP_HEIGHT, MAX_ITEM_HEALTH_POINT, '')
        self._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)

    @classmethod
    def from_save(cls, save_path: str) -> 'Model':
        model = cls()
        self._map = FileMapBuilder(world_map, MAP_HEIGHT, MAP_WIDTH, MAX_ITEM_HEALTH_POINT, EnemyFactory(), save_path).generate_map()  # TODO
        model._map_controller = MapController(MAP_WIDTH, MAP_HEIGHT, MAX_ITEM_HEALTH_POINT, save_path)
        model._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)
        return model

    def move(self, direction: Direction):
        """Move the user's hero to the appropriate direction. If the user finishes the current level, then generate new level."""
        self._map_controller.move(direction, self._user_hero)
        if self._map_controller.status == Status.FINISH or self._map_controller.status == Status.DEATH:
            self._map_controller = MapController(MAP_WIDTH, MAP_HEIGHT, MAX_ITEM_HEALTH_POINT, '')
            self._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)

    @property
    def world_map(self) -> MapController:
        """Return the game map."""
        return self._map_controller

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
