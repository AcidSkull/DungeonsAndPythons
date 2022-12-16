from Entities import *
import copy

class EntityManager:
    def __init__(self):
        self.entities = {
            "Slime" : Slime.Slime(0, 0),
        }
    
    def spawn(self, name: str, x: int, y: int):
        if not name in self.entities: return None

        clone = copy.deepcopy(self.entities[name])
        clone.x = x
        clone.y = y

        return clone