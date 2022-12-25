from src.Model.Map.MapBuilder import MapBuilder
from src.Model.Item import Item
from src.Model.Enemy.ConfusedEnemy import ConfusedEnemy
import random

class FileMapBuilder(MapBuilder):
    """Class for building the world map from file."""

    def __init__(self, world_map, height, width, max_item_health_point, enemy_factory, file_path):
        self._map = world_map
        self._height = height
        self._width = width
        self._max_item_health_point = max_item_health_point
        self._enemy_factory = enemy_factory
        self._file_path = file_path

        self._start_position = (0, 0)
        self._finish_position = (height - 1, width - 1)

    def generate_walls(self):
        from src.Model.Map.Map import GridCell

        with open(self._file_path, 'r') as file:
            lines = file.readlines()
            for i in range(self._height):
                for j in range(self._width):
                    if lines[i][j] == '.':
                        self._map[i][j] = GridCell.EMPTY
                    else:
                        self._map[i][j] = GridCell.WALL


    def generate_items(self):
        from src.Model.Map.Map import GridCell

        ITEMS_NUMBER = 10
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        self._coordinates_to_items = dict()
        cells_with_items = random.sample(empty_cells, min(len(empty_cells), ITEMS_NUMBER))
        for cell in cells_with_items:
            health_point = random.randint(1, self._max_item_health_point)
            self._coordinates_to_items[cell] = Item(health_point)
        return self._coordinates_to_items

    def generate_enemies(self):
        from src.Model.Map.Map import GridCell

        ENEMIES_NUMBER = 15
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY and (i, j) not in self._coordinates_to_items:
                    empty_cells.append((i, j))

        self._coordinates_to_enemies = dict()
        cells_with_enemies = random.sample(empty_cells, min(len(empty_cells), ENEMIES_NUMBER))

        for (cell_x, cell_y) in cells_with_enemies:
            enemy = self._enemy_factory.create_random_enemy()

            self._coordinates_to_enemies[(cell_x, cell_y)] = ConfusedEnemy(enemy)
            self._map[cell_x][cell_y] = GridCell.ENEMY
        return self._coordinates_to_enemies

    def generate_mold_prototype(self):
        self._mold_prototype = self._enemy_factory.create_mold()
        return self._mold_prototype
