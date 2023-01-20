from EntityComponents.Actor import Actor
from EntityComponents.Fighter import Fighter
from EntityComponents.AI import BaseAI
import copy

class EntityManager:
    def __init__(self):
        self.entities = {
            "Slime" : Actor(0, 0, "Slime", BaseAI(), Fighter(10, 5, 2)),
        }
    
    def spawn(self, name: str, x: int, y: int):
        if not name in self.entities: return None

        clone = copy.deepcopy(self.entities[name])
        clone.x = x
        clone.y = y

        return clone