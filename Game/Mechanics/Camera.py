from settings import *

class Camera:
    def __init__(self):
        self.position = [0, 0]
    
    def follow(self, shift_x: int, shift_y: int):
        self.position[0] += shift_x
        self.position[1] += shift_y
