from Entities.Player import Player
from settings import *
import pygame

class UserInterface:
    def __init__(self, player: Player, screen: pygame.Surface):
        self.player = player
        self.screen = screen
        self.ui_textures = {
            "Heart" : pygame.image.load(".\\Assets\\UI\\heart_point.png"),
            "Defense" : pygame.image.load(".\\Assets\\UI\\defense_point.png"),
            "Power" : pygame.image.load(".\\Assets\\UI\\power_point.png"),
        }
        self.font = pygame.font.Font(".\\Assets\\Fonts\\IMMORTAL.ttf", 32)
        self.text = [None, None, None]
        self.text_rect = [None, None, None]
        self._update_text()

    def _update_text(self):
        self.text[0] = self.font.render(str(self.player.fighter.hp), True, (255, 255, 255))
        self.text[1] = self.font.render(str(self.player.fighter.defense), True, (255, 255, 255))
        self.text[2] = self.font.render(str(self.player.fighter.power), True, (255, 255, 255))

        self.text_rect[0] = self.text[0].get_rect()
        self.text_rect[0].center = (80, 25)

        self.text_rect[1] = self.text[1].get_rect()
        self.text_rect[1].center = (80, 60)

        self.text_rect[2] = self.text[2].get_rect()
        self.text_rect[2].center = (80, 100)
    
    def render(self):
        self._update_text()
        self.screen.blit(self.ui_textures['Heart'], (8, 8))
        self.screen.blit(self.text[0], self.text_rect[0])

        self.screen.blit(self.ui_textures['Defense'], (8, 40))
        self.screen.blit(self.text[1], self.text_rect[1])

        self.screen.blit(self.ui_textures['Power'], (8,80))
        self.screen.blit(self.text[2], self.text_rect[2])