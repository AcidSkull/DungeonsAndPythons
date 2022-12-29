from settings import *

class Camera:
    def __init__(self):
        self.viewbox_left = WIDTH / 2 - WIDTH / 8
        self.viewbox_right = HEIGHT / 2  + HEIGHT / 8
        self.position = [0, 0]
    
    def follow(self, shift_x: int, shift_y: int):
        self.position[0] += shift_x
        self.position[1] += shift_y
