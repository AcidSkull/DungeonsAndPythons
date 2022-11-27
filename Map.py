from Tiles import *
import pygame

class Map:
    def __init__(self, width: int, height: int):
        self.width = width // 64
        self.height = height // 64
        # self.tiles = self.init_tiles()
        self.tile_png = self.init_images()
    
    def init_tiles(self):
        tiles = [[Tile() for y in range(self.height)] for x in range(self.width)]
        return tiles
    
    def init_images(self):
        tile_png = {
            "Floor" : pygame.image.load(".\\Assets\\Tiles\\Tile.png"),
            "Wall" : pygame.image.load(".\\Assets\\Tiles\\Wall.png"),
        }
        return tile_png
    
    def in_bound(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y <self.height
    
    def render(self, screen: pygame.Surface):
        for x in range(0, self.width):
            for y in range(0, self.height):
                # print(self.tiles[x][y].get_texture())
                screen.blit(self.tile_png["Floor"], (x*64, y*64))
                # screen.blit(self.tiles[x][y].get_texture(), (x * 64, y * 64))