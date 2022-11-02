extends KinematicBody2D
class_name Character

onready var raycast = $RayCast2D

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

func _ready() -> void:
	var _tmp = connect("move", get_tree().root.get_node("Game"), "move_character")

func check_if_turn_is_over() -> void:
	if moves_left > 0 and action == false and bonus_action == false:
		emit_signal("end_turn")

func move(dir: Vector2) -> void:
	raycast.cast_to = dir * 32
	raycast.force_raycast_update()
	if raycast.is_colliding(): return
	
	if moves_left > 0:
		emit_signal("move", dir)
#		moves_left -= 1
	else:
		check_if_turn_is_over()
