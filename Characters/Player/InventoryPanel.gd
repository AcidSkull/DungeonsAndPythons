extends CanvasLayer

onready var backpack = $Backpack/GridContainer

func update_inventory(items):
	if items.size() < 0: return
	
	var i = 0
	
	# Filing inventory
	for slot in backpack.get_children():
		if i < items.size():
			slot.get_child(0).texture = load(items[i].get("item_reference").texture.resource_path)
		else: 
			slot.get_child(0).texture = null
			
		i += 1
