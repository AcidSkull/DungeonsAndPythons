extends CanvasLayer

onready var moves = $VBoxContainer/TextureRect/Label

func _update_moves_left(x: int):
	moves.text = str(x)
