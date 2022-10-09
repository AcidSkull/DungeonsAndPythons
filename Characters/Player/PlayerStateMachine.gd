extends StateMachine

func _state_logic(delta: float):
	add_state("idle")
	add_state("walk")

func _get_transition(delta: float):
	return null

func _enter_state(new_state, old_state):
	pass

func _exit_state(old_state, new_state):
	pass
