extends Character

var direction = Vector2.ZERO

func _process(delta):
	direction = get_direction()
	if direction == Vector2.ZERO:
		return
	

func get_direction():
	if Input.is_action_pressed("ui_up"):
		direction.y = -1
	elif Input.is_action_pressed("ui_down"):
		direction.y = 1
	elif Input.is_action_pressed("ui_right"):
		direction.x = 1
	elif Input.is_action_pressed("ui_left"):
		direction.x = -1
