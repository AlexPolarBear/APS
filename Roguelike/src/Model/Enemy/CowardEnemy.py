from src.Model.Enemy.Enemy import Enemy


class CowardEnemy(Enemy):

    def __init__(self, health_point: int, attack_point: int):
        super().__init__(health_point, attack_point)
    
    def next_move(self, map) -> (int, int):
        raise NotImplementedError