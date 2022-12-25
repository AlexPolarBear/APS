from src.Model.Map.MapBuilder import MapBuilder
import random
from src.Model.Item import Item
from src.Model.Enemy.EnemyFactory import EnemyFactory
from src.Model.Enemy.ConfusedEnemy import ConfusedEnemy

class RandomMapBuilder(MapBuilder):
    """Class for random building the world map."""

    def __init__(self, world_map, height, width, max_item_health_point, enemy_factory, initial_map):
        self._map = world_map
        self._height = height
        self._width = width
        self._max_item_health_point = max_item_health_point
        self._enemy_factory = enemy_factory
        self._initial_map = initial_map

        self._start_position = (0, 0)
        self._finish_position = (height - 1, width - 1)

    def _find_path(self) -> bool:
        from src.Model.Map.Map import GridCell

        if self._map[self._start_position[0]][self._start_position[1]] == GridCell.WALL:
            return False
        self._initial_map.calculate_distance(self._start_position)
        return self._initial_map._distance_from_user[self._finish_position[0]][self._finish_position[1]] != -1

    def generate_walls(self):
        from src.Model.Map.Map import GridCell

        WALLS_NUMBER = self._width * self._height // 2
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        for _ in range(WALLS_NUMBER):
            rnd = random.choice(empty_cells)
            self._map[rnd[0]][rnd[1]] = GridCell.WALL
            if self._find_path():
                empty_cells.remove(rnd)
            else:
                self._map[rnd[0]][rnd[1]] = GridCell.EMPTY

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