import random

from src.Model.Enemy.EnemyContext import EnemyContext
from src.Model.Item import Item
from src.Model.Map.Map import Map
from src.Model.Map.MapBuilder import MapBuilder


class RandomMapBuilder(MapBuilder):
    """Class for random building the world map."""

    def _find_path(self, map_: Map) -> bool:
        from src.Model.Map.MapController import GridCell

        if map_.map[self._start_position[0]][self._start_position[1]] == GridCell.WALL:
            return False

        distance_from_user = map_.calculate_distance(self._start_position)
        return distance_from_user[self._finish_position[0]][self._finish_position[1]] != -1

    def _generate_walls(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        WALLS_NUMBER = self._width * self._height // 2
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if map_.map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        for _ in range(WALLS_NUMBER):
            rnd = random.choice(empty_cells)
            map_.map[rnd[0]][rnd[1]] = GridCell.WALL
            if self._find_path(map_):
                empty_cells.remove(rnd)
            else:
                map_.map[rnd[0]][rnd[1]] = GridCell.EMPTY

    def _generate_items(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        ITEMS_NUMBER = 10
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if map_.map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        cells_with_items = random.sample(empty_cells, min(len(empty_cells), ITEMS_NUMBER))
        for cell in cells_with_items:
            health_point = random.randint(1, self._max_item_health_point)
            map_.coordinates_to_items[cell] = Item(health_point)

    def _generate_enemies(self, map_: Map):
        from src.Model.Map.MapController import GridCell

        ENEMIES_NUMBER = 15
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if map_.map[i][j] == GridCell.EMPTY and (i, j) not in map_.coordinates_to_items:
                    empty_cells.append((i, j))

        cells_with_enemies = random.sample(empty_cells, min(len(empty_cells), ENEMIES_NUMBER))

        for (cell_x, cell_y) in cells_with_enemies:
            enemy = self._enemy_factory.create_random_enemy()

            map_.coordinates_to_enemies[(cell_x, cell_y)] = EnemyContext(enemy)
            map_.map[cell_x][cell_y] = GridCell.ENEMY
