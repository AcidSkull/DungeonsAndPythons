extends Character

var direction = Vector2.ZERO

onready var UI = $UserInterface

# Signals to update user interface
signal update_move(x)
signal update_action(x)
signal update_bonus_action(x)

func _ready() -> void:
	# Connectiong player to user interface
	var _tmp = connect("update_move", UI, "_update_moves_left")
	_tmp = connect("update_action", UI, "_update_action")
	_tmp = connect("update_bonus_action", UI, "_update_bonus_action")
	
	# Updating user interface
	emit_signal("update_move", moves_left)

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	
	# Detecting movment
	if Input.is_action_just_released("ui_up"):
		move(Vector2.UP)
	elif Input.is_action_just_released("ui_down"):
		move(Vector2.DOWN)
	elif Input.is_action_just_released("ui_left"):
		move(Vector2.LEFT)
	elif Input.is_action_just_released("ui_right"):
		move(Vector2.RIGHT)

func move(dir: Vector2) -> void:
	.move(dir)
	emit_signal("update_move", moves_left)

