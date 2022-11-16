extends Character
class_name Enemy

onready var AI = $AI
onready var Weapon = $Weapon

func _ready() -> void:
	AI.initialize(self, Weapon)
