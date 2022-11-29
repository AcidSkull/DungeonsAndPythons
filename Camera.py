from Player import Player
import pygame

class Camera:
    def __init__(self, player: Player, width: int, height: int):
        self.player = player
        self.offset = pygame.math.Vector2(0, 0)
        self.offset_float = pygame.math.Vector2(0, 0)
        self.width = width
        self.height = height
        self.CONST = pygame.math.Vector2(-self.width / 2 + player.x / 2, -self.height + player.y)