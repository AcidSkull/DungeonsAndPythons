from Entities.Entity import Entity
from Mechanics.Camera import Camera
from EntityComponents.Fighter import Fighter

class Player(Entity):
    def __init__(self, x: int, y: int, camera: Camera):
        super().__init__(x, y, "Player")
        self.fighter = Fighter(25, 5, 5)
        self.visible = True
        self.camera = camera
        self.is_alive = True
        self.enemy_group = 1
    
    def move(self, dx: int, dy: int):
        self.camera.follow(dx, dy)
        return super().move(dx, dy)