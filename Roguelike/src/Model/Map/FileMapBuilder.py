import random

from src.Model.Enemy.EnemyContext import EnemyContext
from src.Model.Item import Item
from src.Model.Map.Map import Map
from src.Model.Map.MapBuilder import MapBuilder


class FileMapBuilder(MapBuilder):
    """Class for building the world map from file."""

    def __init__(self):
        super().__init__()
        self._file_path = None

    def set_file_path(self, value: str) -> 'FileMapBuilder':
        self._file_path = value

        with open(self._file_path, 'r') as file:
            lines = file.readlines()
            self._height = len(lines)
            self._width = len(lines[0]) - 1
            self._finish_position = (self._height - 1, self._width - 1)

        return self

    def _generate_walls(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        with open(self._file_path, 'r') as file:
            lines = file.readlines()
            for i in range(self._height):
                for j in range(self._width):
                    if lines[i][j] == '.':
                        map_.map[i][j] = GridCell.EMPTY
                    else:
                        map_.map[i][j] = GridCell.WALL

    def _generate_items(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        ITEMS_NUMBER = 10
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if map_.map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        self._coordinates_to_items = dict()
        cells_with_items = random.sample(empty_cells, min(len(empty_cells), ITEMS_NUMBER))
        for cell in cells_with_items:
            health_point = random.randint(1, self._max_item_health_point)
            self._coordinates_to_items[cell] = Item(health_point)
        return self._coordinates_to_items

    def _generate_enemies(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        ENEMIES_NUMBER = 15
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if map_.map[i][j] == GridCell.EMPTY and (i, j) not in self._coordinates_to_items:
                    empty_cells.append((i, j))

        self._coordinates_to_enemies = dict()
        cells_with_enemies = random.sample(empty_cells, min(len(empty_cells), ENEMIES_NUMBER))

        for (cell_x, cell_y) in cells_with_enemies:
            enemy = self._enemy_factory.create_random_enemy()

            self._coordinates_to_enemies[(cell_x, cell_y)] = EnemyContext(enemy)
            map_.map[cell_x][cell_y] = GridCell.ENEMY
        return self._coordinates_to_enemies
