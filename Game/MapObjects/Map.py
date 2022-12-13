from MapObjects.Tiles import *
from MapObjects.Room import Room
from Entities.Player import Player
from Entities.Slime import Slime
from settings import *
import pygame, random

class Map:
    def __init__(self, width: int, height: int, entities: list):
        self.width = width
        self.height = height
        self.entities = entities
        self.tiles = self.clear_map()
        self.visible = [[False for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]

        self.tile_png = {
            "Floor" : pygame.image.load(".\\Assets\\Tiles\\Floor.png"),
            "Floor_explored": pygame.image.load(".\\Assets\\Tiles\\Floor_explored.png"),
            "Wall" : pygame.image.load(".\\Assets\\Tiles\\Wall.png"),
        }

        self.entity_sprites = {
            "Player" : pygame.image.load(".\\Assets\\Entities\\Knight.png"),
            "Slime" : pygame.image.load(".\\Assets\\Entities\\Slime.png"),
        }
    
    def clear_map(self) -> list():
        return [[Wall(x, y) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
    
    def can_walk(self, x: int, y: int) -> bool:
        return not self.tiles[x][y].blocked
    
    def update_fov(self, player: Player, radius: int):
        min_x = player.get_tile_position_x() - radius
        max_x = player.get_tile_position_x() + radius
        min_y = player.get_tile_position_y() - radius
        max_y = player.get_tile_position_y() + radius
        
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                if x <= min_x or x >= max_x:
                    self.tiles[x][y].visible = False
                    continue
                if y <= min_y or y >= max_y:
                    self.tiles[x][y].visible = False
                    continue

                # Finding all tiles between player and this tile
                points = self._cast_ray(player.get_tile_position_x(), player.get_tile_position_y(), x, y)
                distance = {}
                for p1, p2 in points:
                    distance[(p1, p2)] = self._get_distance_between_tiles(player.get_tile_position_x(), player.get_tile_position_y(), p1, p2)
                
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
                    screen.blit(self.tile_png[tile.get_texture()], (tile.x, tile.y))
        
        for entity in self.entities:
            if self.tiles[entity.get_tile_position_x()][entity.get_tile_position_y()].visible:
                screen.blit(self.entity_sprites[entity.get_sprite()], (entity.x, entity.y))

    
    def generate_floor(self, max_rooms: int, min_room_size: int, max_room_size: int, max_monsters: int, player: Player):

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
                
                self.spawn_monsters(new_room, max_monsters)

                rooms.append(new_room)
    
    def _generate_room(self, room: Room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y] = Floor(x, y)
    
    def _generate_horizontal_tunnel(self, x1: int, x2: int, y: int):
        min_x = min(x1, x2)
        max_x = max(x1, x2)
        for x in range(min_x, max_x + 1):
            self.tiles[x][y] = Floor(x, y)

    def _generate_vertical_tunnel(self, y1: int, y2: int, x: int):
        min_y = min(y1, y2)
        max_y = max(y1, y2)
        for y in range(min_y, max_y + 1):
            self.tiles[x][y] = Floor(x, y)
    
    def spawn_monsters(self, room: Room, max_monsters: int):
        number_of_monsters = random.randint(0, max_monsters)

        for i in range(number_of_monsters):
            x = random.randint(room.x1 + 1, room.x2 - 1)
            y = random.randint(room.y1 + 1, room.y2 - 1)

            slime = Slime(x * TILESIZE, y * TILESIZE)
            self.entities.append(slime)