extends CanvasLayer

onready var moves = $VBoxContainer/Moves/Label
onready var action = $VBoxContainer/Action/Label
onready var bonus_action = $VBoxContainer/BonusAction/Label

func _update_moves_left(x: int):
	moves.text = str(x)

func _update_action(x: bool):
	action.text = "1" if x else "0"

func _update_bonus_action(x: bool):
	bonus_action.text = "1" if x else "0"
