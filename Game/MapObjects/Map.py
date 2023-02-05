from MapObjects.Tiles import *
from MapObjects.Room import Room
from Entities.Player import Player
from Mechanics.EntityManager import EntityManager
from Mechanics.ItemManager import ItemManager
from Mechanics.Camera import Camera
from Items.Item import Sword
from settings import *
import pygame, random

class Map:
    def __init__(self, width: int, height: int, entities: list, camera: Camera):
        self.level = 0
        self.width = width
        self.height = height
        self.entity_manager = EntityManager()
        self.item_manager = ItemManager()
        self.entities = entities
        self.player = entities[0]
        self.tiles = [[Wall(x, y) for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        self.entities_pos = [[None for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        self.camera = camera

        self.tile_png = {
            "Floor" : pygame.image.load(".\\Assets\\Tiles\\Floor.png"),
            "Floor_explored" : pygame.image.load(".\\Assets\\Tiles\\Floor_explored.png"),
            "Wall" : pygame.image.load(".\\Assets\\Tiles\\Wall.png"),
            "Stairs" : pygame.image.load(".\\Assets\\Tiles\\Stairs.png"),
            "Chest_with_gold" : pygame.image.load(".\\Assets\\Tiles\\Chest_with_gold.png"),
            "Sword" : pygame.image.load(".\\Assets\\Items\\Sword.png"),
            "Shield" : pygame.image.load(".\\Assets\\Items\\Shield.png"),
            "HealthPotion" : pygame.image.load(".\\Assets\\Items\\HealthPotion.png"),
        }

        self.entity_sprites = {
            "Player" : pygame.image.load(".\\Assets\\Entities\\Knight.png"),
            "Slime" : pygame.image.load(".\\Assets\\Entities\\Slime.png"),
            "Python" : pygame.image.load(".\\Assets\\Entities\\Python.png"),
            "Skeleton" : pygame.image.load(".\\Assets\\Entities\\Skeleton.png"),
            "Wraith" : pygame.image.load(".\\Assets\\Entities\\Wraith.png"),
            "Snake_warrior" : pygame.image.load(".\\Assets\\Entities\\Snake_warrior.png"),
        }

        self.monster_level = [
            ["Python", "Slime"],
            ["Slime", "Python", "Wraith", "Wraith"],
            ["Wraith", "Wraith", "Wraith", "Slime"],
            ["Skeleton", "Skeleton", "Wraith", "Python"],
            ["Snake_warrior", "Skeleton", "Skeleton", "Wraith"],
        ]

    def clear_map(self):
        for x in range(MAP_WIDTH):
            for y in range(MAP_HEIGHT):
                self.tiles[x][y] = Wall(x, y)
                self.entities_pos[x][y] = None
        
        self.entities.clear()
        self.entities.append(self.player)
    
    def can_walk(self, x: int, y: int, entity: Entity) -> bool:
        if self.entities_pos[x][y] is not None:
            if self.entities_pos[x][y].is_alive == False:
                return True
            return False

        if self.tiles[x][y].walk_in_event:
            self.tiles[x][y].walk_in_event_perform(self, entity)

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
                    screen.blit(self.tile_png[tile.get_texture()], (tile.x - self.camera.position[0], tile.y - self.camera.position[1], tile.x, tile.y))
        
        for entity in self.entities:
            if entity.is_alive == False:
                self.entities_pos[entity.get_tile_position_x()][entity.get_tile_position_y()] = None
                self.entities.remove(entity)

            if self.tiles[entity.get_tile_position_x()][entity.get_tile_position_y()].visible:
                screen.blit(self.entity_sprites[entity.get_sprite()], (entity.x - self.camera.position[0], entity.y - self.camera.position[1], entity.x, entity.y))

    
    def generate_floor(self, max_rooms: int, min_room_size: int, max_room_size: int, max_monsters: int):
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
                    self.player.x = center[0]*TILESIZE
                    self.player.y = center[1]*TILESIZE
                    
                    self.camera.follow(self.player.x - (WIDTH // 2) ,  self.player.y - (HEIGHT // 2))
                    self.entities_pos[center[0]][center[1]] = self.player
                else:
                    previous_center = rooms[-1].get_center()

                    if random.randint(0, 1) == 0:
                        self._generate_horizontal_tunnel(previous_center[0], center[0], previous_center[1])
                        self._generate_vertical_tunnel(previous_center[1], center[1], center[0])
                    else:
                        self._generate_vertical_tunnel(previous_center[1], center[1], previous_center[0])
                        self._generate_horizontal_tunnel(previous_center[0], center[0], center[1])
                    
                    if len(rooms) != max_rooms - 1:
                        self.spawn_monsters(new_room, max_monsters)

                rooms.append(new_room)
            
            tile = rooms[-1].get_center()
            if(self.level == 4):
                self.tiles[tile[0]][tile[1]] = Chest_with_gold(tile[0], tile[1])
            else:
                self.tiles[tile[0]][tile[1]] = Stairs(tile[0], tile[1])
    
    def _generate_room(self, room: Room):
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.tiles[x][y] = Floor(x, y)
        
        if random.randint(0, 1) == 0:
            x = random.randint(room.x1, room.x2)
            y = random.randint(room.y1, room.y2)
        
            self.tiles[x][y].item = self.item_manager.random_spawn()
    
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

            while not self.can_walk(x, y, None):
                x = random.randint(room.x1 + 1, room.x2 - 1)
                y = random.randint(room.y1 + 1, room.y2 - 1)

            entity = self.entity_manager.spawn(self._chose_monster(), x * TILESIZE, y * TILESIZE)
            if entity is not None:
                self.entities.append(entity)
                self.entities_pos[entity.get_tile_position_x()][entity.get_tile_position_y()] = entity
    
    def enter_new_floor(self):
        self.clear_map()
        self.level += 1
        self.generate_floor(MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAX_MONSTERS)
        self.camera.position = [0, 0]
        self.camera.follow(self.player.x - (WIDTH // 2) ,  self.player.y - (HEIGHT // 2))
    
    def finish(self):
        self.player.win = True
    
    def _chose_monster(self) -> str:
        random_int = random.randint(0, len(self.monster_level[self.level]) - 1)
        s = self.monster_level[self.level][random_int]
        return s