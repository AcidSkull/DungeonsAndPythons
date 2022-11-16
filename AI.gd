extends Node2D
class_name AI

signal state_change(state)

onready var detection_zone = $DetectionZone

enum States{
	IDLE,
	HOSTILE
}

var state: int = States.IDLE setget set_state
var player: Player = null
var weapon: Weapon = null
var actor: Enemy = null

func _process(_delta: float) -> void:
	match state:
		States.IDLE:
			pass
		States.HOSTILE:
			if player != null and weapon != null:
				actor.rotation = actor.global_position.direction_to(player.global_position).angle()
				weapon.shoot()

func initialize(character: Enemy, new_weapon: Weapon) -> void:
	actor = character
	weapon = new_weapon
	

func set_state(new_state: int) -> void:
	if new_state == state: return
	
	state = new_state
	emit_signal("state_change", state)

func _on_DetectionZone_body_entered(body: Node) -> void:
	if body.is_in_group("player"):
		set_state(States.HOSTILE)
		player = body
