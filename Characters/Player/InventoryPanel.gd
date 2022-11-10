extends CanvasLayer

onready var backpack = $Backpack/GridContainer

signal use_item(index)

func _ready():
	var _tmp
	for slot in $Backpack/GridContainer.get_children():
		_tmp = slot.connect("gui_input", self, "_use_item")

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

func _use_item(event: InputEvent):
	if event is InputEventMouseButton and event.doubleclick:
#		emit_signal("use_item", )
		print("YOS")
