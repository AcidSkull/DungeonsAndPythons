extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	
	if Input.is_action_just_released("ui_up"):
		emit_signal("move", "ui_up")
	elif Input.is_action_just_released("ui_down"):
		emit_signal("move", "ui_down")
	elif Input.is_action_just_released("ui_left"):
		emit_signal("move", "ui_left")
	elif Input.is_action_just_released("ui_right"):
		emit_signal("move", "ui_right")

