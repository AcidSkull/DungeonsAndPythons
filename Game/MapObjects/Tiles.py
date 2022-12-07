

class Tile:
    def __init__(self, x: int, y: int, blocked: bool=True):
        self.x = x
        self.y = y
        self.blocked = blocked
        self.visible = False
        self.explored = False
    
    def get_texture(self):
        raise NotImplementedError()

class Floor(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)
    
    def get_texture(self):
        if self.visible:
            return "Floor"
        elif self.explored:
            return "Floor_dark"
        else:
            return "Wall"

class Wall(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, True)
    
    def get_texture(self):
        return "Wall"