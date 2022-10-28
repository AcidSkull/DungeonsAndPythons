extends Resource
class_name Inventory

signal inventory_change

export var _items = Array() setget set_items, get_items

func get_items():
	return _items

func set_items(new_items):
	_items = new_items
	emit_signal("inventory_change", self)
