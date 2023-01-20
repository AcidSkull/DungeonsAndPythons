from EntityComponents.Component import Component
from Entities.Entity import Entity

class Fighter(Component):
    entity: Entity

    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self._hp = hp
        self.defense = defense
        self.power = power
    
    @property
    def hp(self) -> int: return self._hp

    @hp.setter
    def hp(self, x: int):
        self._hp = max(0, min(x, self.max_hp))