import pygame as pg
import sys
from TileMap import *
from Player import *

class Game:
    WIDTH = 1920
    HEIGHT = 1080

    tile_image = pg.image.load("Assets/Tile.png")

    def __init__(self):
        pg.init()
        pg.display.set_caption('Dungeon and Pythons')
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT), pg.FULLSCREEN)
        self.tile_map = TileMap("Assets/Tile.png")
        self.player = Player()
        self.running = True
    
    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pg.quit()
    
    def draw(self):
        self.screen.fill((255,255,255))

        self.draw_grid()
        # self.tile_map.render(self.screen)

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event == pg.QUIT or event.type == pg.K_ESCAPE:
                self.running = False
        

    def update(self):
        pass    

    def draw_grid(self):
        for x in range(0, 1920, 64):
            for y in range(0, 1080, 64):
                self.screen.blit(self.tile_image, (x, y))

if __name__ == '__main__':
    g = Game()
    g.run()