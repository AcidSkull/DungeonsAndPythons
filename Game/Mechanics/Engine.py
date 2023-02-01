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
        self.init()
    
    def render(self):
        self.map.update_fov(self.player, 4)
        self.map.render(self.screen)
    
    def message_screen(self, string: str, color):
        font = pygame.font.Font(".\\Assets\\Fonts\\IMMORTAL.ttf", 32)
        self.text = font.render(string, True, color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (WIDTH // 2, HEIGHT // 2)
    
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

            if(self.map.can_walk(direction[0], 0, entity)):
                if(entity.y > self.player.y): direction[1] = -1
                elif(entity.y < self.player.y): direction[1] = 1
            if(self.map.can_walk(0, direction[1], entity)):
                if(entity.y > self.player.y): direction[0] = -1
                elif(entity.y < self.player.y): direction[0] = 1

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
    
    def init(self):
        # self.player.is_alive = True
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
        self.running = True
        self.camera = Camera()
        self.player = Player(self.width // 2 , self.height // 2, self.camera)
        self.entities = [self.player]
        self.event_handler = EventHandler(self.player)
        self.map = Map(MAP_WIDTH, MAP_HEIGHT, self.entities, self.camera)
        self.map.generate_floor(MAX_ROOMS, MIN_ROOM_SIZE, MAX_ROOM_SIZE, MAX_MONSTERS)

    def start(self):
        self.init()

        while self.running:
            self.screen.fill([0,0,0])
            action = None

            if(not self.player.is_alive):
                self.message_screen("You died", (255, 0, 0))
                self.screen.blit(self.text, self.text_rect)
                action = self.event_handler.handle_death_win_screen()
                if isinstance(action, ResetAction):
                    action.perform(self)
            elif(self.player.win):
                self.message_screen("Congratulations! You found the treasure", (0, 255, 0))
                self.screen.blit(self.text, self.text_rect)
                action = self.event_handler.handle_death_win_screen()
                if isinstance(action, ResetAction):
                    action.perform(self)
            else:

                action = self.event_handler.handle_events()

                if isinstance(action, DecideWhatNextAction):
                    action.perform(self.map)
                    self.handle_enemy_turns()

                self.render()

            if isinstance(action, EscapeAction):
                self.running = action.perform()

            pygame.display.flip()
        pygame.quit()