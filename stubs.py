# These are just stubs to help interface with the engine.
# Helper functions to get proper ID's etc can be called here before making
# the appropriate call to the engine (TBD)
# These are called in parseCommands.executeCommand() wtih exception of quit() (needs fix)

import parseItem
import enginetest

def saveGame():
	print "Game would be saved here."
	return


def loadGame():
	print "Game would be loaded here."
	return


def showInventory():
	print "This is your imaginary inventory: (print list of items)"
	return


# may want to adjust this logic before category is assigned
def look(wordArray, item):
	# in zork, it checks for look (alone) first (only working command)
	# then if there is more than one word, it checks if the following word is "at"
	# if the second word is not "at", then return an error (only understood you as far as wanting to look)
	# if there are only two words "look at" return a specific error (at what?)
	# look(current roomID)
	if (item == "invalid") and (wordArray[1] != "around"):
		parseItem.randomErrorMessage(wordArray, item)
	elif (len(wordArray) == 1) or (wordArray[1] == "around"):
		#print "You look around and see... (full description for the room)"
		enginetest.bottomLevelTest(11)
	elif (len(wordArray) > 1) and (wordArray[1] != "at"):
		print "I only understood you as far as wanting to look."
	else:
		# Handling "look_at" this might be duplication since it's also handled in findCommand()
		lookAt(item)
	return

# An item has been specified (and verified to be look-able) before calling this
# Clean up and merge with look()?
def lookAt(item):
	# identifyItemNumber(item) - turn word into an item ID
	# lookAt(itemID)
	# check if item is unspecified / undefined and give error message accordingly.
	# Maybe this should be handled in another function.
	#if (wordArray[0] == item):
	#	print "Look at what?  (Please specify an item to look at)"
	#elif (item == "invalid"):
	#	print "You're trying to look at an unrecognized item."

	# Hard coding some items as we prepare for integration!
	if (item == "straw"):
		enginetest.bottomLevelTest(1)
	elif (item == "bench"):
		enginetest.bottomLevelTest(3)
	elif (item == "board"):
		enginetest.bottomLevelTest(5)
	elif (item == "window"):
		enginetest.bottomLevelTest(6)
	elif (item == "keys"):
		enginetest.bottomLevelTest(8)
	elif (item == "door"):
		enginetest.bottomLevelTest(9)


	elif (item != "invalid"):
		print "You look at the " + item + "."
	else:
		# item is invalid
		print "Look at what?"
	return


def goTo(room):
	# identifyRoomNumber(direction/room) - turn input into a proper roomID (ex. library -> 01)
	# go(roomID)
	if (room == "invalid"):
		print "You can't go there."
	else:
		print "You go to the " + room + " (place?)."
	return


def take(item):
	# identifyItemNumber(item)
	if (item == "invalid"):
		randomErrorMessage(wordArray, item)
	elif (item == "board"):
		enginetest.bottomLevelTest(12)
	elif (item == "keys"):
		enginetest.bottomLevelTest(13)
	else:
		print "You take the " + item + "."
	return


# This is also a variant of "take" and is a custom command.
# I'm not really sure if it will be used though.  Maybe text-only response?  May not be needed.
def bring(item1, item2):
	print "You take the " + item1 + " to the " + item2 + "."
	return

def help():
	print "These are the items in the room..."
	# This ought to be room-specific and may require calling on a room ID
	return

def drop(item):
	# identifyItemNumber(item)
	if (item == "invalid"):
		print "You don't have that item."
	elif (item == "board"):
		enginetest.bottomLevelTest(14)
	elif (item == "keys"):
		enginetest.bottomLevelTest(15)
	else:
		print "You drop the " + item + "."
	return

def quit():
	print "Exiting the game.  Thanks for playing!"
	return

# Custom command - this will probably need to be fleshed out depending
#	on what kind of objects we come up with.
def use(item1, item2):
	if (item1 == "invalid"):
		print "You don't have this item."
	elif (item1 == "board"):
		if (item2 == "keys"):
			enginetest.bottomLevelTest(7)
		else:
			print "I'm not sure what you want to do with this board."
	elif (item1 == "keys"):
		if (item2 == "door"):
			enginetest.bottomLevelTest(10)
		else:
			print "I'm not sure how you want to use these keys."
	elif (item2 != 'none'):
		print "You use the " + item1 + " on the " + item2 + "."
	else:
		print "You use the " + item1 + "."
	return

def move(item):
	if (item == "invalid"):
		print "You don't see this item."
	elif (item == "straw"):
		enginetest.bottomLevelTest(2)
	elif (item == "board") or (item == "bench"):
		enginetest.bottomLevelTest(4)

def hit(item):
	if (item == "invalid"):
		print "You don't see this item."
	elif (item == "bench"):
		enginetest.bottomLevelTest(4)
	elif (item == "door"):
		print "Ow.  That hurts."
