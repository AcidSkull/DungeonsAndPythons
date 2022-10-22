extends Character

var direction = Vector2.ZERO
onready var Game = get_parent()

signal move(direction)

func _ready():
	var tmp = connect("move", Game, "_on_player_move")

func _process(delta: float) -> void:
	_get_direction()


func _get_direction() -> void:
	print(1)
	if Input.is_action_pressed("ui_up"):
		direction.y = -1
	elif Input.is_action_pressed("ui_down"):
		direction.y = 1
	elif Input.is_action_pressed("ui_right"):
		direction.x = 1
	elif Input.is_action_pressed("ui_left"):
		direction.x = -1
		
	if direction != Vector2.ZERO:
		emit_signal("move", direction)
	direction = Vector2.ZERO
