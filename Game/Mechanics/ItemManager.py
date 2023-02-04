from Items.Item import *
import copy, random

class ItemManager:
    def __init__(self):
        self.items = {
            "Sword" : Sword(),
            "Shield" : Shield(),
            "HealthPotion" : HealthPotion(),
        }
    
    def spawn(self, name: str) -> Item:
        if not name in self.items: return None

        clone = copy.deepcopy(self.items[name])

        return clone
    
    def random_spawn(self) -> Item:
        x = random.randint(0, len(self.items) - 1)
        l = list(self.items.values())
        item = self.spawn(l[x].name)
        
        return item
