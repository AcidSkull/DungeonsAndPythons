extends Character
class_name Player

signal player_fired(bullet, position, direction)

var inventory = load("res://Characters/Player/Inventory.gd").new()
var velocity = Vector2()

onready var UI = $UserInterface
onready var Weapon = $Weapon

export (int) var speed = 200

func _ready() -> void:
	Weapon.connect("weapon_fired", self, "shoot")
	
	inventory.add_item("Sword", 1)
	inventory.add_item("Sword", 1)
	inventory.add_item("Shield", 1)
	inventory.add_item("Key", 1)
	

func _physics_process(_delta: float) -> void:
	# Movement
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
	velocity = move_and_slide(velocity)
	
	look_at(get_global_mouse_position())
	
	# Shooting
	if Input.is_action_pressed("shoot"):
		Weapon.shoot()
	
func shoot(bullet: Bullet, position: Vector2, direction: Vector2) -> void:
	emit_signal("player_fired", bullet, position, direction)

func kill() -> void:
	pass
