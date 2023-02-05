from EntityComponents.Actor import Actor

class Item:
    def __init__(self, name: str):
        self.name = name
    
    def use(self, actor: Actor):
        raise NotImplementedError()

class Sword(Item):
    def __init__(self):
        super().__init__("Sword")
    
    def use(self, actor: Actor):
        if actor.name == "Player":
            actor.fighter.power += 1 

class Shield(Item):
    def __init__(self):
        super().__init__("Shield")
    
    def use(self, actor: Actor):
        if actor.name == "Player":
            actor.fighter.defense += 1

class HealthPotion(Item):
    def __init__(self):
        super().__init__("HealthPotion")
    
    def use(self, actor: Actor):
        if actor.name == "Player":
            actor.fighter.hp += 5