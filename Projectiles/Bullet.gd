extends Area2D
class_name Bullet

export (int) var speed = 5

var direction = Vector2.ZERO

func _physics_process(_delta: float):
	if direction != Vector2.ZERO:
		var velocity = direction * speed
		global_position += velocity

func set_direction(dir: Vector2):
	self.direction = dir
	rotation += direction.angle()

func _on_LifeTime_timeout():
	queue_free()
