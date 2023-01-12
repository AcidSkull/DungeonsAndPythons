from settings import *

class Tile: 
    def __init__(self, x: int, y: int, blocked: bool):
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.blocked = blocked
        self.visible = False
        self.explored = False
        self.walk_in_event = False
    
    def get_texture(self):
        raise NotImplementedError()
    
    def walk_in_event(self, map):
        raise NotImplementedError()

class Floor(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
    
    def get_texture(self):
        if self.visible:
            return "Floor"
        elif self.explored:
            return "Floor_explored"
        else:
            return "Wall"

class Wall(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, True)
    
    def get_texture(self):
        return "Wall"

class Stairs(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
        self.walk_in_event = True
    
    def get_texture(self):
        if self.visible:
            return "Stairs"
        elif self.explored:
            return "Floor_explored"
        else:
            return "Wall"
    
    def walk_in_event_perform(self, map):
        map.clear_map()