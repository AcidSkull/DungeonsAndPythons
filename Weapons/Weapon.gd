extends Node2D
class_name Weapon

signal out_of_ammo

export (PackedScene) var Bullet = preload("res://Projectiles/Bullet.tscn")
export (int) var MAX_AMMO = 5
export (int) var ammo_per_shoot = 1

onready var EndOfGun = $EndOfGun
onready var GunDirection = $GunDirection
onready var GunCooldown = $GunCooldown
onready var Animation = get_parent().get_node("AnimationPlayer")

var ammo: int = MAX_AMMO

func _ready() -> void:
	"""
	When another scene inherit from this scene the scene has default magazine size
	instead of it own magazine size and it change after reloading to the correct size
	"""
	reload()

func shoot() -> void:
	if ammo > 0 and GunCooldown.is_stopped() and Bullet != null:
		var bullet_instance = Bullet.instance()
		var direction = (GunDirection.global_position - EndOfGun.global_position).normalized()
		GlobalSignals.emit_signal("bullet_fired", bullet_instance, EndOfGun.global_position, direction)
		
		GunCooldown.start()
		Animation.play("muzzle_flash")
		
		ammo -= ammo_per_shoot
		if ammo <= 0:
			emit_signal("out_of_ammo")

func reload() -> void:
#	Animation.play("reload")
	ammo = MAX_AMMO
