from Mechanics.Action import *
from Entities.Player import Player
import pygame


class EventHandler:
    def __init__(self, player: Player):
        self.player = player
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EscapeAction()
            
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                return EscapeAction()

            if keys[pygame.K_RIGHT]:
                return DecideWhatNextAction(1, 0, self.player)
            elif keys[pygame.K_LEFT]:
                return DecideWhatNextAction(-1, 0, self.player)
            elif keys[pygame.K_UP]:
                return DecideWhatNextAction(0, -1, self.player)
            elif keys[pygame.K_DOWN]:
                return DecideWhatNextAction(0, 1, self.player)
    
    def handle_death_win_screen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return EscapeAction()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                return EscapeAction()
            
            if keys[pygame.K_r]:
                return ResetAction()
                 