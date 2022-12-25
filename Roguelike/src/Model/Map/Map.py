from collections import deque
from enum import Enum
import random
from typing import Deque, List, Optional, Dict

from src.Model.Enemy.EnemyFactory import EnemyFactory
from src.Model.UserHero import UserHero, CharacterStatus
from src.Model.Item import Item
from src.Model.Enemy.Enemy import Enemy
from src.Model.Enemy.AggressiveEnemy import AggressiveEnemy
from src.Model.Enemy.NeutralEnemy import NeutralEnemy
from src.Model.Enemy.CowardEnemy import CowardEnemy
from src.Model.Enemy.ConfusedEnemy import ConfusedEnemy
from src.Model.Map.RandomMapBuilder import RandomMapBuilder
from src.Model.Map.FileMapBuilder import FileMapBuilder


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
    ITEM = 3              #only for printing, all items are saved in dict
    ENEMY = 4             #during the game all enemies are saved as ENEMY
    AGGRESSIVE_ENEMY = 5  #only for printing
    NEUTRAL_ENEMY = 6     #only for printing
    COWARD_ENEMY = 7      #only for printing
    CONFUSED_ENEMY = 8    #only for printing
    MOLD = 9              #only for printing


ONE_STEP = [(-1, 0), (0, 1), (1, 0), (0, -1)]


class Map(object):

##########public##########

    def __init__(self, width, height, max_item_health_point, file_path):
        self._width = width
        self._height = height
        self._user_position = (0, 0)
        self._start_position = (0, 0)
        self._finish_position = (height - 1, width - 1)
        self._game_status = Status.IN_PROGRESS

        self._max_item_health_point = max_item_health_point

        self._generate_map(file_path)

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height
    
    @property
    def status(self) -> Status:
        return self._game_status
    
    def get_map(self) -> List[List[GridCell]]:
        map_with_items: List[List[GridCell]] = []
        for i in range(self._height):
            map_with_items.append([GridCell.EMPTY] * self._width)
        
        for i in range(self._height):
            for j in range(self._width):
                map_with_items[i][j] = self._map[i][j]
                if map_with_items[i][j] == GridCell.EMPTY and (i, j) in self._coordinates_to_items:
                    map_with_items[i][j] = GridCell.ITEM
                if map_with_items[i][j] == GridCell.ENEMY:
                    map_with_items[i][j] = self._coordinates_to_enemies[(i, j)].get_type()
        return map_with_items
    
    def distance_from_user(self, x: int, y: int):
        if not self._check_in_bounds(x, y):
            return -1
        return self._distance_from_user[x][y]

    def get_enemy_info(self, xy: (int, int)) -> Optional[Dict[str, str]]:
        x, y = xy
        if not self._check_in_bounds(x, y) or self._map[x][y] != GridCell.ENEMY:
            return None
        enemy: Enemy = self._coordinates_to_enemies[(x, y)]
        return {
            'type': enemy.get_type().name,
            'name': enemy.name,
            'health': str(enemy.health),
            'attack': str(enemy.attack),
        }

    def calculate_distance(self, start_position):
        for i in range(self._height):
            for j in range(self._width):
                self._distance_from_user[i][j] = -1

        if self._map[start_position[0]][start_position[1]] == GridCell.WALL:
            return

        queue: Deque[(int, int)] = deque()
        queue.append(start_position)
        self._distance_from_user[start_position[0]][start_position[1]] = 0

        while len(queue) > 0:
            position = queue.popleft()

            for (dx, dy) in ONE_STEP:
                (new_row, new_col) = (position[0] + dx, position[1] + dy)
                if self._check_in_bounds(new_row, new_col) and self._map[new_row][new_col] != GridCell.WALL \
                        and self._distance_from_user[new_row][new_col] == -1:
                    self._distance_from_user[new_row][new_col] = self._distance_from_user[position[0]][position[1]] + 1
                    queue.append((new_row, new_col))

    def move(self, direction: Direction, user_hero: UserHero) -> None:
        new_row, new_col = self._user_position[0] + ONE_STEP[direction.value][0], \
                           self._user_position[1] + ONE_STEP[direction.value][1]
        if not self._check_in_bounds(new_row, new_col):
            return
        if self._map[new_row][new_col] == GridCell.WALL:
            return
        
        if self._map[new_row][new_col] == GridCell.EMPTY:
            self._map[new_row][new_col] = GridCell.USER_POSITION
            self._map[self._user_position[0]][self._user_position[1]] = GridCell.EMPTY
            self._user_position = (new_row, new_col)
            if self._user_position == self._finish_position:
                self._game_status = Status.FINISH
            
            if (new_row, new_col) in self._coordinates_to_items:
                item = self._coordinates_to_items[(new_row, new_col)]
                user_hero.backpack.add_item(item)
                self._coordinates_to_items.pop((new_row, new_col))
        else:
            enemy = self._coordinates_to_enemies[(new_row, new_col)]
            user_hero.attack(enemy)
            if enemy.status == CharacterStatus.DEAD:
                self._coordinates_to_enemies.pop((new_row, new_col))
                self._map[new_row][new_col] = GridCell.EMPTY
        
        self.calculate_distance(self._user_position)

        old_positions = list(self._coordinates_to_enemies.items())
        for (enemy_position, enemy) in old_positions:
            (enemy_move_x, enemy_move_y) = enemy.next_move(enemy_position, self)
            
            if (enemy_move_x, enemy_move_y) == enemy_position:
                if enemy.get_type() == GridCell.MOLD:
                    for (dx, dy) in ONE_STEP:
                        (new_enemy_x, new_enemy_y) = (dx + enemy_position[0], dy + enemy_position[1])
                        if not self._check_in_bounds(new_enemy_x, new_enemy_y):
                            continue
                        if self._map[new_enemy_x][new_enemy_y] == GridCell.EMPTY and random.random() < enemy.probability:
                            self._map[new_enemy_x][new_enemy_y] = GridCell.ENEMY
                            self._coordinates_to_enemies[(new_enemy_x, new_enemy_y)] = enemy.clone()
                continue

            if self._map[enemy_move_x][enemy_move_y] == GridCell.EMPTY:
                self._coordinates_to_enemies.pop(enemy_position)
                self._map[enemy_move_x][enemy_move_y] = GridCell.ENEMY
                self._map[enemy_position[0]][enemy_position[1]] = GridCell.EMPTY
                self._coordinates_to_enemies[(enemy_move_x, enemy_move_y)] = enemy
            elif self._map[enemy_move_x][enemy_move_y] == GridCell.USER_POSITION:
                user_hero.defence(enemy)
            
        if user_hero.status == CharacterStatus.DEAD:
            self._game_status = Status.DEATH

