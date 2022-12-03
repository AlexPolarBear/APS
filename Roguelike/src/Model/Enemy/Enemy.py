class Enemy(object):

    def __init__(self, health_point: int, attack_point: int):
        self._health_point = health_point
        self._attack_point = attack_point

    def next_move(self, map) -> (int, int):
        raise NotImplementedError