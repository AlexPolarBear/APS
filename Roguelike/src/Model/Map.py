from collections import deque
from enum import Enum
import random
from typing import Deque, List

from src.Model import UserHero
from src.Model.Item import MAX_HEALTH_POINT, Item


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Status(Enum):
    IN_PROGRESS = 0
    FINISH = 1


class GridCell(Enum):
    EMPTY = 0
    WALL = 1
    USER_POSITION = 2
    ITEM = 3


ONE_STEP = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Map(object):
    def _check_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self._height) and (0 <= col < self._width)

    def _find_path(self) -> bool:
        if self._map[self._start_position[0]][self._start_position[1]] == GridCell.WALL:
            return False

        visited = []
        for _ in range(self._height):
            visited.append([False] * self._width)

        queue: Deque[(int, int)] = deque()
        queue.append(self._start_position)
        visited[self._start_position[0]][self._start_position[1]] = True

        while len(queue) > 0:
            position = queue.popleft()

            for (dx, dy) in ONE_STEP:
                (new_row, new_col) = (position[0] + dx, position[1] + dy)
                if self._check_in_bounds(new_row, new_col) and self._map[new_row][new_col] == GridCell.EMPTY \
                        and not visited[new_row][new_col]:
                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

        return visited[self._finish_position[0]][self._finish_position[1]]

    def _generate_walls(self):
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

    def _generate_items(self):
        ITEMS_NUMBER = 10
        empty_cells = []
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY:
                    empty_cells.append((i, j))

        self._coordinates_to_item = dict()
        for _ in range(ITEMS_NUMBER):
            if len(empty_cells) == 0:
                break

            rnd = random.choice(empty_cells)
            empty_cells.remove(rnd)
            self._map[rnd[0]][rnd[1]] = GridCell.ITEM

            health_point = random.randrange(MAX_HEALTH_POINT)
            self._coordinates_to_item[rnd] = Item(health_point)

    def _generate_map(self) -> None:
        self._map: List[List[GridCell]] = []
        for i in range(self._height):
            self._map.append([GridCell.EMPTY] * self._width)

        self._generate_walls()
        self._map[self._start_position[0]][self._start_position[1]] = GridCell.USER_POSITION
        self._generate_items()

    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._user_position = (0, 0)
        self._start_position = (0, 0)
        self._finish_position = (height - 1, width - 1)
        self._game_status = Status.IN_PROGRESS

        self._generate_map()

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def print_map(self) -> None:
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY:
                    print('.', end=' ')
                elif self._map[i][j] == GridCell.WALL:
                    print('█', end=' ')
                elif self._map[i][j] == GridCell.USER_POSITION:
                    print('@', end=' ')
                elif self._map[i][j] == GridCell.ITEM:
                    item = self._coordinates_to_item[(i, j)]
                    print(item.get_map_symbol(), end=' ')
            print()

    def get_status(self) -> Status:
        return self._game_status

    def move(self, direction: Direction, user_hero: UserHero) -> None:
        new_row, new_col = self._user_position[0] + ONE_STEP[direction.value][0], \
                           self._user_position[1] + ONE_STEP[direction.value][1]
        if not self._check_in_bounds(new_row, new_col):
            return
        if self._map[new_row][new_col] == GridCell.WALL:
            return
        if self._map[new_row][new_col] == GridCell.ITEM:
            item = self._coordinates_to_item[(new_row, new_col)]
            user_hero.get_backpack().add_item(item)
            self._coordinates_to_item.pop((new_row, new_col))

        self._map[new_row][new_col] = GridCell.USER_POSITION
        self._map[self._user_position[0]][self._user_position[1]] = GridCell.EMPTY
        self._user_position = (new_row, new_col)
        if self._user_position == self._finish_position:
            self._game_status = Status.FINISH
