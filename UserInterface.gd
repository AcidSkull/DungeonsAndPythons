extends CanvasLayer

onready var moves = $HBoxContainer/Moves/Label
onready var action = $HBoxContainer/Action/Label
onready var bonus_action = $HBoxContainer/BonusAction/Label

func _update_moves_left(x: int) -> void:
	moves.text = str(x)

func _update_action(x: bool) -> void:
	action.text = "1" if x else "0"

func _update_bonus_action(x: bool) -> void:
	bonus_action.text = "1" if x else "0"
