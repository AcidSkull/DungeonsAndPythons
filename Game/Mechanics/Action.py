from Entities.Entity import Entity

class Action():
    def perform(self, entity: Entity):
        raise NotImplementedError()

class Movement(Action):
    def __init__(self, dx, dy):
        super().__init__()
        self.dx = dx
        self.dy = dy
    
    def perform(self, entity: Entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        entity.move(self.dx, self.dy)