extends Resource
class_name Inventory

signal inventory_change(items)

export var _items = Array() setget set_items, get_items

var max_size : int = 15

func print_inventory():
	if _items.size() == 0:
		print("Pusto")
		return
	
	for i in range(_items.size()):
		print(_items[i].values()[0].name," ", _items[i].quantity)

func get_items():
	return _items

func get_item(index):
	return _items[index]

func set_items(new_items):
	_items = new_items
	emit_signal("inventory_change", _items)

func check_if_inventory_is_full():
	return true if _items.size() >= max_size else false

func add_item(name, quantity):
	if check_if_inventory_is_full(): return
	# Checking if quantity is not negative
	if quantity <= 0:
		return
	
	var item = ItemManager.get_item(name)
	# If we couldn't find the item
	if not item:
		return
	
	var remaining_quantity = quantity
	var max_stack = item.max_stack if item.stackable else 1
	
	# Adding item to existing inventory slot
	if item.stackable:
		for i in range(_items.size()):
			if check_if_inventory_is_full(): return
			
			if remaining_quantity == 0:
				break
			var inventory_item = _items[i]
			
			# Checking if this is the item we looking for
			if inventory_item.item_reference.name != item.name:
				continue
			
			# Checking if we don't add to many quantity to item
			if inventory_item.quantity < max_stack:
				var original_quantity = inventory_item.quantity
				inventory_item.quantity = min(original_quantity + remaining_quantity, max_stack)
				remaining_quantity -= inventory_item.quantity - original_quantity
	
	# Filling new inventory slots
	while remaining_quantity > 0:
		if check_if_inventory_is_full(): return
		
		var new_item = {
			item_reference = item,
			quantity = min(remaining_quantity, max_stack)
		}
		_items.append(new_item)
		remaining_quantity -= new_item.quantity
	
	emit_signal("inventory_change", _items)
