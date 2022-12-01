from Mechanics.Engine import Engine

class Main():

    def __init__(self, width: int, height: int):
        self.engine = Engine(width=width, height=height)

    def run(self):
        self.engine.start()
        


if __name__ == '__main__':
    # import pygame
    # pygame.init()
    # from Entities.Player import Player
    # p = Player(100,100)
    # surface = pygame.display.set_mode([1920,1080])
    # while True:
    #     pygame.Surface.blit(surface, Player.sprite, (Player.x, Player.y))
    #     # surface.blit(Player.sprite, (Player.x, Player.y))
    #     pygame.display.flip()
    m = Main(1920, 1080)
    m.run()