from enum import Enum
from typing import List, Dict

from src.Model.UserHero import CharacterStatus


class EnemyStyle(Enum):
    FANTASY = 0
    SCIFI = 1


class Enemy(object):

    def __init__(self, health_point: int, attack_point: int, enemy_style: EnemyStyle):
        self._health_point = health_point
        self._attack_point = attack_point
        self._status = CharacterStatus.ALIVE
        self._enemy_style = enemy_style
        self._enemy_adjective, self._entity_name = self._get_enemy_name(enemy_style)
    
    @property
    def status(self) -> CharacterStatus:
        return self._status

    @status.setter
    def status(self, value: CharacterStatus):
        self._status = value
    
    @property
    def attack(self) -> int:
        return self._attack_point
    
    @property
    def style(self):
        return self._enemy_style

    @property
    def health(self):
        return self._health_point
    
    @health.setter
    def health(self, value: int):
        self._health_point = value

    @property
    def name(self) -> str:
        return f'{self._enemy_adjective} {self._entity_name}'

    def defence(self, attack_value: int):
        self.health -= attack_value
        if self.health <= 0:
            self.status = CharacterStatus.DEAD

    def next_move(self, current_position: (int, int), map) -> (int, int):
        raise NotImplementedError
    
    def get_type(self):
        raise NotImplementedError

    def _get_enemy_name(self, enemy_style: EnemyStyle) -> (str, str):
        raise NotImplementedError
