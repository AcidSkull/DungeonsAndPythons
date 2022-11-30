
class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.DL_TOP = x
        self.UL_TOP = y
        self.DR_TOP = width + x
        self.UR_TOP = height + y
    
    def __contains__(self, other):
        return self.DL_TOP <= other.DR_TOP and self.DR_TOP >= other.DL_TOP and self.UL_TOP <= other.UR_TOP and self.UR_TOP >= other.UL_TOP
    
    def get_center(self):
        return (
            int((self.DL_TOP + self.DR_TOP) / 2),
            int((self.UL_TOP + self.UR_TOP) / 2)
        )