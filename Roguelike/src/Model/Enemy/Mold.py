from src.Model.Enemy.NeutralEnemy import NeutralEnemy
from src.Model.Enemy.Enemy import EnemyStyle

class Mold(NeutralEnemy):
    """Class for mold, that can duplicate self on adjacent cell of the map with some probability."""
    def __init__(self, health_point: int, attack_point: int, enemy_style: EnemyStyle, probability: float):
        super().__init__(health_point, attack_point, enemy_style)
        self._probability = probability

    def get_type(self):
        from src.Model.Map.MapController import GridCell
        return GridCell.MOLD

    @property
    def probability(self) -> float:
        return self._probability

    def _get_enemy_name(self, enemy_style: EnemyStyle) -> (str, str):
        enemy_adjective, entity_name = super()._get_enemy_name(enemy_style)
        entity_name = 'mold'
        return enemy_adjective, entity_name

    def clone(self):
        """Create copy of the current mold."""
        return Mold(self._health_point, self._attack_point, self._enemy_style, self._probability)
