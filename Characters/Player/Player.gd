extends Character

var inventory = load("res://Characters/Player/Inventory.gd").new()
var velocity = Vector2()

onready var UI = $UserInterface
onready var InventoryPanel = $InventoryPanel

export (int) var speed = 200

func _ready() -> void:
	
	inventory.add_item("Sword", 1)
	inventory.add_item("Sword", 1)
	inventory.add_item("Shield", 1)
	inventory.add_item("Key", 1)
	
	InventoryPanel.hide()
	

func _physics_process(_delta: float) -> void:
	# Open inventory
	if Input.is_action_just_pressed("inventory"):
		inventory.add_item("Bone", 5)
		if InventoryPanel.visible:
			InventoryPanel.hide()
		else:
			InventoryPanel.show()
	
	get_input()
	velocity = move_and_slide(velocity)
	
# Detecting movment
func get_input() -> void:
	velocity = Vector2()
	if Input.is_action_pressed("ui_up"):
		velocity.y -= 1
	if Input.is_action_pressed("ui_down"):
		velocity.y += 1
	if Input.is_action_pressed("ui_left"):
		velocity.x -= 1
	if Input.is_action_pressed("ui_right"):
		velocity.x += 1
	velocity = velocity.normalized() * speed


