# This will handle preposition recognition / processing
# References: 
# http://www.spwickstrom.com/prepositions/
# https://www.grammarly.com/blog/prepositions/
import parseItem

# Searches sentence for likely preposition matches
# Probably between two objects (an item and a feature, item and item)
# Should be an invalid command if missing an item (ex. "Put in")
# Should be an invalid command if missing a second object (ex. "Put key in")
# Definitely should be invalid if missing a command (ex. "key in")
# If there is a preposition, probably is 3rd word [cmd][item][prep][object]
def identify(wordArray, item1, item2):
	# item.position() should return first instance of the item's location
	#itemPosition = parseItem.position(wordArray)
	positionItem1 = parseItem.positionInWord(wordArray, item1)
	positionItem2 = parseItem.positionInWord(wordArray, item2)

	# Check for error state - if there are >1 words between item1 + item2
	# Stripped articles, but this logic may not hold if adjectives, etc. used
	#	ex. "Use the lamp on the dark staircase"
	if (positionItem2 - positionItem1 != 2):
		print "Error: There are " + str(positionItem2 - positionItem1) + " words between 1 and 2."
		print "positionItem1: " + str(positionItem1) + " positionItem2: " + str(positionItem2)
		print "Phrase: " + str(wordArray)
		print "item1: " + wordArray[positionItem1] + " item2: " + wordArray[positionItem2]
		return -1

	# Expected result should be right after the first item
	else:
		return (positionItem1 + 1)



# A listing of preposition types - will work like categories
def types ():
	#above: above, on, onto, over
	#under: under, underneath, below, beneath
	#by: by, near, against, beside, along, with
	#in: in, inside, into, through
	#off: off, away, apart
	#to: to, towards

	# Very situational
	#between: between (and constuction may be required)
	#down: down
	#up: up
	#outside: outside
	#around: around
	#behind: behind
	return