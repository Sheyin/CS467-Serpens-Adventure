# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import parseCategory
import parseItem
# To-do list:
# 1. Reorganize so some "main" function is sending a list of acceptable values instead of hard coding
# 2. Cull some unused / experimental functions
# 3. Study how to put some of these extraneous functions into a different file





# working off the assumption that the first word used is the command / verb.
# Returns the "category" of the verb if known, otherwise returns "unknown"
def checkCommand(wordArray):
	# Special handling for look vs look at since only command is sent
	# Needs more refinement to make "look at door" and "look door" the same
	if ((len(wordArray) > 1) and ((wordArray[0] == "look") and (wordArray[1] == "at"))):
		category = parseCategory.identify ("look_at")
	else:
		category = parseCategory.identify(wordArray[0])
	return category


# This executes the specified command by calling whichever functions
# The command and item should have been validated before calling this
# _maybe_ can combine with findCategory() but would need to restructure
def executeCommand(wordArray, category, item):
	if (category == "savegame"):
		# saveGame()
		print "Game would be saved here."
	elif (category == "loadgame"):
		# loadGame()
		print "Game would be loaded here."
		# not sure how this should be handled - maybe destroy this instance? so return False?
	elif (category == "inventory"):
		# showInventory()
		print "This is your imaginary inventory!"
	elif (category == "look"):
		# look(current roomID)
		print "You look around and see things.... (list objects / long description)"
	elif (category == "look_at"):
		# identifyItemNumber(item) - turn word into an item ID
		# lookAt(itemID)
		# check if item is unspecified / undefined and give error message accordingly.
		# Maybe this should be handled in another function.
		if (wordArray[0] == item):
			print "Look at what?"
		#elif (item == "invalid"):
		#	print "You're trying to look at an unrecognized item."
		elif (item != "invalid"):
			print "You look at the " + item + "."
	elif (category == "go"):
		# identifyRoomNumber(direction/room) - turn input into a proper roomID (ex. library -> 01)
		# go(roomID)
		print "You go to the " + item + " (place?)."
	elif (category == "take"):
		# identifyItemNumber(item)
		# take(itemID)
		if (item != "invalid"):
			print "You take the " + item + "."
	elif (category == "help"):
		# help(room)
		print "These are the items in the room..."
	elif (category == "drop"):
		# identifyItemNumber(item)
		# drop(item)
		if (item != "invalid"):
			print "You drop the " + item + "."
	elif (category == "quit"):
		# Currently this is never reached because it is also handled in getInput()
		# quit()
		print "Exiting the game."
	else:
		# Some custom handling here - ex. new actions? add more elifs?
		print "You " + wordArray[0] + " the " + item + "."
	return True


# Putting this into a function to mimic what probably happens in overall program.
def getInput():
	lineInput = raw_input('Your action: ')
	# Split sentence into its component words
	wordArray = lineInput.split(" ")
	command = wordArray[0]
	# Probably need to insert a check if a valid object is specified, or how to handle missing prepositions
	# For that matter, determine where the item is going to be in a sentence (wordArray[1] or wordArray[2])
	# maybe keep a list of items in the room, loop and check each word, then return a contextual response?
	listOfItems = ['key', 'door', 'plant', 'bird', 'plane', 'superman']

	# Check if the command used is known / valid
	category = checkCommand(wordArray)
	if (category == "quit"):
		print "Exiting the game.  Thanks for playing!"
		return False
	# Invalid command used.
	elif (category == "unknown"):
		print "You want to " + wordArray[0] + " but you don't know how.  Try a different command."
	else: 
		item = parseItem.findItemUsed(wordArray, listOfItems)
		executeCommand(wordArray, category, item)
	return True


# Update to run main function for parseCommands.py separately from main.py
def main():
	keepLooping = True
	while (keepLooping):
		keepLooping = getInput()

if __name__ == "__main__":
   print 'Starting the script.'
   main() 
