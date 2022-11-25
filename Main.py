from Engine import Engine
from Map import Map
from Entity import Entity
from InputHandler import InputHandler
import pygame

class Main():

    def __init__(self, width: int, height: int):
        self.engine = Engine(width=width, height=height)

    def run(self):
        self.engine.start()
        


if __name__ == '__main__':
    m = Main(800,600)
    m.run()