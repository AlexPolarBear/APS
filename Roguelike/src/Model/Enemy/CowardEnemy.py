import random
from typing import Dict, List

from src.Model.Enemy.Enemy import Enemy, EnemyStyle


style_to_enemy_name: Dict[EnemyStyle, List[str]] = {
    EnemyStyle.FANTASY: [
        'chicken', 'rabbit', 'mouse',
    ],
    EnemyStyle.SCIFI: [
        'cleaning bot', 'scrapper',
    ]
}
coward_synonyms: List[str] = [
    'scared', 'frightened', 'timid', 'coward',
]


class CowardEnemy(Enemy):

    def __init__(self, health_point: int, attack_point: int, enemy_style: EnemyStyle):
        super().__init__(health_point, attack_point, enemy_style)

    def next_move(self, current_position: (int, int), map) -> (int, int):
        from src.Model.Map.Map import ONE_STEP
        next_step = current_position
        max_dist: int = 0
        for (dx, dy) in ONE_STEP:
            (new_row, new_col) = (current_position[0] + dx, current_position[1] + dy)
            dst = map.distance_from_user(new_row, new_col)
            if dst != -1:
                if dst > max_dist:
                    max_dist = dst
                    next_step = (new_row, new_col)
        return next_step
    
    def get_type(self):
        from src.Model.Map.Map import GridCell
        return GridCell.COWARD_ENEMY

    def _get_enemy_name(self, enemy_style: EnemyStyle) -> (str, str):
        return random.choice(coward_synonyms), random.choice(style_to_enemy_name[self._enemy_style])
