from Mechanics.Action import Action
from EntityComponents.Component import Component
from typing import List, Tuple
import numpy as np

class BaseAI(Action, Component):
    def perform(self):
        raise NotImplementedError()
    
    def get_path_to(self, dest_x: int, dest_y: int) -> List[Tuple[int, int]]:
        pass
