extends Node2D

func bullet_handling(bullet: Bullet, position: Vector2, direction: Vector2) -> void:
	add_child(bullet)
	bullet.global_position = position
	bullet.set_direction(direction)
