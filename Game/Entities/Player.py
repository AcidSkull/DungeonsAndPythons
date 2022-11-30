from Entities.Entity import Entity

class Player(Entity):
    def __init__(self, x: int, y: int, sprite: str):
        super().__init__(x, y, sprite)
        