extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()
onready var UI = $UserInterface

signal update_move(x)

func _ready():
	connect("update_move", UI, "_update_moves_left")
	emit_signal("update_move", moves_left)

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	
	if Input.is_action_just_released("ui_up"):
		move("ui_up")
		emit_signal("update_move", moves_left)
	elif Input.is_action_just_released("ui_down"):
		move("ui_down")
		emit_signal("update_move", moves_left)
	elif Input.is_action_just_released("ui_left"):
		move("ui_left")
		emit_signal("update_move", moves_left)
	elif Input.is_action_just_released("ui_right"):
		move("ui_right")
		emit_signal("update_move", moves_left)

