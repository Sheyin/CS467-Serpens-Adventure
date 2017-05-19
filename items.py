# Actions upon items or features - part of parsing


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