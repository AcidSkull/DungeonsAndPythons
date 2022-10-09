extends character

func _process(_delta: float) -> void:
	var mouse = (get_global_mouse_position() - global_position).normalized()
	
	if mouse.x > 0 and sprite.flip_h:
		sprite.flip_h = false
	elif mouse.x < 0 and not sprite.flip_h:
		sprite.flip_h = true

func get_input() -> void:
	direction = Vector2.ZERO
	if Input.is_action_pressed("Down"):
		direction.y = 1
	if Input.is_action_pressed("Up"):
		direction.y = -1
	if Input.is_action_pressed("Left"):
		direction.x = -1
	if Input.is_action_pressed("Right"):
		direction.x = 1
