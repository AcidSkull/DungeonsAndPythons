

class Tile:
    def __init__(self, x: int, y: int, blocked: bool=True, texture=""):
        self.x = x
        self.y = y
        self.blocked = blocked
        self.texture = texture
    
    def get_texture(self) -> str: return self.texture

class Floor(Tile):
    def __init__(self, texture):
        super().__init__(False, texture)