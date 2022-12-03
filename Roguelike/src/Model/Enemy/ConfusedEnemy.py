from src.Model.Enemy.Enemy import Enemy


class ConfusedEnemy(Enemy):

    def __init__(self, enemy: Enemy):
        self._enemy = enemy
        self._confusion_time = 0
    
    def next_move(self, map) -> (int, int):
        raise NotImplementedError