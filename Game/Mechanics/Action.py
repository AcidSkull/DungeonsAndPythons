from Entities.Entity import Entity
from MapObjects.Map import Map
from settings import *

class Action():
    def perform(self, entity: Entity):
        raise NotImplementedError()

class Movement(Action):
    def __init__(self, dx, dy):
        super().__init__()
        self.dx = dx
        self.dy = dy
    
    def perform(self, entity: Entity, map: Map):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not map.can_walk(dest_x // TILESIZE, dest_y // TILESIZE):
            return

        entity.move(self.dx, self.dy)