from settings import *
from Entities.Entity import Entity
from EntityComponents.Actor import Actor

class Action():
    def __init__(self, entity: Entity):
        self.entity = entity

    def perform(self):
        raise NotImplementedError()

class EscapeAction(Action):
    def __init__(self):
        pass

    def perform(self):
        return False

class ResetAction(Action):
    def __init__(self):
        pass

    def perform(self, engine):
        engine.init()

class Movement(Action):
    def __init__(self, dx: int, dy: int, entity: Entity):
        super().__init__(entity)
        self.dx = dx
        self.dy = dy
    
    def perform(self, map):
        dest_x = self.entity.get_tile_position_x() + self.dx
        dest_y = self.entity.get_tile_position_y() + self.dy

        if not map.can_walk(dest_x , dest_y, self.entity):
            return

        map.entities_pos[self.entity.get_tile_position_x()][self.entity.get_tile_position_y()] = None
        self.entity.move(self.dx * TILESIZE, self.dy * TILESIZE)
        map.entities_pos[self.entity.get_tile_position_x()][self.entity.get_tile_position_y()] = self.entity

class MeleeAction(Action):
    def __init__(self, dx: int, dy: int, entity: Actor):
        super().__init__(entity)
        self.dx = dx
        self.dy = dy
    
    def perform(self, map):
        dest_x = self.entity.get_tile_position_x() + self.dx
        dest_y = self.entity.get_tile_position_y() + self.dy

        target = map.entities_pos[dest_x][dest_y]

        if target is not None:
            if target.enemy_group == self.entity.enemy_group: return
            damage = self.entity.fighter.power
            target.take_damage(damage)
            print(f"{self.entity.name} punched {target.name}({target.fighter.hp}) and deal {damage} dmg")

class DecideWhatNextAction(Action):
    def __init__(self, dx: int, dy: int, entity: Entity):
        super().__init__(entity)
        self.dx = dx
        self.dy = dy

    def perform(self, map):
        dest_x = self.entity.get_tile_position_x() + self.dx
        dest_y = self.entity.get_tile_position_y() + self.dy

        if map.entities_pos[dest_x][dest_y] is None:
            return Movement(self.dx, self.dy, self.entity).perform(map)
        else:
            return MeleeAction(self.dx, self.dy, self.entity).perform(map)