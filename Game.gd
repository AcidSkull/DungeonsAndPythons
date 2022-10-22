extends Node2D

onready var player = get_node("Player")

func _on_player_move(direction: Vector2):
	player.global_position += (direction * 32)
