extends KinematicBody2D
class_name Character

onready var Animation = $AnimationPlayer

export (int) var MAX_HEALTH = 100

var health: int = MAX_HEALTH

var stats = {
	"streangth": 0,
	"dexterity": 0,
	"constitutuion": 0,
	"wisdom": 0,
	"charisma": 0,
	"armor": 0,
}

func _change_health(value: int, damage: bool) -> void:
	if damage:
		health = clamp(health - value, 0, MAX_HEALTH)
	else:
		health = clamp(health + value, 0, MAX_HEALTH)
	if health <= 0:
		kill()

func handle_hit() -> void:
	_change_health(25, true)
	print(health)

func kill() -> void:
	queue_free()
