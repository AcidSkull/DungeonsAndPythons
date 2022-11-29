from Engine import Engine
from Map import Map
from Entity import Entity
from Player import Player
import pygame

class Main():

    def __init__(self, width: int, height: int, player: Player):
        self.engine = Engine(width=width, height=height, entities=[player])

    def run(self):
        self.engine.start()
        


if __name__ == '__main__':
    p = Player(0, 0, "Assets\\Knight.png")

    m = Main(1920, 1080, p)
    m.run()