from EntityComponents.Actor import Actor
from EntityComponents.Fighter import Fighter
from EntityComponents.AI import BaseAI
import copy

class EntityManager:
    def __init__(self):
        self.entities = {
            "Slime" : Actor(0, 0, "Slime", BaseAI(), Fighter(8, 2, 2)),
            "Python" : Actor(0, 0, "Python", BaseAI(), Fighter(5, 1, 2)),
            "Skeleton" : Actor(0, 0, "Skeleton", BaseAI(), Fighter(15, 3, 3)),
            "Wraith" : Actor(0, 0, "Wraith", BaseAI(), Fighter(15, 5, 3)),
            "Snake_warrior" : Actor(0, 0, "Snake_warrior", BaseAI(), Fighter(20, 6, 4)),
        }
    
    def spawn(self, name: str, x: int, y: int):
        if not name in self.entities: return None

        clone = copy.deepcopy(self.entities[name])
        clone.x = x
        clone.y = y

        return clone