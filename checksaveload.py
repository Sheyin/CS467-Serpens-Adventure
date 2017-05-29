# Mostly to produce a mockup of save interface
import os
from utils import display

# This returns a number in string form (save game file to load, filtered)
def checkSaving():
	path = "data/gamestate/"
	fileList = os.listdir(path)
	fileNumbers = []

	for gamestate in fileList:
		strippedName = gamestate.strip(".json")
		fileNumbers.append(strippedName)
		display("Save Game #" + strippedName + ":")
		file = open(path + gamestate, 'r')
		# skip first line - name
		file.readline()
		currentRoomLine = file.readline()
		currentRoom = currentRoomLine[15:-2]
		display("Current Room:" + currentRoom)
		file.close()

	choice = "unknown"
	while choice not in ['cancel', 'quit', 'stop', 'end', 'exit']:
		print ""
		display("Which save game would you like to load?")
		display("Please select a number or enter 'cancel'.")
		choice = raw_input(':')
		choice = choice.lower()
		if choice in fileNumbers:
			return choice
		elif choice in ['cancel', 'quit', 'stop', 'end', 'exit']:
			display("Game will not be saved.")
		else:
			display("This is not a valid selection.")


# This returns a number in string form (save game file to be created, filtered)
def checkLoading():
	path = "data/gamestate/"
	fileList = os.listdir(path)
	fileNumbers = []

	for gamestate in fileList:
		strippedName = gamestate.strip(".json")
		fileNumbers.append(strippedName)

	choice = "unknown"
	while choice not in ['cancel', 'quit', 'stop', 'end', 'exit']:
		print ""
		display("Please enter a number to save your game in or enter 'cancel'.")
		choice = raw_input(':')
		choice = choice.lower()
		if choice in fileNumbers:
			display ("A save game by this number already exists.  Would you like to overwrite this save?")
			confirm = raw_input(':')
			if confirm.lower() in ['y', 'yes', 'ok', 'go ahead', 'overwrite', 'confirm']:
				display ("Saving over game number " + choice + ".")
				return choice
		elif choice in ['cancel', 'quit', 'stop', 'end', 'exit']:
			display("Game will not be saved.")

# Update to run main function for parseCommands.py separately from main.py
if __name__ == "__main__":
	print 'Starting the script.'
	checkLoading()
