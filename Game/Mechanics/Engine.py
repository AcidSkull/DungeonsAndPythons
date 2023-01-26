from Entities.Player import Player
from Mechanics.Camera import Camera
from Mechanics.EventHandler import EventHandler
from MapObjects.Map import Map
from Mechanics.Action import *
from settings import *
import pygame

class Engine:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dungeons&Pythons")
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
        self.running = True
        self.camera = Camera()
        self.player = Player(self.width // 2 , self.height // 2, self.camera)
        self.entities = [self.player]
        self.event_handler = EventHandler(self.player)
        self.map = Map(MAP_WIDTH, MAP_HEIGHT, self.entities, self.camera)
    
    def render(self):
        self.map.update_fov(self.player, 4)
        self.map.render(self.screen)
    
    def handle_enemy_turns(self):
        for entity in self.entities:
            if entity == self.player: continue
            if entity.stunned:
                entity.stunned = False
                continue

            direction = [0, 0]
            if(entity.x > self.player.x): direction[0] = -1
            elif(entity.x < self.player.x): direction[0] = 1
            elif(entity.y > self.player.y): direction[1] = -1
            elif(entity.y < self.player.y): direction[1] = 1

            action = DecideWhatNextAction(direction[0], direction[1], entity)
            action.perform(self.map)

            # path = entity.AI.get_path_to(entity.get_tile_position_x(), entity.get_tile_position_y(), self.player.get_tile_position_x(), self.player.get_tile_position_y(), self.map.tiles)

            # print(path)
            # if path is not None:
            #     q = path.get()
            #     print(q)
                # direction = (entity.get_tile_position_x() - q[2], entity.get_tile_position_y() - q[3])

                # action = DecideWhatNextAction(direction[0], direction[1], entity)
                # action.perform(self.map)
            # print(f'{self.player.x},{self.player.y} {entity}')
            # print(f'{entity.name} is haeding towards you!')

    def start(self):
        self.map.generate_floor(MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAX_MONSTERS)

        while self.running:
            action = self.event_handler.handle_events()

            if isinstance(action, EscapeAction):
                self.running = action.perform()

            if isinstance(action, DecideWhatNextAction):
                action.perform(self.map)
                self.handle_enemy_turns()

            self.screen.fill([0,0,0])
            self.render()

            pygame.display.flip()
        pygame.quit()