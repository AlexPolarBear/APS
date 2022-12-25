import random
from typing import List

from src.Model.Enemy.Enemy import Enemy, EnemyStyle
from src.Model.UserHero import CharacterStatus

CRITICAL_LEVEL = 5

class EnemyContext(object):
    """Class that store information about enemy and its state."""

    def __init__(self, enemy: Enemy):
        self._enemy = enemy
        self._original_state = enemy

    @property
    def status(self) -> CharacterStatus:
        return self._enemy.status

    @status.setter
    def status(self, value: CharacterStatus):
        self._enemy.status = value
        self._original_state.status = value

    @property
    def attack(self) -> int:
        return self._enemy.attack

    @property
    def health(self):
        return self._enemy.health

    @health.setter
    def health(self, value: int):
        if self.health >= CRITICAL_LEVEL and value < CRITICAL_LEVEL:
            self._original_state = self._enemy
            self._enemy = CowardEnemy(self._enemy.health, self._enemy.attack, self._enemy.style)
        elif self.health < CRITICAL_LEVEL and value >= CRITICAL_LEVEL:
            self._enemy = self._original_state

        self._enemy.health = value
        self._original_state.health = value

    @property
    def name(self) -> str:
        return self._enemy.name

    @property
    def probability(self) -> float:
        return self._enemy.probability

    def next_move(self, current_position: (int, int), map) -> (int, int):
        return self._enemy.next_move(current_position, map)

    def get_type(self):
        return self._enemy.get_type()

    def clone(self):
        return self._enemy.clone()
    
    def defence(self, attack: int):
        if self.health >= CRITICAL_LEVEL and self.health - value < CRITICAL_LEVEL:
            self._original_state = self._enemy
            self._enemy = CowardEnemy(self._enemy.health, self._enemy.attack, self._enemy.style)
        elif self.health < CRITICAL_LEVEL and self.Health - value >= CRITICAL_LEVEL:
            self._enemy = self._original_state

        self._enemy.defence(attack)
        if self._enemy is not self._original_state:
            self._original_state.defence(attack)
