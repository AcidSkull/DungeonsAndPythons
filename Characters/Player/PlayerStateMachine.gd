extends StateMachine

func _ready():
	set_state(states.idle)

func _init() -> void:
	add_state("idle")
	add_state("walk")

func _state_logic(_delta: float) -> void:
	if state == states.idle or state == states.move:
		parent.get_input()
		parent.move()

func _get_transition(delta: float) -> int:
	match states:
		states.idle:
			if parent.velocity.length() > 1:
				return states.walk
		states.walk:
			if parent.velocity.length() < 1:
				return states.idle
	return -1

func _enter_state(new_state, old_state):
	match new_state:
		states.idle:
			animation.play("Idle")
		states.walk:
			animation.play("Walk")

func _exit_state(old_state, new_state):
	pass