##########private##########

    def _check_in_bounds(self, row: int, col: int) -> bool:
        return (0 <= row < self._height) and (0 <= col < self._width)

    def _generate_map(self, file_path) -> None:
        self._map: List[List[GridCell]] = []
        self._distance_from_user: List[List[int]] = []
        for i in range(self._height):
            self._map.append([GridCell.EMPTY] * self._width)
            self._distance_from_user.append([-1] * self._width)

        if file_path == '':
            map_builder = RandomMapBuilder(self._map, self._height, self._width, self._max_item_health_point, EnemyFactory(), self)
        else:
            map_builder = FileMapBuilder(self._map, self._height, self._width, self._max_item_health_point, EnemyFactory(), file_path)

        map_builder.generate_walls()
        self._map[self._start_position[0]][self._start_position[1]] = GridCell.USER_POSITION
        self._coordinates_to_items = map_builder.generate_items()
        self._mold_prototype = map_builder.generate_mold_prototype()
        self._coordinates_to_enemies = map_builder.generate_enemies()

    def _print_map(self) -> None:
        for i in range(self._height):
            for j in range(self._width):
                if self._map[i][j] == GridCell.EMPTY and not (i, j) in self._coordinates_to_items:
                    print('.', end=' ')
                elif self._map[i][j] == GridCell.WALL:
                    print('█', end=' ')
                elif self._map[i][j] == GridCell.USER_POSITION:
                    print('@', end=' ')
                elif self._map[i][j] == GridCell.EMPTY and (i, j) in self._coordinates_to_items:
                    item = self._coordinates_to_items[(i, j)]
                    print(item.get_map_symbol(), end=' ')
                elif self._map[i][j] == GridCell.ENEMY:
                    enemy = self._coordinates_to_enemies[(i, j)]
                    if enemy.get_type() == GridCell.AGGRESSIVE_ENEMY:
                        print('a', end=' ')
                    elif enemy.get_type() == GridCell.NEUTRAL_ENEMY:
                        print('n', end=' ')
                    elif enemy.get_type() == GridCell.COWARD_ENEMY:
                        print('c', end=' ')
                    elif enemy.get_type() == GridCell.CONFUSED_ENEMY:
                        print('*', end=' ')
                    elif enemy.get_type() == GridCell.MOLD:
                        print('p', end=' ')
            print()