# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import parseCategory
import parseItem

# To-do list:
# 1. Reorganize so some "main" function is sending a list of acceptable values instead of hard coding
# 2. Cull some unused / experimental functions
# 3. Study how to put some of these extraneous functions into a different file


# This is just a test function to show off an example room.
# **** this should NOT be here in a final copy ****
# Note to self: when removing this, also correct main() and getInput(), executeCommand()
class TestRoom(object):
	def __init__(self):
		self.descLong = "The captain's quarters turn out to be a well-furnished bedroom with shelves filled with books and a fireplace.  The wood-paneled walls are lined with maps and navigational charts.  A recliner near the fireplace looks quite worn and inviting, as if someone had sat there reading often.  There is also a desk on one side of the room, which has some papers scattered across it.  There is a door leading back outside, a door on the left that is locked, and a door on the right which leads to the bathroom."
		self.descShort = "The captain's quarters are a well-furnished bedroom with a filled bookshelf and a fireplace.  There is a recliner near the fireplace, as well as a desk to one side of the room.  One door leads outside, another leads to a bathroom, and the last door appears to be locked."
		self.roomID = -01
		self.features = ['bookshelf', 'recliner', 'fireplace', 'desk', 'doorBathroom', 'bed', 'door']
		self.items = ['key']
		self.challengeFlag = False
	def getRoomThings(self):
		return self.items + self.features
	def getItems(self):
		return self.items
	def getFeatures(self):
		return self.features
	def printDescLong(self):
		print self.descLong
	def printDescShort(self):
		print self.descShort


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
def executeCommand(wordArray, category, item, roomTemp):
	if (category == "savegame"):
		# saveGame()
		print "Game would be saved here."
	elif (category == "loadgame"):
		# loadGame()
		print "Game would be loaded here."
		# not sure how this should be handled - maybe destroy this instance? so return False?
	elif (category == "inventory"):
		# showInventory()
		print "This is your imaginary inventory: (print list of items)"
	elif (category == "look"):
		# look(current roomID)
		#print "You look around and see things.... (list objects / long description)"
		print "You look around and see... (full description)"
		roomTemp.printDescLong()
	elif (category == "look_at"):
		# identifyItemNumber(item) - turn word into an item ID
		# lookAt(itemID)
		# check if item is unspecified / undefined and give error message accordingly.
		# Maybe this should be handled in another function.
		if (wordArray[0] == item):
			print "Look at what?  (Please specify an item to look at)"
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
		print roomTemp.getRoomThings()
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
def getInput(tempCounter):
	# Example room only:
	captroom = TestRoom()
	listOfItems = captroom.getRoomThings()
	if (tempCounter == 0):
		captroom.printDescLong()
	else:
		captroom.printDescShort()
	print '\n'

	lineInput = raw_input('Your action: ')
	# Split sentence into its component words
	wordArray = lineInput.split(" ")
	command = wordArray[0]
	# Probably need to insert a check if a valid object is specified, or how to handle missing prepositions
	# For that matter, determine where the item is going to be in a sentence (wordArray[1] or wordArray[2])
	# maybe keep a list of items in the room, loop and check each word, then return a contextual response?
	#listOfItems = ['key', 'door', 'plant', 'bird', 'plane', 'superman']
	
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
		executeCommand(wordArray, category, item, captroom)
	return True


# Update to run main function for parseCommands.py separately from main.py
def main():
	keepLooping = True
	# tempCounter is only used with the example room to simulate a first visit to a room.
	# This shouldn't be in here permanently, and getInput should work without a parameter.
	tempCounter = 0
	while (keepLooping):
		keepLooping = getInput(tempCounter)
		tempCounter+= 1

if __name__ == "__main__":
   print 'Starting the script.'
   main() 
