from telnetlib import GA
from turtle import Screen
import pygame as pg

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((1920, 1080))
    
    def run(self):
        while True:
            self.draw()
    
    def draw(self):
        self.screen.fill((100,255,255))
        pg.display.flip()

if __name__ == '__main__':
    g = Game()
    g.run()