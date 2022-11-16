extends Node2D

onready var player: Player = $Player
onready var projectiles_manager = $ProjectilesManager

func _ready() -> void:
	var _tmp = GlobalSignals.connect("bullet_fired", projectiles_manager, "bullet_handling")
