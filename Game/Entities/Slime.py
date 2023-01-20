from EntityComponents.Actor import Actor
from EntityComponents.Fighter import Fighter
from EntityComponents.AI import BaseAI
from typing import Type

class Slime(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(x, y, "Slime", BaseAI(), Fighter(10, 5, 2))