extends Node2D
class_name Weapon

signal weapon_fired(bullet, position, direction)

export (PackedScene) var Bullet = preload("res://Projectiles/Bullet.tscn")

onready var EndOfGun = $EndOfGun
onready var GunDirection = $GunDirection
onready var GunCooldown = $GunCooldown
onready var Animation = get_parent().get_node("AnimationPlayer")

func shoot() -> void:
	if GunCooldown.is_stopped() and Bullet != null:
		var bullet_instance = Bullet.instance()
		var direction = (GunDirection.global_position - EndOfGun.global_position).normalized()
		emit_signal("weapon_fired", bullet_instance, EndOfGun.global_position, direction)
		GunCooldown.start()
		Animation.play("muzzle_flash")
