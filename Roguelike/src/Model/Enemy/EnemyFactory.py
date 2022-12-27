import random

from src.Model.Enemy import Enemy, AggressiveEnemy, NeutralEnemy, CowardEnemy, EnemyStyle, Mold

MAX_ENEMY_HEALTH = 10
MAX_ENEMY_ATTACK = 2
MOLD_PROBABILITY = 0.05


class EnemyFactory(object):
    def __init__(self, enemy_style: EnemyStyle = None):
        self._enemy_types = [AggressiveEnemy, NeutralEnemy, CowardEnemy, Mold]
        if enemy_style is None:
            enemy_style = random.choice(list(EnemyStyle))
        self._enemy_style = enemy_style

    def create_random_enemy(self) -> Enemy:
        enemy_type = random.choice(self._enemy_types)

        enemy_health = random.randrange(MAX_ENEMY_HEALTH) + 1
        enemy_attack = random.randrange(MAX_ENEMY_ATTACK) + 1

        if enemy_type is Mold:
            return enemy_type(enemy_health, enemy_attack, self._enemy_style, MOLD_PROBABILITY)
        else:
            return enemy_type(enemy_health, enemy_attack, self._enemy_style)

    def create_enemy(
            self, health_point: int, attack_point: int, enemy_type: int = None, enemy_style: str = None,
    ) -> Enemy:
        if enemy_type is None:
            enemy_type = random.randrange(len(self._enemy_types))
        if enemy_style is None:
            enemy_style = self._enemy_style

        enemy_type = self._enemy_types[enemy_type]

        return enemy_type(health_point, attack_point, enemy_style)

    def create_mold(self):
        return Mold(random.randrange(MAX_ENEMY_HEALTH) + 1, random.randrange(MAX_ENEMY_ATTACK) + 1,
                    EnemyStyle.SCIFI, MOLD_PROBABILITY)
