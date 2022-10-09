extends KinematicBody2D
class_name character

const FRICTION: float = 0.15

var velocity: Vector2 = Vector2.ZERO
var direction: Vector2 = Vector2.ZERO

export (int) var accerelation: int = 40
export (int) var max_speed: int = 100

onready var sprite = get_node("Sprite")

func _physics_process(_delta: float) -> void:
	velocity = move_and_slide(velocity)
	velocity = lerp(velocity, Vector2.UP, FRICTION)

func move() -> void:
	direction = direction.normalized()
	velocity += direction * accerelation
	velocity = velocity.clamped(max_speed)
