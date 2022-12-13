from typing import Tuple

class Room:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.x1 = x
        self.y1 = y
        self.x2 = width + x
        self.y2 = height + y
    
    def __contains__(self, other):
        return self.x1 <= other.x2 and self.x2 >= other.x1 and self.y1 <= other.y2 and self.y2 >= other.y1
    
    def get_inner_space(self) -> Tuple[slice, slice]:
        return slice(self.x1 + 1, self.y1), slice(self.x2 + 1, self.y2)
    
    def get_center(self) -> Tuple[int, int]:
        return (
            int((self.x1 + self.x2) / 2),
            int((self.y1 + self.y2) / 2)
        )