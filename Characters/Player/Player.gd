extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	
	if Input.is_action_just_released("ui_up"):
		move("ui_up")
	elif Input.is_action_just_released("ui_down"):
		move("ui_down")
	elif Input.is_action_just_released("ui_left"):
		move("ui_left")
	elif Input.is_action_just_released("ui_right"):
		move("ui_right")

