from typing import Optional

from src.Model.Enemy.EnemyFactory import EnemyFactory
from src.Model.Map.Map import Map
from src.Model.Map.MapController import GridCell


class MapBuilder(object):
    """Class for building the world map."""

    def __init__(self):
        self._height = None
        self._width = None
        self._max_item_health_point = None
        self._enemy_factory = None

        self._start_position = (0, 0)
        self._finish_position = None

    def generate_map(self) -> Optional[Map]:
        """Generate the map data."""
        if (
                self._height is None
                or self._width is None
                or self._max_item_health_point is None
                or self._enemy_factory is None
        ):
            return None

        map_ = Map(self._height, self._width)

        self._generate_walls(map_)
        map_.map[self._start_position[0]][self._start_position[1]] = GridCell.USER_POSITION
        self._generate_items(map_)
        self._generate_enemies(map_)

        return map_

    def set_height(self, value: int) -> 'MapBuilder':
        self._height = value
        if self._width is not None:
            self._finish_position = (self._height - 1, self._width - 1)
        return self

    def set_width(self, value: int) -> 'MapBuilder':
        self._width = value
        if self._height is not None:
            self._finish_position = (self._height - 1, self._width - 1)
        return self

    def set_max_item_health_point(self, value: int) -> 'MapBuilder':
        self._max_item_health_point = value
        return self

    def set_enemy_factory(self, enemy_factory: EnemyFactory) -> 'MapBuilder':
        self._enemy_factory = enemy_factory
        return self

    def _generate_walls(self, map_: Map):
        """Generate walls on the world map."""
        raise NotImplementedError

    def _generate_items(self, map_: Map):
        """Arrange items on the map."""
        raise NotImplementedError

    def _generate_enemies(self, map_: Map):
        """Arrange enemies on the map."""
        raise NotImplementedError
