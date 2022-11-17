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
onready var weapon: Weapon = null
var actor: Enemy = null

func _process(_delta: float) -> void:
	match state:
		States.IDLE:
			pass
		States.HOSTILE:
			if player != null and weapon != null:
				var angle = actor.global_position.direction_to(player.global_position).angle()
				actor.rotation = lerp(actor.rotation, angle, 0.1)
				
				if abs(actor.rotation - angle) < 0.1:
					weapon.shoot()

func initialize(character: Enemy, new_weapon: Weapon) -> void:
	actor = character
	weapon = new_weapon
	var _tmp = weapon.connect("out_of_ammo", self, "_on_ammo_run_out")

func set_state(new_state: int) -> void:
	if new_state == state: return
	
	state = new_state
	emit_signal("state_change", state)

func _on_DetectionZone_body_entered(body: Node) -> void:
	if body.is_in_group("player"):
		set_state(States.HOSTILE)
		player = body

func _on_ammo_run_out() -> void:
	weapon.reload()
