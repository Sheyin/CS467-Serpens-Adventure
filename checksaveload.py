import os
from utils import display

# These functions act as helper functions for the save and load interface.
# Produces a string (number) which can then be sent to the actual save/load functions.

# Call this to prompt to ask for the correct file to load 
# This returns a number in string form (save game file to load, filtered)
# Returns nothing if load is cancelled.  (Add a check before calling save/load)
def checkLoading():
	path = "data/gamestate/"
	fileList = os.listdir(path)
	fileNumbers = []

	if "0.json" in fileList:
		fileList.remove("0.json")

	for gamestate in fileList:
		strippedName = gamestate.strip(".json")
		fileNumbers.append(strippedName)
		file = open(path + gamestate, 'r')
		# skip first line
		file.readline()
		currentRoomLine = file.readline().rstrip()
		currentRoom = currentRoomLine[15:-1]
		
		display("Save Game #" + strippedName + ":    Current Room: " + currentRoom)
		file.close()

	choice = "unknown"
	while choice not in ['cancel', 'quit', 'stop', 'end', 'exit']:
		print ""
		display("Which save game would you like to load?")
		display("Please select a number or enter 'cancel'.")
		print ""
		choice = raw_input(': ')
		choice = choice.lower()

		if choice in fileNumbers:
			print ""
			display("Loading save #" + choice + ".")
			return choice
		elif choice in ['cancel', 'quit', 'stop', 'end', 'exit']:
			display("Game will not be loaded.")
			return "cancel"
		else:
			display("This is not a valid selection.")


# Call this to prompt to ask for the correct file to save
# This returns a number in string form (save game file to be created/overwritten, filtered)
# Returns nothing if load is cancelled.  (Add a check before calling save/load)
def checkSaving():
	path = "data/gamestate/"
	fileList = os.listdir(path)
	fileNumbers = []

	if "0.json" in fileList:
		fileList.remove("0.json")

	for gamestate in fileList:
		strippedName = gamestate.strip(".json")
		fileNumbers.append(strippedName)

	choice = "unknown"
	while choice not in ['cancel', 'quit', 'stop', 'end', 'exit']:
		print ""
		display("Please enter a number to save your game in or enter 'cancel'.")
		print ""
		choice = raw_input(': ')
		choice = choice.lower()
		if choice == "0":
			display("Sorry, you cannot use this as a filename.  Please choose another.")
		elif choice in fileNumbers:
			print ""
			display ("A save game by this number already exists.  Would you like to overwrite this save?")
			confirm = raw_input(': ')
			if confirm.lower() in ['y', 'yes', 'yeah', 'do it', 'proceed', 'ok', 'go ahead', 'overwrite', 'confirm', 'sure']:
				display("Saving over game number " + choice + ".")
				return choice
			else:
				print ""
				display("File will not be overwritten.")
		elif choice in ['cancel', 'quit', 'stop', 'end', 'exit']:
			print ""
			display("Game will not be saved.")
			return "cancel"
		else:
			display("Game is saved.")
			return choice