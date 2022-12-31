from Entities.Entity import Entity
from MapObjects.Map import Map
from Mechanics.Camera import Camera
from settings import *

class Action():
    def perform(self, entity: Entity):
        raise NotImplementedError()

class Movement(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()
        self.dx = dx
        self.dy = dy
    
    def perform(self, entity: Entity, map: Map):
        map.entities_pos[entity.get_tile_position_x()][entity.get_tile_position_y()] = None

        dest_x = entity.get_tile_position_x() + self.dx
        dest_y = entity.get_tile_position_y() + self.dy

        if not map.can_walk(dest_x , dest_y):
            return

        entity.move(self.dx * TILESIZE, self.dy * TILESIZE)
        map.entities_pos[entity.get_tile_position_x()][entity.get_tile_position_y()] = entity

class MeleeAction(Action):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy
    
    def perform(self, entity: Entity, map: Map):
        dest_x = entity.get_tile_position_x() + self.dx
        dest_y = entity.get_tile_position_y() + self.dy
        target = map.entities_pos[dest_x][dest_y]

        if target is not None:
            print(f"You punched {target.name}")

class DecideWhatNextAction(Action):
    def __init__(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def perform(self, entity: Entity, map: Map):
        dest_x = entity.get_tile_position_x() + self.dx
        dest_y = entity.get_tile_position_y() + self.dy

        if map.entities_pos[dest_x][dest_y] is None:
            return Movement(self.dx, self.dy).perform(entity, map)
        else:
            return MeleeAction(self.dx, self.dy).perform(entity, map)