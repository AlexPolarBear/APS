import random
from typing import List

from src.Model.Enemy.Enemy import Enemy, EnemyStyle
from src.Model.UserHero import CharacterStatus


confused_adjectives: List[str] = [
    'confused', 'dazed', 'disoriented', 'perplexed',
]

class ConfusedEnemy(Enemy):

    def __init__(self, enemy: Enemy):
        self._enemy = enemy
        self._confusion_time = 0
        self._enemy_adjective = random.choice(confused_adjectives)
    
    @property
    def status(self) -> CharacterStatus:
        return self._enemy.status

    @status.setter
    def status(self, value: CharacterStatus):
        self._enemy.status = value

    @property
    def attack(self) -> int:
        return self._enemy.attack

    @property
    def health(self):
        return self._enemy.health
    
    @health.setter
    def health(self, value: int):
        self._enemy.health = value

    @property
    def name(self) -> str:
        # return f'{self._enemy_adjective} {" ".join(self._enemy.name.split(" ")[1:])}'
        return self._enemy.name
    
    def next_move(self, current_position: (int, int), map) -> (int, int):
        return self._enemy.next_move(current_position, map)
    
    def get_type(self):
        from src.Model.Map.Map import GridCell
        if self._confusion_time > 0:
            return GridCell.CONFUSED_ENEMY
        else:
            return self._enemy.get_type()
