from Entity import Entity
from Map import Map
from InputHandler import InputHandler
from typing import Set, Iterable, Any

import pygame

class Engine:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.running = True
    
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def start(self):
        while self.running:
            self.handle_input()

            self.screen.fill([255,255,255])
            pygame.display.flip()
        pygame.quit()