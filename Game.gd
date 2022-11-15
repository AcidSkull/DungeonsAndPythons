extends Node2D

onready var player = $Player
onready var projectiles_manager = $ProjectilesManager

func _ready() -> void:
	player.connect("fired_bullet", projectiles_manager, "bullet_handling")
