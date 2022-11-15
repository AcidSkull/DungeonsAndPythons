extends Character

signal fired_bullet(bullet, position, direction)

var inventory = load("res://Characters/Player/Inventory.gd").new()
var velocity = Vector2()

onready var UI = $UserInterface
onready var EndOfGun = $EndOfGun
onready var GunDirection = $GunDirection
onready var GunCooldown = $GunCooldown

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
	if GunCooldown.is_stopped():
		var bullet_instance = Bullet.instance()
		var direction = (GunDirection.global_position - EndOfGun.global_position).normalized()
		emit_signal("fired_bullet", bullet_instance, EndOfGun.global_position, direction)
		GunCooldown.start()
		Animation.play("muzzle_flash")
	
