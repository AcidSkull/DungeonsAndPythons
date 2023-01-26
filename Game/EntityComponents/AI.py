from typing import List, Tuple
from queue import PriorityQueue
from settings import *

class BaseAI():

    def perform(self):
        raise NotImplementedError()
    
    def _distance(x1: int, y1: int, x2: int, y2: int): return abs(x1 - x2) + abs(y1 - y2)
    
    def get_path_to(self, start_x: int, start_y: int, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, start_x, start_y))
        came_from = {}
        g_score = {[x for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)}
        g_score[start_x][start_y] = 0
        f_score = {[x for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)}
        f_score[start_x][start_y] = self._distance(start_x, start_y, dest_x, dest_y) 

        open_set_hash = {{start_x, start_y}}

        # while not queue.empty():
            