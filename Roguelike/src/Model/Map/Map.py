from collections import deque
from typing import Dict, List, Deque

from src.Model import Item
from src.Model.Enemy import EnemyContext

ONE_STEP = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Map(object):
    """Class for storing map data."""

    def __init__(self, height: int, width: int):
        from src.Model.Map.MapController import GridCell
        self.map: List[List[GridCell]] = [[GridCell.EMPTY for _ in range(width)] for _ in range(height)]
        self.coordinates_to_items: Dict[(int, int), Item] = dict()
        self.coordinates_to_enemies: Dict[(int, int), EnemyContext] = dict()
        self._height = height
        self._width = width

    def calculate_distance(self, start_position: (int, int)) -> List[List[int]]:
        from src.Model.Map.MapController import GridCell
        distance_from_user = [[-1 for _ in range(self._width)] for _ in range(self._height)]

        if self.map[start_position[0]][start_position[1]] == GridCell.WALL:
            return distance_from_user

        queue: Deque[(int, int)] = deque()
        queue.append(start_position)
        distance_from_user[start_position[0]][start_position[1]] = 0

        while len(queue) > 0:
            position = queue.popleft()

            for (dx, dy) in ONE_STEP:
                (new_row, new_col) = (position[0] + dx, position[1] + dy)
                if self.check_in_bounds(new_row, new_col) and self.map[new_row][new_col] != GridCell.WALL \
                        and distance_from_user[new_row][new_col] == -1:
                    distance_from_user[new_row][new_col] = distance_from_user[position[0]][position[1]] + 1
                    queue.append((new_row, new_col))

        return distance_from_user

    def check_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self._height) and (0 <= col < self._width)

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    @property
    def user_position(self) -> (int, int):
        from src.Model.Map.MapController import GridCell
        for i in range(self._height):
            for j in range(self._width):
                if self.map[i][j] == GridCell.USER_POSITION:
                    return i, j
        return None
