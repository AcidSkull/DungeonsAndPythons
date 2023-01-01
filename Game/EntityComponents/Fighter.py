from EntityComponents.Component import Component

class Fighter(Component):
    def __init__(self, hp: int, defense: int, power: int):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
    
    @property
    def hp(self) -> int: return self.hp

    @hp.setter
    def hp(self, x: int):
        self.hp = max(0, min(x, self.max_hp))
    