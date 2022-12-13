from Entities.Entity import Entity

class Slime(Entity):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Slime")