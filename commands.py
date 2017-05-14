import utils
import items
# Separates all the command related functions - for parsing

# This has been narrowed down since there is another check for verbs based
# on the item which will override this one.  This acts more like a failsafe
# or catches the one-word commands.  Move, hit, use aren't really implemented.
synonyms =  {
	'save': 'save', 'load': 'load',
	'inventory': 'inventory',
	'quit': 'exit', 'exit': 'exit',
	'help': 'help',
	'look at': 'look at', 'examine': 'look at', 'view': 'look at',
	'look': 'look_room', 'explore': 'look_room', 'look around': 'look_room',
	'go': 'go', 'move to': 'go',
	'take': 'take', 'pick up': 'pick up', 'get': 'get',
	'drop': 'drop', 'remove': 'drop',
	'use': 'use', 'open': 'use',
	'move': 'move', 'shift': 'move', 'search': 'move',
	'hit': 'hit', 'kick': 'hit', 'punch': 'hit'
}

# Identifies a command
def identify(input):
	# Support for engine codes being directly entered
	if input.isdigit():
		return input
	commandUsed = compareList(input)

	# One word command - switch to engine code
	# Help should be part of this
	if commandUsed in ['save', 'load', 'exit', 'look_room', 'inventory']:
		commandUsed = utils.engine_codes_dict[commandUsed]
	return commandUsed


# Helper function to keep look commands working correctly
def compareList(input):
	for command in synonyms.keys():
		if input.startswith(command):
			return synonyms[command]


if __name__ == "__main__":
	keepLooping = True
	while (keepLooping != "exit"):
		userInput = raw_input (": ")
		keepLooping = identify(userInput)
		print "Code received: " + str(keepLooping)