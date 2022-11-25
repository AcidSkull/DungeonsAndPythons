from Entity import Entity
import pygame

class Player(Entity):
    def __init__(self, x: int, y: int, sprite: str):
        super().__init__(x, y, sprite)
        