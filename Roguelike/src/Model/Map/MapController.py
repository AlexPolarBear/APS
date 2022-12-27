import random
from enum import Enum
from typing import List, Optional, Dict

from src.Model.Enemy import EnemyContext
from src.Model.Map.Map import Map
from src.Model.UserHero import UserHero, CharacterStatus


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Status(Enum):
    IN_PROGRESS = 0
    FINISH = 1
    DEATH = 2


class GridCell(Enum):
    EMPTY = 0
    WALL = 1
    USER_POSITION = 2
    ITEM = 3  # only for printing, all items are saved in dict
    ENEMY = 4  # during the game all enemies are saved as ENEMY
    AGGRESSIVE_ENEMY = 5  # only for printing
    NEUTRAL_ENEMY = 6  # only for printing
    COWARD_ENEMY = 7  # only for printing
    CONFUSED_ENEMY = 8  # only for printing
    MOLD = 9  # only for printing


ONE_STEP = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class MapController(object):

    def __init__(self, map_: Map):
        self._map: Map = map_
        self._user_position: (int, int) = map_.user_position
        self._game_status: Status = Status.IN_PROGRESS
        self._finish_position: (int, int) = (self._map.height - 1, self._map.width - 1)
        self._distance_from_user: List[List[int]] = \
            [[-1 for _ in range(self._map.width)] for _ in range(self._map.height)]

    @property
    def width(self) -> int:
        return self._map.width

    @property
    def height(self) -> int:
        return self._map.height

    @property
    def status(self) -> Status:
        return self._game_status

    def get_map(self) -> List[List[GridCell]]:
        map_with_items: List[List[GridCell]] = []
        for i in range(self._map.height):
            map_with_items.append([GridCell.EMPTY] * self._map.width)

        for i in range(self._map.height):
            for j in range(self._map.width):
                map_with_items[i][j] = self._map.map[i][j]
                if map_with_items[i][j] == GridCell.EMPTY and (i, j) in self._map.coordinates_to_items:
                    map_with_items[i][j] = GridCell.ITEM
                if map_with_items[i][j] == GridCell.ENEMY:
                    map_with_items[i][j] = self._map.coordinates_to_enemies[(i, j)].get_type()
        return map_with_items

    def distance_from_user(self, x: int, y: int):
        if not self._map.check_in_bounds(x, y):
            return -1
        return self._distance_from_user[x][y]

    def get_enemy_info(self, xy: (int, int)) -> Optional[Dict[str, str]]:
        x, y = xy
        if not self._map.check_in_bounds(x, y) or self._map.map[x][y] != GridCell.ENEMY:
            return None
        enemy: EnemyContext = self._map.coordinates_to_enemies[(x, y)]
        return {
            'type': enemy.get_type().name,
            'name': enemy.name,
            'health': str(enemy.health),
            'attack': str(enemy.attack),
        }

    def move(self, direction: Direction, user_hero: UserHero) -> None:
        new_row, new_col = self._user_position[0] + ONE_STEP[direction.value][0], \
                           self._user_position[1] + ONE_STEP[direction.value][1]
        if not self._map.check_in_bounds(new_row, new_col):
            return
        if self._map.map[new_row][new_col] == GridCell.WALL:
            return

        if self._map.map[new_row][new_col] == GridCell.EMPTY:
            self._map.map[new_row][new_col] = GridCell.USER_POSITION
            self._map.map[self._user_position[0]][self._user_position[1]] = GridCell.EMPTY
            self._user_position = (new_row, new_col)
            if self._user_position == self._finish_position:
                self._game_status = Status.FINISH

            if (new_row, new_col) in self._map.coordinates_to_items:
                item = self._map.coordinates_to_items[(new_row, new_col)]
                user_hero.backpack.add_item(item)
                self._map.coordinates_to_items.pop((new_row, new_col))
        else:
            enemy = self._map.coordinates_to_enemies[(new_row, new_col)]
            user_hero.attack(enemy)
            if enemy.status == CharacterStatus.DEAD:
                self._map.coordinates_to_enemies.pop((new_row, new_col))
                self._map.map[new_row][new_col] = GridCell.EMPTY

        self._distance_from_user = self._map.calculate_distance(self._user_position)

        old_positions = list(self._map.coordinates_to_enemies.items())
        for (enemy_position, enemy) in old_positions:
            (enemy_move_x, enemy_move_y) = enemy.next_move(enemy_position, self)

            if (enemy_move_x, enemy_move_y) == enemy_position:
                if enemy.get_type() == GridCell.MOLD:
                    for (dx, dy) in ONE_STEP:
                        (new_enemy_x, new_enemy_y) = (dx + enemy_position[0], dy + enemy_position[1])
                        if not self._map.check_in_bounds(new_enemy_x, new_enemy_y):
                            continue
                        if (self._map.map[new_enemy_x][new_enemy_y] == GridCell.EMPTY
                                and random.random() < enemy.probability):
                            self._map.map[new_enemy_x][new_enemy_y] = GridCell.ENEMY
                            self._map.coordinates_to_enemies[(new_enemy_x, new_enemy_y)] = enemy.clone()
                continue

            if self._map.map[enemy_move_x][enemy_move_y] == GridCell.EMPTY:
                self._map.coordinates_to_enemies.pop(enemy_position)
                self._map.map[enemy_move_x][enemy_move_y] = GridCell.ENEMY
                self._map.map[enemy_position[0]][enemy_position[1]] = GridCell.EMPTY
                self._map.coordinates_to_enemies[(enemy_move_x, enemy_move_y)] = enemy
            elif self._map.map[enemy_move_x][enemy_move_y] == GridCell.USER_POSITION:
                user_hero.defence(enemy)

        if user_hero.status == CharacterStatus.DEAD:
            self._game_status = Status.DEATH
