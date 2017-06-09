# This file contains functions that identify items or features (mostly) for parsing.

# This translates attributes in the object to their colloquial equivalents.
# Used for help function in utils or anything pulling data from the gamestate object.
# Possibly missing: paper clip in room 12 (= lockpick?), keycard (keycarddisc)
itemKeysDict = {'rm01o1': 'board', 'rm01o2': 'keys', 'rm02o1': 'handle', 'rm04o1': 'skeleton key',
				'rm06o1': 'small key', 'rm07o1': 'gun', 'rm12o1': 'lockpick', 'paperclipDisc': 'paper clip',
				'rm14o1':'cryptex', 'keycardDisc': 'keycard',
				}

# Identifies the location (to be used specifically with "go")
def findLocation(input, features):
	# Some directional word was used
	for direction in ['north', 'south', 'east', 'west', 'up', 'down']:
		if direction in input:
			return direction

	# A feature was referenced, hopefully some sort of door
	return identifyFeature(input, features)

# Checks if an item was specifically referenced in the input
def identifyItem(input, items):
	for item in items:
		if item in input:
			return item
		else:
			synonymList = items[item]
			for synonym in synonymList:
				if synonym in input:
					return item

# Checks if a feature was specifically referenced in the input
def identifyFeature(input, features):
	for feature in features:
		if feature in input:
			return feature