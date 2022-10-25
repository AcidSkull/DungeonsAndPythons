extends Node2D

onready var player = get_node("Player")

var active_characters = []
var i = 0
var directions = {
	"ui_up" : Vector2.UP,
	"ui_down" : Vector2.DOWN,
	"ui_left" : Vector2.LEFT,
	"ui_right" : Vector2.RIGHT
}

func _ready():
	active_characters.append(player)

func move_character(dir):
	active_characters[i].position += directions[dir] * 32
