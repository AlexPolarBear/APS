from src.Model.UserHero import CharacterStatus

class Enemy(object):

    def __init__(self, health_point: int, attack_point: int):
        self._health_point = health_point
        self._attack_point = attack_point
        self._status = CharacterStatus.ALIVE
    
    @property
    def status(self) -> CharacterStatus:
        return self._status
    
    @property
    def attack(self) -> int:
        return self._attack_point
    
    @property
    def health(self):
        return self.health
    
    @health.setter
    def health(self, value: int):
        self._health_point = value
    
    def defence(self, attack_value: int):
        self._health_point -= attack_value
        if self._health_point <= 0:
            self._status = CharacterStatus.DEAD

    def next_move(self, current_position: (int, int), map) -> (int, int):
        raise NotImplementedError
    
    def get_type(self):
        raise NotImplementedError
