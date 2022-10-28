extends Resource
class_name Item

export var name : String
export var stackable : bool = false
export var max_stack : int = 1

enum item_type {GENERIC, CONSUMABLE, EQUIPMENT}
export(item_type) var type
export var texture : Texture
