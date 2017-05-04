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
# 4. Consider if 'invalid' and 'none' can be standardized

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
# The command and item should have been validated before calling this.
# _maybe_ can combine with findCategory() but would need to restructure
# TODO: Maybe separate out commands that don't require items early on
# 	ex. moving "save" and "load" to be handled and skip over item / prep process
#	The default arguments may or may not be required here.
# TODO: Note that single-item commands may need a different function than
# 	the double-item commands (take item != take item to the feature)
def executeCommand(wordArray, category, item1='none', item2='none', listOfItems=[]):
	if (category == "savegame"):
		return stubs.saveGame()
	elif (category == "loadgame"):
		return stubs.loadGame()
	elif (category == "inventory"):
		return stubs.showInventory()
	elif (category == "look"):
		return stubs.look(wordArray, item1)
	elif (category == "look_at"):
		return stubs.lookAt(item1)
	elif (category == "go"):
		# Should adjust this so it clearly accepts different "places" not "items"
		return stubs.goTo(item1)
	elif (category == "take"):
		if (item2 != 'none'):
			return stubs.bring(item1, item2)
		else:
			return stubs.take(item1)
	elif (category == "help"):
		return stubs.help(listOfItems)
	elif (category == "drop"):
		return stubs.drop(item1)
	elif (category == "quit"):
		# Currently this is never reached because it is also handled in getInput()
		# Should be altered to be handled here instead, probably when properly integrated with engine
		return stubs.quit()
	elif (category == "use"):
		return stubs.use(item1, item2)
	elif (category == "move"):
		return stubs.move(item1)
	elif (category == "hit"):
		return stubs.hit(item1)
	else:
		# Some custom handling here - ex. new actions? add more elifs?
		#print "You " + wordArray[0] + " the " + item1 + "."
		print "You can't do that right now."
	return "unknown"


# This receives input from engine/engineTest, validates and returns an engine code
def getInput(lineInput):
	item1 = 'none'
	item2 = 'none'

	# Stripping determiners/articles from sentence ('the', 'a', 'an')
	newString = parseArticles.removeArticles(lineInput)

	# Split sentence into its component words
	wordArray = newString.split(" ")
	command = wordArray[0]

	# This should be populated from a text file
	listOfItems = ['straw', 'bench', 'board', 'window', 'keys', 'door']
	listOfFeatures = ['window', 'door', 'bench']
	# may want to separate out list of features and add a separate check.  Limit 4 currently.
	
	# Is this a valid command?
	category = checkCommand(wordArray)

	if (category == "quit"):
		return "exit"

	elif (category == "unknown"):
		# This is to continue support of engine codes (numerical input)
		if (int(lineInput) >= 0) and (int(lineInput) <= 20):
			return lineInput
		else:
			print "You want to " + command + " but you don't know how.  Try a different command."
	else: 
		# One-word command
		if (len(wordArray) == 1):
			# Maybe should add a check here to see if a single word input was allowed for that command
			# Instead of within the executeCommand() function
			return executeCommand(wordArray, category, "none", "none", listOfItems)
		item1 = parseItem.findItemUsed(wordArray, listOfItems)
		
		# Two-word command
		if (len(wordArray) > 2):
			# Create a second string / array to skip over first known item and find the second
			removedItem1 = newString.replace(item1, ' ')
			wordArray2 = removedItem1.split(' ')
			item2 = parseItem.findItemUsed(wordArray2, listOfItems)
			#print "Item1: " + item1 + " Item 2: " + item2
			if (item2 != "invalid"):
				# not sure what to do with the preposition function yet, or if it even belongs here
				preposition = parsePreposition.identify(wordArray, item1, item2)
		return executeCommand(wordArray, category, item1, item2, listOfItems)


'''
# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
   print 'Starting the script.'
   keepLooping = True
	while (keepLooping):
		userInput = raw_input (": ")
		keepLooping = getInput(userInput)
'''
