

class Tile:
    def __init__(self, x: int, y: int, blocked: bool=True):
        self.x = x
        self.y = y
        self.blocked = blocked

class Floor(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, False)

class Wall(Tile):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, True)