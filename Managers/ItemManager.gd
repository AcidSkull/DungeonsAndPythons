extends Node

var items = Array()

func _ready():
	# Loading items
	var directory = Directory.new()
	directory.open("res://Items")
	directory.list_dir_begin()
	
	var file = directory.get_next()
	while(file):
		if not directory.current_is_dir():
			items.append(load("res://Items/%s" % file))
			
		file = directory.get_next()

func get_item(name):
	for i in items:
		if i.name == name:
			return i
	return null
