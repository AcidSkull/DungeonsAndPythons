from Entities.Player import Player
from MapObjects.Map import Map
from settings import *

import pygame

class Engine:
    def __init__(self):
        pygame.init()
        self.width = WIDTH
        self.height = HEIGHT
        self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
        self.running = True
        self.map = Map(MAP_WIDTH, MAP_HEIGHT)
        self.player = Player(self.width // 2 , self.height //2)
        self.entities = [self.player]
    
    def render(self):
        self.map.render(self.screen)

        for entity in self.entities:
            self.screen.blit(entity.sprite, (entity.x, entity.y))
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.running = False

            if keys[pygame.K_RIGHT]:
                self.player.move(TILESIZE, 0)
                # self.move_camera(-64, 0)
            elif keys[pygame.K_LEFT]:
                self.player.move(-TILESIZE, 0)
                # self.move_camera(64, 0)
            elif keys[pygame.K_UP]:
                self.player.move(0, -TILESIZE)
                # self.move_camera(0, 64)
            elif keys[pygame.K_DOWN]:
                self.player.move(0, TILESIZE)
                # self.move_camera(0, -64)

    def move_camera(self, dx: int, dy: int):
        for row in self.map.tiles:
            for tile in row:
                if tile is not None:
                    tile.x += dx
                    tile.y += dy

    def start(self):
        self.map.generate_floor(25, 3, 6, self.player)

        while self.running:
            self.handle_input()
            self.screen.fill([255,255,255])
            self.render()

            pygame.display.flip()
        pygame.quit()