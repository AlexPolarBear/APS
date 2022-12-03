from src.Model.Enemy.Enemy import Enemy


class ConfusedEnemy(Enemy):

    def __init__(self, enemy: Enemy):
        self._enemy = enemy
        self._confusion_time = 0
    
    def next_move(self, current_position: (int, int), map) -> (int, int):
        return self._enemy.next_move(current_position, map)
    
    def get_type(self):
        from src.Model.Map import GridCell
        if self._confusion_time > 0:
            return GridCell.CONFUSED_ENEMY
        else:
            return self._enemy.get_type()
