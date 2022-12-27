import random
from typing import List, Dict

from src.Model.Enemy.Enemy import Enemy, EnemyStyle


style_to_enemy_name: Dict[EnemyStyle, List[str]] = {
    EnemyStyle.FANTASY: [
        'cow', 'pig', 'sheep', 'goat', 'horse', 'dog', 'cat',
    ],
    EnemyStyle.SCIFI: [
        'mail bot', 'power charger', 'ad bot',
    ]
}
neutral_synonyms: List[str] = [
    'indifferent', 'disinterested', 'inactive', 'uninvolved', 'neutral',
]


class NeutralEnemy(Enemy):

    def __init__(self, health_point: int, attack_point: int, enemy_style: EnemyStyle):
        super().__init__(health_point, attack_point, enemy_style)

    def next_move(self, current_position: (int, int), game_map) -> (int, int):
        return current_position

    def get_type(self):
        from src.Model.Map.MapController import GridCell
        return GridCell.NEUTRAL_ENEMY

    def _get_enemy_name(self, enemy_style: EnemyStyle) -> (str, str):
        return random.choice(neutral_synonyms), random.choice(style_to_enemy_name[self._enemy_style])
