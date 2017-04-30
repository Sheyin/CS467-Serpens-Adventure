# identify() (formerly checkCategory()): lists related words / synonyms under a category for each
# This returns a string for what "category" the input belongs to
# Need a better way to organize this.  Multiple arrays / dictionary? Needs research.
# May be using a file for each category, with synonyms for each
def identify(command):
	if ((command == "savegame") or (command == "save")):
		return "savegame"
	elif ((command == "loadgame") or (command == "load")):
		return "loadgame"
	elif ((command == "inventory") or (command == "bag")):
		return "inventory"
	elif ((command == "look") or (command == "explore")):
		return "look"
	elif ((command == "look_at") or (command == "examine") or (command == "view")):
		return "look_at"
	elif ((command == "go") or (command == "move_to")):
		return "go"
	elif ((command == "take") or (command == "pick_up")):
		return "take"
	elif (command == "help"):
		return "help"
	elif ((command == "drop") or (command == "remove")):
		return "drop"
	elif ((command == "quit") or (command == "exit")):
		return "quit"
	elif (command == "use"):
		return "use"
	elif ((command == "move") or (command == "grab") or (command == "shift") or (command == "pull") or (command == "push")):
		return "move"
	elif ((command == "hit") or (command == "kick") or (command == "punch") or (command == "break") or (command == "attack")):
		return "hit"
	else:
		return "unknown"