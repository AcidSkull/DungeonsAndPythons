extends Character

var direction = Vector2.ZERO
var inventory = load("res://Characters/Player/Inventory.gd").new()

onready var UI = $UserInterface
onready var InventoryPanel = $InventoryPanel

# Signals to update user interface
signal update_move(x)
signal update_action(x)
signal update_bonus_action(x)

func _ready() -> void:
	# Connectiong player to user interface
	var _tmp = connect("update_move", UI, "_update_moves_left")
	_tmp = connect("update_action", UI, "_update_action")
	_tmp = connect("update_bonus_action", UI, "_update_bonus_action")
	
	inventory.add_item("Bone", 5)
	
	InventoryPanel.hide()
	
	# Updating user interface
	emit_signal("update_move", moves_left)

func _process(_delta: float) -> void:
	if Input.is_action_just_pressed("end_turn"):
		emit_signal("end_turn")
	# Open inventory
	if Input.is_action_just_pressed("inventory"):
		if InventoryPanel.visible:
			InventoryPanel.hide()
		else:
			InventoryPanel.show()
		inventory.print_inventory()
	
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

