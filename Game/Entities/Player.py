from Entities.Entity import Entity
from Mechanics.Camera import Camera

class Player(Entity):
    def __init__(self, x: int, y: int, camera: Camera):
        super().__init__(x, y, "Player")
        self.visible = True
        self.camera = camera