from typing import List, Tuple

class BaseAI():

    def perform(self):
        raise NotImplementedError()
    
    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        pass
