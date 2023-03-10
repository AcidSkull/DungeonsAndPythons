from Entities.Entity import Entity
from EntityComponents.AI import BaseAI
from EntityComponents.Fighter import Fighter
from typing import Type, Optional

class Actor(Entity):
    def __init__(self, x: int, y: int, name: str, AI: Type[BaseAI], fighter: Fighter):
        super().__init__(x, y, name)
        self.AI: Optional[BaseAI] = AI
        self.fighter = fighter
        self.is_alive = True
        self.stunned = False
    
    def take_damage(self, damage: int):
        self.stunned = True
        self.fighter.hp -= max(damage - self.fighter.defense, 1)
        if(self.fighter.hp == 0): self.die()
    
    def die(self):
        self.is_alive = False