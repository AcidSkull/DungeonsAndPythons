from typing import List, Tuple
from queue import PriorityQueue
from settings import *

class BaseAI():

    def perform(self):
        raise NotImplementedError()
    
    def _distance(self, x1: int, y1: int, x2: int, y2: int): return abs(x1 - x2) + abs(y1 - y2)

    def _get_neighbors(self, x: int, y: int):
        return ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
    
    def get_path_to(self, start_x: int, start_y: int, dest_x: int, dest_y: int, tiles):
        count = 0
        queue = PriorityQueue()
        queue.put((0, count, start_x, start_y))
        came_from = {}
        g_score = [[0 for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        g_score[start_x][start_y] = 0
        f_score = [[0 for y in range(MAP_HEIGHT)] for x in range(MAP_WIDTH)]
        f_score[start_x][start_y] = self._distance(start_x, start_y, dest_x, dest_y) 

        open_set_hash = {(start_x, start_y)}

        while not queue.empty():
            queue_element = queue.get()
            current = (queue_element[2], queue_element[3])
            open_set_hash.remove((queue_element[2], queue_element[3]))

            if current == (dest_x, dest_y):
                return queue
            
            neighbors = self._get_neighbors(current[0], current[1])

            for neighbor in neighbors:
                temp_g_score = g_score[current[0]][current[1]] + 1

                if temp_g_score < g_score[neighbor[0]][neighbor[1]]:
                    came_from[{neighbor[0], neighbor[1]}] = current
                    g_score[neighbor[0]][neighbor[1]] = temp_g_score
                    f_score[neighbor[0]][neighbor[1]] = temp_g_score + self._distance(neighbor[0], neighbor[1], dest_x, dest_y)

                    if {neighbor[0], neighbor[1]} in open_set_hash:
                        count += 1
                        queue.put((f_score[neighbor[0]][neighbor[1]], count, neighbor[0], neighbor[1]))
                        open_set_hash.add((neighbor[0], neighbor[1]))
        

        return None