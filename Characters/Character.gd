extends KinematicBody2D
class_name Character

signal move(direction)
signal end_turn

var stats = {
	"streangth": 0,
	"dexterity": 0,
	"constitutuion": 0,
	"wisdom": 0,
	"charisma": 0,
	"armor": 0,
}
var moves_left = 3
var action = true
var bonus_action = true

func _ready():
	connect("move", get_tree().root.get_child(0), "move_character")

func check_if_turn_is_over():
	if moves_left > 0 and action == false and bonus_action == false:
		emit_signal("end_turn")

func move(direction: String):	
	if moves_left > 0:
		emit_signal("move", direction)
		--moves_left
	else:
		check_if_turn_is_over()
