extends Character

var inventory = load("res://Characters/Player/Inventory.gd").new()
var velocity = Vector2()

onready var UI = $UserInterface
onready var Pointer = $Pointer

export (int) var speed = 200
export (PackedScene) var Bullet = preload("res://Projectiles/Bullet.tscn")

func _ready() -> void:
	
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
		shoot()
	
func shoot() -> void:
	# Craeting bullet
	var bullet_instance = Bullet.instance()
	add_child(bullet_instance)
	bullet_instance.global_position = Pointer.global_position
	
	var direction_to_mouse = bullet_instance.global_position.direction_to(get_global_mouse_position()).normalized()
	bullet_instance.set_direction(direction_to_mouse)
