# This will parse a string input from the command line and call a corresponding function.
# Also has some random bits as I try to figure out how to use Python.

import parseCategory
import parseItem
import parseArticles
import parsePreposition
import stubs

# Cheryl's To-do list:
# 1. Reorganize so some "main" function is sending a list of acceptable values instead of hard coding
# 2. Tidy up process so it isn't trying to parse things that won't be found (ex. single word input)
# 3. Consider renaming .py files to be more in line with rest of group - requires editing main.py
# 4. Coordinate with Karen to begin integrating stubs with actual engine
# 5. Consider if 'invalid' and 'none' can be standardized

# Returns the "category" of the verb if known, otherwise returns "unknown"
# Working off the assumption that the first word used is the command / verb.
def checkCommand(wordArray):
	# Special handling for look vs look at since only command is sent
	# Needs more refinement to make "look at door" and "look door" the same
	if ((len(wordArray) > 1) and ((wordArray[0] == "look") and (wordArray[1] == "at"))):
		return "look_at"
	else:
		category = parseCategory.identify(wordArray[0])
	return category


# This executes the specified command by calling whichever functions
# The command and item should have been validated before calling this
# _maybe_ can combine with findCategory() but would need to restructure
# TODO: Maybe separate out commands that don't require items early on
# 	ex. moving "save" and "load" to be handled and skip over item / prep process
#	The default arguments may or may not be required here.
# TODO: Note that single-item commands may need a different function than
# 	the double-item commands (take item != take item to the feature)
def executeCommand(wordArray, category, item1='none', item2='none'):
	if (category == "savegame"):
		stubs.saveGame()
	elif (category == "loadgame"):
		stubs.loadGame()
	elif (category == "inventory"):
		stubs.showInventory()
	elif (category == "look"):
		stubs.look(wordArray, item1)
	elif (category == "look_at"):
		stubs.lookAt(item1)
	elif (category == "go"):
		# Should adjust this so it clearly accepts different "places" not "items"
		stubs.goTo(item1)
	elif (category == "take"):
		if (item2 != 'none'):
			stubs.bring(item1, item2)
		else:
			stubs.take(item1)
	elif (category == "help"):
		stubs.help()
	elif (category == "drop"):
		stubs.drop(item1)
	elif (category == "quit"):
		# Currently this is never reached because it is also handled in getInput()
		# Should be altered to be handled here instead, probably when properly integrated with engine
		stubs.quit()
	elif (category == "use"):
		stubs.use(item1, item2)
	elif (category == "move"):
		stubs.move(item)
	else:
		# Some custom handling here - ex. new actions? add more elifs?
		print "You " + wordArray[0] + " the " + item1 + "."
	return True


# Putting this into a function to mimic what probably happens in overall program.
def getInput():
	lineInput = raw_input('Your action: ')

	# Defining items early to prevent errors
	item1 = 'none'
	item2 = 'none'

	# Stripping determiners/articles from sentence ('the', 'a', 'an')
	newString = parseArticles.removeArticles(lineInput)

	# Split sentence into its component words
	wordArray = newString.split(" ")
	command = wordArray[0]
	# Probably need to insert a check if a valid object is specified, or how to handle missing prepositions
	# For that matter, determine where the item is going to be in a sentence (wordArray[1] or wordArray[2])
	# maybe keep a list of items in the room, loop and check each word, then return a contextual response?
	#listOfItems = ['key', 'door', 'plant', 'bird', 'plane', 'superman']
	listOfItems = ['straw', 'bench', 'board', 'window', 'keys', 'door']
	# may want to separate out list of features and add a separate check.  Limit 4 currently.
	
	# Check if the command used is known / valid
	category = checkCommand(wordArray)
	if (category == "quit"):
		stubs.quit()
		return False
	# Invalid command used.
	elif (category == "unknown"):
		print "You want to " + wordArray[0] + " but you don't know how.  Try a different command."
	else: 
		# One- or two- word command
		if (len(wordArray) == 1):
			# Maybe should add a check here to see if a single word input was allowed for that command
			# Instead of within the executeCommand() function
			executeCommand(wordArray, category)
			return True
		item1 = parseItem.findItemUsed(wordArray, listOfItems)
		#if (item1 == 'invalid'):
			# An error message was probably already generated
			#return True
		
		if (len(wordArray) > 2):
			# Create a second string / array to skip over first known item and find the second
			removedItem1 = newString.replace(item1, ' ')
			wordArray2 = removedItem1.split(' ')
			item2 = parseItem.findItemUsed(wordArray2, listOfItems)
			#print "Item1: " + item1 + " Item 2: " + item2
			if (item2 != "invalid"):
				# not sure what to do with the preposition function yet, or if it even belongs here
				preposition = parsePreposition.identify(wordArray, item1, item2)
		executeCommand(wordArray, category, item1, item2)
	return True


# Update to run main function for parseCommands.py separately from main.py
def main():
	keepLooping = True
	while (keepLooping):
		keepLooping = getInput()

if __name__ == "__main__":
   print 'Starting the script.'
   main() 
