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

func _on_LifeTime_timeout() -> void:
	queue_free()

func _on_Bullet_body_entered(body: Node) -> void:
	if body.has_method("handle_hit"):
		body.handle_hit()
		queue_free()
	elif body.is_in_group("Environment"):
		queue_free()
