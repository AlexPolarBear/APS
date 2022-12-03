from src.Model.Backpack import Backpack
from src.Model.Item import Item
from enum import Enum

START_LEVEL = 1
START_POINTS = 0
INCREASE_ATTACK_STEP = 2

class CharacterStatus(Enum):
    ALIVE = 0
    DEAD = 1

class UserHero(object):
    """
    Class representing an user's character in the game world. The character has three parameters: health points,
    attack points and level. In the beggining of the game user has level START_LEVEL 
    """

##########public##########

    def __init__(self, health_point: int, attack_point: int):
        """Create user's character with appropriate health points and attack points."""
        self._health_point = health_point
        self._attack_point = attack_point
        self._level = START_LEVEL
        self._points = START_POINTS
        self._backpack = Backpack()
        self._status = CharacterStatus.ALIVE
    
    @property
    def backpack(self) -> Backpack:
        """Return user's backpack."""
        return self._backpack
    
    @property
    def health_point(self) -> int:
        """Return user's health points."""
        return self._health_point
    
    @property
    def attack_point(self) -> int:
        """Return user's attack points."""
        return self._attack_point
    
    @property
    def level(self) -> int:
        """Return user's level."""
        return self._level
    
    @property 
    def status(self) -> CharacterStatus:
        """Return user's status."""
        return self._status
    
    def activate_item(self, index: int) -> None:
        """Activate item in the backpack with appropriate index."""
        item: Item = self._backpack.get_item(index)
        if item.activate():
            print('aaaaaaaaaa')
            self._health_point += item.health_point
    
    def deactivate_item(self, index: int) -> None:
        """Deactivate item in the backpack with appropriate index."""
        item: Item = self._backpack.get_item(index)
        if item.deactivate():
            self._health_point -= item.health_point
            if self._health_point <= 0:
                self._status = CharacterStatus.DEAD

    def attack(self, enemy):
        enemy.defence(self._attack_point)
        if enemy.status == CharacterStatus.DEAD:
            self._points += 1
            if self._points == self._level:
                self._points = START_POINTS
                self._level += 1
                self._attack_point += INCREASE_ATTACK_STEP
    
    def defence(self, enemy):
        self._health_point -= enemy.attack
        if self._health_point <= 0:
            self._status = CharacterStatus.DEAD
