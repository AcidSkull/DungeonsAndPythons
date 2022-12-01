from Entities.Player import Player
from MapObjects.Map import Map

import pygame

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.running = True
        self.map = Map(800, 800)
        self.player = Player(self.width // 2, self.height //2)
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
                self.move_camera(-64, 0)
                # self.player.move(64, 0)
            elif keys[pygame.K_LEFT]:
                self.move_camera(64, 0)
                # self.player.move(-64, 0)
            elif keys[pygame.K_UP]:
                self.move_camera(0, 64)
                # self.player.move(0, -64)
            elif keys[pygame.K_DOWN]:
                self.move_camera(0, -64)
                # self.player.move(0, 64)

    def move_camera(self, dx: int, dy: int):
        for row in self.map.tiles:
            for tile in row:
                if tile is not None:
                    tile.x += dx
                    tile.y += dy

    def start(self):
        self.map.generate_floor(15, 10, 20, 120, 120, self.player)

        while self.running:
            self.handle_input()
            self.screen.fill([255,255,255])
            self.render()

            pygame.display.flip()
        pygame.quit()