# Much of this commented out as trying regular expressions
import re

# Displays an error message for an invalid action
# TODO: randomize the error messages (optional)
def randomErrorMessage(wordArray, word):
	if ((wordArray[0] == "take") or (wordArray[0] == "look_at")):
		print "You try to " + wordArray[0] + " the " + word + " but you realize there isn't one."
	else:
		print "You try to " + wordArray[0] + " the " + word + " but you realize you don't have one."



# This identifies where in a sentence an item is located
# if it doesn't match any known items, then it will guess at words
# after particles (after "the", "a", ), then prepositions ("in", "on")
# Returns a negative value if the word was a guess, but positive
# if the item was confirmed (on the list of items in a room)
#def position(wordArray, listOfItems):
def position(wordArray, listOfItems, listOfFeatures):

	# Single word input, so there is no item:
	if (len(wordArray) == 1):
		return 0

	# Check if the item referenced is an "item"
	for wordPos in range (0, len(wordArray)):
		for itemPos in range (0, len(listOfItems)):
			if (wordArray[wordPos] == listOfItems[itemPos]):
				return wordPos

	# Check if the item referenced is a "feature"
	for wordPos in range (0, len(wordArray)):
		for itemPos in range (0, len(listOfFeatures)):
			if (wordArray[wordPos] == listOfFeatures[itemPos]):
				return wordPos

	# --anything past this point is strictly optional - the item is not a known object in room

	# This should be erased since particles are being stripped in the beginning now
	# item name is not found - infer an answer based on particles
	particles = ['the', 'a']
	for wordPos in range (0, len(wordArray)):
		for articlePos in range (0, len(particles)):
			if (wordArray[wordPos] == particles[articlePos]):
				# turning this negative so we know it was not a recognized object, just a guess
				return -wordPos

	# item name is still not found - assume it is right after the command 
	# command is assumed to be the first word in the sentence
	if (wordArray[1] == "at") and (len(wordArray) > 2):
		return -2
	else:
		return -1


# Identifies the verb and item, as well as location, for easier handling
# TODO: For unrecognized items right now it is calling randomErrorMessage() AND being 
# handled in executeCommand, so it should be consolidated into one or the other.
def findItemUsed(wordArray, listOfItems, listofFeatures):

	# The verb is _probably_ in the first word used, identify category (meaning/intent of the word)
	#command = wordArray[0]
	#category = parseCategory.identify(command)

	# Identify the item and its position in the sentence
	positionOfItem = position(wordArray, listOfItems, listofFeatures)
	if (positionOfItem < 0):
		# Item was not found in room, so guessed at it for a response
		# displaying a message stating the command tried to operate on an invalid item
		word = wordArray[abs(positionOfItem)]
		return "invalid"
	else:
		word = wordArray[positionOfItem]
		return word
	# Prepositions are either between the command and item, or after the item


# Locates a given word and returns its position in the sentence.
# This is used by other functions and might be categorized under "general"
# Similar to position() but we already know the word, just need to know where.
def positionInWord(wordArray, word):
	for wordPos in range (0, len(wordArray)):
		if (wordArray[wordPos] == word):
			return wordPos
	# Word not found in sentence
	return -1