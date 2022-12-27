from src.Model.Backpack import Backpack
from src.Model.Enemy.EnemyFactory import EnemyFactory
from src.Model.Map import RandomMapBuilder, FileMapBuilder
from src.Model.Map.MapController import Direction, MapController, Status
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
        self._map = RandomMapBuilder() \
            .set_width(MAP_WIDTH) \
            .set_height(MAP_HEIGHT) \
            .set_max_item_health_point(MAX_ITEM_HEALTH_POINT) \
            .set_enemy_factory(EnemyFactory()) \
            .generate_map()
        self._map_controller = MapController(self._map)
        self._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)

    @classmethod
    def from_save(cls, save_path: str) -> 'Model':
        model = cls()
        model._map = FileMapBuilder() \
            .set_file_path(save_path) \
            .set_max_item_health_point(MAX_ITEM_HEALTH_POINT) \
            .set_enemy_factory(EnemyFactory()) \
            .generate_map()
        model._map_controller = MapController(model._map)
        model._user_hero = UserHero(START_HERO_HEALTH, START_HERO_ATTACK)
        return model

    def move(self, direction: Direction):
        """
        Move the user's hero to the appropriate direction.
        If the user finishes the current level, then generate new level.
        """
        self._map_controller.move(direction, self._user_hero)
        if self._map_controller.status == Status.FINISH or self._map_controller.status == Status.DEATH:
            new_map = RandomMapBuilder() \
                .set_width(MAP_WIDTH) \
                .set_height(MAP_HEIGHT) \
                .set_max_item_health_point(MAX_ITEM_HEALTH_POINT) \
                .set_enemy_factory(EnemyFactory()) \
                .generate_map()
            self._map_controller = MapController(new_map)
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
