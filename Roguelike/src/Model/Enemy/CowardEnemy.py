from src.Model.Enemy.Enemy import Enemy


class CowardEnemy(Enemy):

    def __init__(self, health_point: int, attack_point: int):
        super().__init__(health_point, attack_point)
    
    def next_move(self, current_position: (int, int), map) -> (int, int):
        return current_position
    
    def get_type(self):
        from src.Model.Map import GridCell
        return GridCell.COWARD_ENEMY
