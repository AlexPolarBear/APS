from src.Model.UserHero import CharacterStatus

class Enemy(object):

    def __init__(self, health_point: int, attack_point: int):
        self._health_point = health_point
        self._attack_point = attack_point
        self._status = CharacterStatus.ALIVE
    
    @property
    def status(self) -> CharacterStatus:
        return self._status

    @status.setter
    def status(self, value: CharacterStatus):
        self._status = value
    
    @property
    def attack(self) -> int:
        return self._attack_point
    
    @property
    def health(self):
        return self._health_point
    
    @health.setter
    def health(self, value: int):
        self._health_point = value

    def defence(self, attack_value: int):
        self.health -= attack_value
        if self.health <= 0:
            self.status = CharacterStatus.DEAD

    def next_move(self, current_position: (int, int), map) -> (int, int):
        raise NotImplementedError
    
    def get_type(self):
        raise NotImplementedError
