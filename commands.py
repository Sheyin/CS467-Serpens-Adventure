import utils
import items
import random
from utils import display
# Separates all the command related functions - for parsing

# This has been narrowed down since there is another check for verbs based
# on the item which will override this one.  This acts more like a failsafe
# or catches the one-word commands.  Move, hit, use aren't really implemented.
synonyms =  {
	'save': 'save', 'savegame': 'save', 
	'load': 'load', 'loadgame': 'load', 'resume': 'load',
	'inventory': 'inventory',
	'quit': 'exit', 'exit': 'exit',
	'help': 'help',
	'look at': 'look at', 'examine': 'look at', 'view': 'look at',
	'explore': 'look_room', 'look around': 'look_room',
	'go': 'go', 'move to': 'go', 'leave': 'go', 'travel': 'go',
	'take': 'take', 'pick up': 'pick up', 'get': 'get',
	'drop': 'drop', 'remove': 'drop',
	'use': 'use', 'open': 'use',
	'move': 'move', 'shift': 'move', 'search': 'move', 
	'pull': 'pull',
	'hit': 'hit', 'kick': 'hit', 'punch': 'hit', 'smack': 'hit', 'slap': 'hit', 'stomp': 'hit', 'step on': 'hit',
	'break': 'break',
	'eat': 'eat', 'bite': 'eat', 'swallow': 'eat', 'put in mouth': 'eat', 'put in your mouth': 'eat', 
	'consume': 'eat', 'nibble': 'eat', 'drink': 'eat', 'sip': 'eat', 'chew': 'eat',
	'escape': 'escape', 'break out': 'escape', '/unstuck': 'escape',
}

# Identifies a command
def identify(input):
	# Support for engine codes being directly entered
	if input.isdigit():
		return input
	commandUsed = compareList(input)

	# One word command - switch to engine code
	# Help should be part of this
	if commandUsed in ['save', 'load', 'exit', 'look_room', 'inventory', 'help']:
		commandUsed = utils.engine_codes_dict[commandUsed]
	return commandUsed


# Helper function to keep look commands working correctly
def compareList(input):
	for command in synonyms.keys():
		if input.startswith(command):
			return synonyms[command]


# Parsing-level commands for when it isn't usable by engine
# item is an item or feature; command is a kick-type command (strings)
# Both should be pre-determined before calling this function.
def kick(command, item):
	# Drop the e if before -ing
	if command[-1] is 'e':
		command = command[:-1]
	display("You " + command + " the " + item + ".")
	# random additional phrase
	phrase = ["It doesn't accomplish much, but it makes you feel better.",
	"Ow.", "That hurt.", "You're sure that it hurts more than you do.",
	"Feel my wrath!", "That'll teach it a lesson.",
	]
	display(random.choice(phrase))


# Parsing-level commands for when it isn't usable by engine
# item is an item or feature; command is a kick-type command (strings)
# Both should be pre-determined before calling this function.
def eat(command, object):
	# Drop the e if before -ing
	if command[-1] is 'e':
		command = command[:-1]
	display("You consider " + command + "ing the " + object + ".")
	# random additional phrase
	phrase = ["Hmm.  This doesn't seem like a good idea.",
	"Well, maybe it has some health benefits...",
	"Hmm.  Crunchy.", "Wait, why would you do that?!",
	"Maybe it's not a good idea to do this while sober.",
	"Well, it's not the worst idea you've ever had...",
	"Yeah, I'll just take a little nibble and... wait, what am I thinking?",
	"You're a bit hungry, but you're not THAT hungry.",
	"Admittedly, this probably wasn't the smartest idea you've ever had.",
	]
	display(random.choice(phrase))


# Pull or shift items or features - but no actual effect.
def pull(command, item, type):
	if "door" in item:
		display("Did you mean 'open the " + item + "'?")
	elif type is "item":
		display("You idly twirl the " + item + " around.")
	else:
		# Drop the e if before -ing
		if command[-1] is 'e':
			command = command[:-1]
		display("What's the point of " + command + "ing the " + item + "?")


# A for-fun parse-level only command.
def escape():
	phrase = ["You escape.  Your quest is over.",
	"You pinch yourself.  Startled, you sit up, and realize the entire ordeal was a dream.",
	"You tap your heels together three times.  There's no place like home... there's no place like home...",
	"You have a brilliant idea.  All you have to do is use your hearthstone and...",
	"Clearly this is where the world magically puts you in a different location so you can go your merry way.",
	"Well, you obtained your licence to Apperate.  Just need to recall The Three D's....",
	"You think you remember how to weave Traveling...",
	"You tap your comm badge.  'Beam me up, Scotty.'",
	]
	display(random.choice(phrase))
	display("Just kidding.  You didn't really think it would be that easy, did you?")
	return


if __name__ == "__main__":
	keepLooping = True
	while keepLooping:
		userInput = raw_input (": ")
		kick('kick', 'ball')
		eat('eat', 'barrel')
		if userInput in ['exit', 'stop', 'quit']:
			keepLooping = False 
		#keepLooping = identify(userInput)
		#print "Code received: " + str(keepLooping)