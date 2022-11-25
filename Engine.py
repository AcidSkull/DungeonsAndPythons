from Entity import Entity
from Map import Map
from typing import Set, Iterable, Any

import pygame

class Engine:
    def __init__(self, width, height, entities: list):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.entities = entities
        self.running = True
        self.player = entities[0]
    
    def render(self):
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
                self.player.move(32, 0)
            elif keys[pygame.K_LEFT]:
                self.player.move(-32, 0)
            elif keys[pygame.K_UP]:
                self.player.move(0, -32)
            elif keys[pygame.K_DOWN]:
                self.player.move(0, 32)

    
    def start(self):
        while self.running:
            self.handle_input()
            self.screen.fill([255,255,255])
            self.render()

            pygame.display.flip()
        pygame.quit()