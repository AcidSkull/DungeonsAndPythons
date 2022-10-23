extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()

func _process(delta: float) -> void:
	_get_direction()


func _get_direction() -> void:
	if Input.is_action_pressed("ui_up"):
		direction.y = -1
	elif Input.is_action_pressed("ui_down"):
		direction.y = 1
	elif Input.is_action_pressed("ui_right"):
		direction.x = 1
	elif Input.is_action_pressed("ui_left"):
		direction.x = -1
		
	if direction != Vector2.ZERO:
		global_position += direction * 32
	direction = Vector2.ZERO
