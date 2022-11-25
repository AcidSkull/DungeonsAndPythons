from Engine import Engine
from Map import Map
from Entity import Entity
from Player import Player
import pygame

class Main():

    def __init__(self, width: int, height: int, player: Player):
        self.engine = Engine(width=width, height=height, entities={player})

    def run(self):
        self.engine.start()
        


if __name__ == '__main__':
    p = Player(100, 100, "Assets\\Knight.png")

    m = Main(800, 600, p)
    m.run()