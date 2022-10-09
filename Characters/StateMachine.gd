extends Node
class_name StateMachine

var state = null
var previous_state = null
var states = {}

onready var parent = get_parent()
onready var animation = parent.get_node("AnimationPlayer")

func _physics_process(delta: float) -> void:
	if state != -1:
		_state_logic(delta)
		var transition = _get_transition(delta)
		
		if transition != -1:
			set_state(transition)

func _state_logic(delta: float) -> void:
	pass

func _get_transition(delta: float) -> int:
	return -1

func _enter_state(new_state, old_state) -> void:
	pass

func _exit_state(old_state, new_state) -> void:
	pass

func set_state(new_state) -> void:
	previous_state = state
	state = new_state
	
	if previous_state != -1:
		_exit_state(previous_state, new_state)
	
	if new_state != -1:
		_enter_state(new_state, previous_state)

func add_state(state_name) -> void:
	states[state_name] = states.size()
