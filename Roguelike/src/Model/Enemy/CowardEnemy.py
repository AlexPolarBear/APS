from src.Model.Enemy.Enemy import Enemy


class CowardEnemy(Enemy):

    def __init__(self, health_point: int, attack_point: int):
        super().__init__(health_point, attack_point)
    
    def next_move(self, current_position: (int, int), map) -> (int, int):
        from src.Model.Map import ONE_STEP
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
        from src.Model.Map import GridCell
        return GridCell.COWARD_ENEMY
