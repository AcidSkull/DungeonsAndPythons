extends Node2D

onready var player = get_node("Player")

var active_characters = []
var i = 0


func _ready() -> void:
	active_characters.append(player)

func move_character(dir) -> void:
	active_characters[i].position += dir * 32
