from Mechanics.Camera import Camera
from EntityComponents.Fighter import Fighter
from EntityComponents.Actor import Actor

class Player(Actor):
    def __init__(self, x: int, y: int, camera: Camera):
        super().__init__(x, y, "Player", None,Fighter(35, 3, 3))
        self.visible = True
        self.camera = camera
        self.is_alive = True
        self.enemy_group = 1
        self.win = False
    
    def move(self, dx: int, dy: int):
        self.camera.follow(dx, dy)
        return super().move(dx, dy)
    