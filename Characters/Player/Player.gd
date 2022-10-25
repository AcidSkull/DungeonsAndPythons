extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()
onready var move_lefts_label = $Control/HBoxContainer/Sprite/Label

func _process(delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	
	if Input.is_action_just_released("ui_up"):
		move("ui_up")
		update_moves_lefts()
	elif Input.is_action_just_released("ui_down"):
		move("ui_down")
		update_moves_lefts()
	elif Input.is_action_just_released("ui_left"):
		move("ui_left")
		update_moves_lefts()
	elif Input.is_action_just_released("ui_right"):
		move("ui_right")
		update_moves_lefts()

func update_moves_lefts():
	move_lefts_label.text = str(moves_left)
