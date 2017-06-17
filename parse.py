import items
import commands
import utils
import data
from data import *
from utils import display
import story

# This is the starting point for all the parsing-related functions. (Cheryl)
# commands.py - command-specific parsing (identifying, synonyms, etc)
# items.py - item-specific parsing (identifying items and features)
# utils.py - Misc. (movement/dir, engine code dictionary, help, print text)
# story.py - Story-specific things (conclusion, cryptex puzzle)
# checksaveload.py - Helper functions for selecting a save/load game

# Prints out the available actions for a specified feature
# This will probably be integrated into the engine or something
def getActions(feature, featureDict):
	actions = featureDict[feature]
	actionsList = actions.split(", ")
	return actionsList

# Check if the command was one specific to operating upon a feature (listed in json)
def checkFeatureActions(input, pos, feature, featureDict):		
	actionsList = getActions(feature, featureDict)

	# Check list of specified actions for a given feature
	for verb in actionsList:
		if verb in input:
			key = "feat" + str(pos) + "_do"
			return utils.engine_codes_dict[key]


# This receives input from engine/engineTest, validates and returns an engine code
# This expects: input(string), features(List), feature(Dict), items(Dict), rooms(List of tuples)
def main(rawinput, features, featureDict, itemDict, rooms, currentRoom):
	input = rawinput.lower()
	command = commands.identify(input)
	itemList = itemDict.keys()
	splitString = input.split()

	if splitString:
		rawCommand = splitString[0]
	else:
		rawCommand = "null"

	if rawCommand is "null":
		return "invalid"

	elif command in ['exit', 'inventory', 'save', 'load', 'help']:
		return utils.engine_codes_dict[command]

	elif command == "go":
		# This will identify a direction or a feature, if found
		# Currently redundant because feature synonyms are included in directions list
		# location = items.findLocation(input, features)
		direction = utils.translateRoom(input, rooms)

		if (direction == -1):
			# Special exit
			if currentRoom == 15 and ("hatch" in input):
					if story.endingPrompt():
						return utils.engine_codes_dict['endgame']
					else:
						return "invalid"
			else:
				display("I can't go that way.")
		# Prevent "go door" in room 6 leading downstairs
		elif currentRoom == 6:
			feature = items.identifyFeature(input, features)
			if feature in ["trap door", "wooden door"]:
				key = "go_" + str(direction)
				return utils.engine_codes_dict[key]
			elif "door" in input:
				display("Which door, wooden or trap?")
				return "invalid"
			else:
				key = "go_" + str(direction)
				return utils.engine_codes_dict[key]
		else:
			key = "go_" + str(direction)
			return utils.engine_codes_dict[key]

	elif command in ["take", "drop"]:
		item = items.identifyItem(input, itemDict)

		if item:
			if command == "take":
				key = item + "_take"
				return utils.engine_codes_dict[key]
			if command == "drop":
				key = item + "_drop"
				return utils.engine_codes_dict[key]
		else:
			# Not one of the items	
			display("I can't do that.")

	elif command == "look at":
		item = items.identifyItem(input, itemDict)
		if item:
			key = item + "_look"
			return utils.engine_codes_dict[key]
		else:
			feature = items.identifyFeature(input, features)
			if feature:
				pos = features.index(feature) + 1
				commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)
				# This is an override if examine is used as an interaction rather than look
				if commandUsedSpecified:
					key = "feat" + str(pos) + "_do"
				else: 
					key = "feat" + str(pos) + "_look"
				return utils.engine_codes_dict[key]
			else:
				display("I can't do that.")

	# Strictly a for-fun command.  Not sure what parameters are really needed yet.
	elif command == "escape":
		if currentRoom == 15 and "hatch" in input:
			for escapeWord in ['escape through', 'escape by', 'escape in']:
				if escapeWord in input:
					if story.endingPrompt():
						return utils.engine_codes_dict['endgame']
			else:
				display("That's an odd thing to do with the hatch.")
				return "invalid"
		else:
			commands.escape()

	# Had to remove "look" from commands.synonyms because it was causing problems - prioritization
	elif "look" in input:
		return utils.engine_codes_dict["look_room"]

	else:
		feature = items.identifyFeature(input, features)
		item = items.identifyItem(input, itemDict)

		# Check if the command was one specific to operating upon a feature (listed in json)
		if feature:
			pos = features.index(feature) + 1
			commandUsedSpecified = checkFeatureActions(input, pos, feature, featureDict)

			# Recognized command on a feature.  May want this to be highest priority.
			if commandUsedSpecified:
				return commandUsedSpecified

			# Special exit
			elif currentRoom == 15 and feature == "hatch":
				for escapeWord in ['climb in', 'climb through', 'enter', 'escape through']:
					if escapeWord in input:
						if story.endingPrompt():
							return utils.engine_codes_dict['endgame']
				else:
					return "invalid"

			# Some item and feature both mentioned in same sentence with a legal action.
			elif item == 'board' and feature in ['window', 'locker'] and (command in ['move', 'use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'keys' and feature in ['door', 'chest'] and (command in ['use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'handle' and feature in ['metal door'] and (command in ['use'] or commandUsedSpecified or "attach" in input or "affix" in input or "stick" in input):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif item == 'skeleton key' and feature in ['trap door', 'trapdoor'] and (command in ['use'] or commandUsedSpecified):
				key = "feat" + str(pos) + "_do"
				return utils.engine_codes_dict[key]

			elif (currentRoom == 12) and ("key" in input) and (feature == "office door") and (command in ['use'] or commandUsedSpecified):
				if item == 'skeleton key':
					key = "feat" + str(pos) + "_do"
					return utils.engine_codes_dict[key]
				else:
					display("The key doesn't fit.  Maybe a different one will work.")
					return "invalid"

			elif (currentRoom == 7) and ("key" in input) and (feature == "case") and (command in ['use'] or commandUsedSpecified):
				if item == 'small key':
					key = "feat" + str(pos) + "_do"
					return utils.engine_codes_dict[key]
				else:
					display("The key doesn't fit.  Maybe a different one will work.")
					return "invalid"

			elif command == 'eat':
				commands.eat(rawCommand, feature)

			# Kicking a recognized feature
			elif command == 'hit':
				if currentRoom == 13 and ("board" in input) and (feature == "glass case"):
					return "4"
				else:
					commands.kick(rawCommand, feature)

			elif command == 'move':
				commands.pull(rawCommand, feature, "feature")

			# Unrecognized combination of item, feature, command - not sure when this will be used
			elif command and feature and item:
				display("I'm not sure if I can " + command + " the " + item + " on the " + feature + ".")

			# Feature mentioned, no item; no legal action from json
			else:
				# This is for the go requirement - if you specify "metal door" only act as go
				direction = utils.translateRoom(input, rooms, "strict")
				# Not a valid room alias
				if (direction == -1):
					if feature in ['chest', 'door'] and rawCommand in ['open', 'unlock']:
						display("I can't open that.  Maybe a key is required?")
					else:
						display("I don't think I can do that to the " + feature + ".")
				# Identical to "go"
				else:
					key = "go_" + str(direction)
					return utils.engine_codes_dict[key]

		# Item but no feature
		elif item and not feature:
			# Catch the silly commands first
			if command == "eat":
				commands.eat(rawCommand, item)
			elif command == "hit":
				commands.kick(rawCommand, item)
			elif command == "move":
				if "door" in input:
					display ("Open a door?  Which door?")
				else:
					commands.pull(rawCommand, item, "item")
			elif item == "board":
				# For "use board on keys"
				if "keys" in input and command in ['use', 'move']:
					return "7"

				# Default - "pull board"
				elif command in ['move', 'pull']:
					return "4"
				
				# Some default return
				else:
					display("What do you want to do with this " + item + "?")
					return "invalid"
			elif item == 'keys' and command in ['use']:
				# "Use board on keys" - shouldn't really be needed, just in case
				if "board" in input:
					return "7"
				# "Use keys on lock"
				if 'lock' in input:
					return "10"
				else:
					display("What do you want to do with this " + item + "?")
					return "invalid"
			# Test the following interactions
			elif item == 'gun' and rawCommand in ['use', 'fire', 'shoot']:
				return utils.engine_codes_dict['gun_use']
			elif item == 'paper clip' and rawCommand in ['bend', 'twist', 'change', 'turn']:
				return utils.engine_codes_dict['paper clip_bend']
			elif item == 'cryptex' and rawCommand in ['open', 'unlock', 'twist', 'turn']:
				return utils.engine_codes_dict['cryptex_open']
			else:
				# No recognized item and command
				display("I'm not sure how to " + rawCommand + " the " + item + " that way.")

		# No item or feature, unrecognized command
		else:
			if 'pots' in input and (command in ['hit', 'move', 'break']) and (currentRoom == 12):
				return "2"
			else:
				# This is for the go requirement - if you specify "metal door" only act as go
				direction = utils.translateRoom(input, rooms, "strict")
				# Not a valid room alias
				if (direction == -1):
					display("I don't understand.")
				elif currentRoom == 6:
					if "door" in input:
						for doordescription in ['trap', 'wooden']:
							if doordescription in input:
								key = "go_" + str(direction)
								return utils.engine_codes_dict[key]
						# Just a plain 'door' not trap / wooden
						display("Which door, wooden or trap?")
						return "invalid"
					else:
						# Some other term like ladder.  Should be okay.
						key = "go_" + str(direction)
						return utils.engine_codes_dict[key]
				# Identical to "go"
				else:
					key = "go_" + str(direction)
					return utils.engine_codes_dict[key]


# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
	print 'Starting the script.'
	keepLooping = True
	currentRoom = 1
	while (keepLooping != "exit"):
		userInput = raw_input (": ")
		featureList, featureDict, itemDict, roomList = utils.formatRoomData(rooms, objects, currentRoom)
		keepLooping = main(userInput, featureList, featureDict, itemDict, roomList)
		print ("Code received: " + str(keepLooping))

