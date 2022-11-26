import numpy as np
from Tiles import Tile
import pygame

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = self.init_tiles()
        self.tile_png = pygame.image.load(".\\Assets\\Tiles\\Tile.png")
        print(dir(self.tile_png))
    
    def init_tiles(self):
        self.tiles = [[Tile(False) for y in range(self.height)] for x in range(self.width)]
        return Tile
    
    def in_bound(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y <self.height
    
    def render(self, screen: pygame.Surface):
        for x in range(0, self.width, 64):
            for y in range(0, self.height, 64):
                screen.blit(self.tile_png, (x, y))