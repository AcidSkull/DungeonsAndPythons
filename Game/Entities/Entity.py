import pygame

class Entity():
    def __init__(self, x: int, y: int, sprite: str):
        self.x = x
        self.y = y
        self.sprite = pygame.image.load(sprite)
    
    def move(self, dx: int, dy: int):
        self.x += dx
        self.y += dy

    def get_coordinates(self):
        return (self.x, self.y)