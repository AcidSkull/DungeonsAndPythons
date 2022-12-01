from Entities.Entity import Entity

class Player(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, ".\\Assets\\Entities\\Knight.png")