from MapObjects.Tiles import *
from MapObjects.Room import Room
from Entities.Player import Player
from math import ceil
from tcod.map import compute_fov
from settings import *
import pygame, random

class Map:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.tiles = self.clear_map()

        self.tile_png = {
            "Floor" : pygame.image.load(".\\Assets\\Tiles\\Floor.png"),
            "Floor_explored": pygame.image.load(".\\Assets\\Tiles\\Floor_explored.png"),
            "Wall" : pygame.image.load(".\\Assets\\Tiles\\Wall.png"),
        }
    
    def clear_map(self) -> list():
        return [[Wall(x * TILESIZE, y * TILESIZE) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
    
    def can_walk(self, x: int, y: int) -> bool:
        return not self.tiles[x][y].blocked
    
    def update_fov(self, player: Player, radius: int):
        min_x = max(player.x // TILESIZE - radius, 0)
        max_x = min(player.x // TILESIZE + radius, MAP_WIDTH)
        min_y = max(player.y // TILESIZE - radius, 0)
        max_y = min(player.y // TILESIZE + radius, MAP_HEIGHT)
        
        # for x in range(MAP_WIDTH):
        #     for y in range(MAP_HEIGHT):
        #             self.tiles[x][y].visible = False

        # for x in range(min_x, max_x):
        #     for y in range(min_y, max_y):
        #         self.tiles[x][y].visible = True
        #         self.tiles[x][y].explored = True


        # transparent = [[False for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        # visible = compute_fov(transparent, (player.x // TILESIZE, player.y // TILESIZE), radius=radius)

        # print(visible)

        # for x in range(MAP_WIDTH):
        #     for y in range(MAP_HEIGHT):
        #         if visible[x][y]:
        #             self.tiles[x][y].visible = True
        #             self.tiles[x][y].explored = True
        #         else:
        #             self.tiles[x][y].visible = False

        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                if x <= min_x or x >= max_x:
                    self.tiles[x][y].visible = False
                    continue
                if y <= min_y or y >= max_y:
                    self.tiles[x][y].visible = False
                    continue

                # self.tiles[x][y].visible = True
                # self.tiles[x][y].explored = True
                
                # Finding all tiles between player and this tile
                points = self._cast_ray(player.x // TILESIZE, player.y // TILESIZE, x, y)
                distance = {}
                for p1, p2 in points:
                    distance[(p1, p2)] = self._get_distance_between_tiles(player.x // TILESIZE, player.y // TILESIZE, p1, p2)
                
                points.sort(key=lambda p: distance[(p[0], p[1])])
                tile_visible = True
                for p1, p2 in points:
                    if radius < distance[(p1, p2)]:
                        self.tiles[p1][p2].visible = False
                    else:
                        if self.tiles[p1][p2].blocked:
                            tile_visible = False
                        self.tiles[p1][p2].visible = tile_visible
                    if tile_visible:
                        self.tiles[p1][p2].explored = tile_visible


    def _get_distance_between_tiles(self, x1: int, y1: int, x2: int, y2: int) -> int:
        distance_x = x1 - x2
        distance_y = y1 - y2
        return ((distance_x ** 2) + (distance_y ** 2)) ** 0.5
    
    # Finding all points between start and end coordinates
    def _cast_ray(self, start_x: int, start_y: int, end_x: int, end_y: int) -> list():
        x_diff = start_x - end_x + 0.01
        slope = (start_y - end_y) / x_diff
        y_intercept = start_y - (slope * start_x)

        points = set()

        min_x = min(start_x, end_x)
        max_x = max(start_x, end_x)
        for x in range(min_x, max_x):
            y = (slope * x) + y_intercept
            points.add((x, round(y)))
        
        min_y = min(start_y, end_y)
        max_y = max(start_y, end_y)
        for y in range(min_y, max_y):
            x = (y - y_intercept) / slope
            points.add((round(x), y))
        
        return list(points)

    def render(self, screen: pygame.Surface):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    screen.blit(self. tile_png[tile.get_texture()], (tile.x, tile.y))
    
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
                self._generate_room(new_room)

                center = new_room.get_center()
                if len(rooms) == 0:
                    player.x = center[0]*TILESIZE
                    player.y = center[1]*TILESIZE
                else:
                    previous_center = rooms[-1].get_center()

                    if random.randint(0, 1) == 0:
                        self._generate_horizontal_tunnel(previous_center[0], center[0], previous_center[1])
                        self._generate_vertical_tunnel(previous_center[1], center[1], center[0])
                    else:
                        self._generate_vertical_tunnel(previous_center[1], center[1], previous_center[0])
                        self._generate_horizontal_tunnel(previous_center[0], center[0], center[1])
                
                rooms.append(new_room)
    
    def _generate_room(self, room: Room):
        for x in range(room.DL_TOP + 1, room.DR_TOP):
            for y in range(room.UL_TOP + 1, room.UR_TOP):
                self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)
    
    def _generate_horizontal_tunnel(self, x1: int, x2: int, y: int):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for x in range(min_x, max_x + 1):
            self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)

    def _generate_vertical_tunnel(self, y1: int, y2: int, x: int):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for y in range(min_y, max_y + 1):
            self.tiles[x][y] = Floor(x*TILESIZE, y*TILESIZE)