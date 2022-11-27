

class Tile:
    def __init__(self, blocked: bool, texture):
        self.blocked = blocked
        self.texture = texture
    
    def get_texture(self) -> str: return self.texture

class Floor(Tile):
    def __init__(self, texture):
        super().__init__(False, texture)