from settings import *

class Entity():
    def __init__(self, x: int, y: int, name: str):
        self.x = x
        self.y = y
        self.name = name
    
    def get_sprite(self): return self.name
    
    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def get_coordinates(self): return (self.x, self.y)
    def get_tile_coordinates(self): return (self.x // TILESIZE, self.y // TILESIZE)    
    def get_tile_position_x(self): return self.x // TILESIZE
    def get_tile_position_y(self): return self.y // TILESIZE
