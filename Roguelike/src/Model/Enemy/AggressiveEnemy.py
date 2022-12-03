from src.Model.Enemy.Enemy import Enemy


class AggressiveEnemy(Enemy):
    
    def __init__(self, health_point: int, attack_point: int):
        super().__init__(health_point, attack_point)
    
    def next_move(self, current_position: (int, int), map) -> (int, int):
        from src.Model.Map import ONE_STEP
        next_step = current_position
        min_dist: int = 0
        for (dx, dy) in ONE_STEP:
            (new_row, new_col) = (current_position[0] + dx, current_position[1] + dy)
            dst = self.distance_from_user(new_row, new_col)
            if dst != -1:
                if dst > min_dist:
                    min_dist = dst
                    next_step = (new_row, new_col)
        return next_step
    
    def get_type(self):
        from src.Model.Map import GridCell
        return GridCell.AGGRESSIVE_ENEMY
