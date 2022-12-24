import random
from typing import List, Dict

from src.Model.Enemy.Enemy import Enemy, EnemyStyle


style_to_enemy_name: Dict[EnemyStyle, List[str]] = {
    EnemyStyle.FANTASY: [
        'goblin', 'orc', 'troll', 'giant', 'dragon', 'demon', 'golem'
    ],
    EnemyStyle.SCIFI: [
        'alien', 'security bot', 'robot', 'cyborg', 'droid',
    ]
}
aggressive_synonyms: List[str] = [
    'aggressive', 'hostile', 'combative', 'ruthless', 'fierce',
]


class AggressiveEnemy(Enemy):
    def __init__(self, health_point: int, attack_point: int, enemy_style: EnemyStyle):
        super().__init__(health_point, attack_point, enemy_style)
    
    def next_move(self, current_position: (int, int), game_map) -> (int, int):
        from src.Model.Map import ONE_STEP
        next_step = current_position
        min_dist: int = -1
        for (dx, dy) in ONE_STEP:
            (new_row, new_col) = (current_position[0] + dx, current_position[1] + dy)
            dst = game_map.distance_from_user(new_row, new_col)
            if dst != -1:
                if min_dist == -1:
                    min_dist = dst
                    next_step = (new_row, new_col)
                elif dst < min_dist:
                    min_dist = dst
                    next_step = (new_row, new_col)
        return next_step

    def get_type(self):
        from src.Model.Map import GridCell
        return GridCell.AGGRESSIVE_ENEMY

    def _get_enemy_name(self, enemy_style: EnemyStyle) -> (str, str):
        return random.choice(aggressive_synonyms), random.choice(style_to_enemy_name[self._enemy_style])
