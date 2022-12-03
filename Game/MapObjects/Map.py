from MapObjects.Tiles import *
from MapObjects.Room import Room
from Entities.Player import Player
from typing import Tuple
from settings import *
import pygame, random

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = self.init_tiles()
        self.tile_png = self.init_images()
    
    def init_tiles(self):
        tiles = [[Wall(x*TILESIZE, y*TILESIZE) for y in range(self.height)] for x in range(self.width)]
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
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    screen.blit(self.tile_png[tile.__class__.__name__], (tile.x, tile.y))
    
    def generate_floor(self, max_rooms: int, min_room_size: int, max_room_size: int, player: Player):

        rooms: list[Room] = list()

        for room in range(max_rooms):
            # Randomize room width and height
            width = random.randint(min_room_size, max_room_size)
            height = random.randint(min_room_size, max_room_size)

            # Randomize room position
            x = random.randint(0, MAP_WIDTH - width - 1)
            y = random.randint(0, MAP_HEIGHT - height - 1)

            new_room = Room(x, y, width, height)

            for other_room in rooms:
                if new_room in other_room:
                    continue
            else:
                self.generate_room(new_room)

                center = new_room.get_center()
                if len(rooms) == 0:
                    pass
                else:
                    previous_center = rooms[-1].get_center()

                    if random.randint(0, 1) == 0:
                        self.generate_horizontal_tunnel(previous_center[0], center[0], previous_center[1])
                        self.generate_vertical_tunnel(previous_center[1], center[1], center[0])
                    else:
                        self.generate_vertical_tunnel(previous_center[1], center[1], previous_center[0])
                        self.generate_horizontal_tunnel(previous_center[0], center[0], center[1])
                
                rooms.append(new_room)
    
    def generate_room(self, room: Room):
        for x in range(room.DL_TOP + 1, room.DR_TOP):
            for y in range(room.UL_TOP + 1, room.UR_TOP):
                self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)
    
    def generate_horizontal_tunnel(self, x1: int, x2: int, y: int):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for x in range(min_x, max_x + 1):
            self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)

    def generate_vertical_tunnel(self, y1: int, y2: int, x: int):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for y in range(min_y, max_y + 1):
            self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)