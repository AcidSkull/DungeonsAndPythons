extends KinematicBody2D
class_name Character

signal move(direction)
signal end_turn

func _ready():
	connect("move", get_tree().root.get_child(0), "move_character")

