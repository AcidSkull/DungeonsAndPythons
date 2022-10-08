extends KinematicBody2D

var velocity
var speed := 400.0

func _physics_process(_delta: float) -> void:
	velocity = Vector2.ZERO
	# Input
	if Input.is_action_pressed("Left"):
		velocity.x -= 1
	if Input.is_action_pressed("Right"):
		velocity.x += 1
	if Input.is_action_pressed("Up"):
		velocity.y -= 1
	if Input.is_action_pressed("Down"):
		velocity.y += 1
	
	velocity.normalized()
	move_and_slide(velocity * speed)
