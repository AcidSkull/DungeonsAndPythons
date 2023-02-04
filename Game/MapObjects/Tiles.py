from Entities.Entity import Entity
from Items.Item import Item
from settings import *

class Tile: 
    def __init__(self, x: int, y: int, blocked: bool):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.blocked = blocked
        self.visible = False
        self.explored = False
        self.walk_in_event = False
    
    def get_texture(self) -> str:
        raise NotImplementedError()
    
    def walk_in_event(self, map, entity: Entity):
        raise NotImplementedError()

class Floor(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
        self.item = None
        self.walk_in_event = True

    def give_item(self, item: Item):
        self.item = item
    
    def get_texture(self) -> str:
        if self.visible:
            if self.item is not None:
                return self.item.name
            return "Floor"
        elif self.explored:
            return "Floor_explored"
        else:
            return "Wall"
    
    def walk_in_event_perform(self, map, entity: Entity):
        if entity is None: return

        if entity.name == "Player" and self.item is not None:
            self.item.use(entity)
            self.item = None

class Wall(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, True)
    
    def get_texture(self) -> str:
        return "Wall"

class Stairs(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
        self.walk_in_event = True
    
    def get_texture(self) -> str:
        if self.visible:
            return "Stairs"
        elif self.explored:
            return "Floor_explored"
        else:
            return "Wall"
    
    def walk_in_event_perform(self, map, entity: Entity):
        if(entity.name == "Player"):
            map.enter_new_floor()
    
class Chest_with_gold(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
        self.walk_in_event = True
    
    def get_texture(self) -> str:
        if self.visible:
            return "Chest_with_gold"
        elif self.explored:
            return "Floor_explored"
        else:
            return "Wall"
    
    def walk_in_event_perform(self, map, entity: Entity):
        if(entity.name == "Player"):
            map.finish()