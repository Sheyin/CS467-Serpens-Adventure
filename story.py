# Story-specific bits.  More specifically, the conclusion.
from utils import display
import textwrap


# Confirmation prompt just before starting the ending sequence
def endingPrompt():
	escapeWords = ["yes", "do it", "exit", "leave", "go out", "outside", "escape", "run away", "crawl through", "freedom", "go hatch", "leave ship", "gtfo"]
	display("The hatch is open, and there are no obstacles between you and freedom.  If you leave, you'll probably never step foot in this place again.    What do you want to do?")
	print ""
	userInput = raw_input(': ').lower()
	if userInput in escapeWords:
		display("You've had enough of this place.  It's time to go.")
		return True
	else:
		display("You decide to stay a while longer.")
		return False


# This reads the gamestate file and populates the variables for the conclusion text
def ending(gamestate):
	flags_to_check = {
	# Temporarily putting paperclipDisc for bracelet since it isn't in the gamestate yet
		'injured': 'floatGun',
	}
	variableList = []

	# Check each of these variables
	for flag in flags_to_check:
		state = getattr(gamestate, flags_to_check[flag])
		if flag == "1":
			variableList.append(True)
		else:
			variableList.append(False)

	endingText(*tuple(variableList))


# Prints the actual conclusion text
def endingText(injured = True):
	# Check gamestate for certain variables.  By default they will be true.

	display("You are blinded by the sudden influx of light as the hatch creaks open.  You feel weak with relief.  It's the outdoors - no doubt about it.")
	print ""

	if injured:
		display("As you climb out, you stifle a curse as your injured skin brushes against the hatch.  The gun explosion had left you slightly scorched - but alive.  Hopefully there are no guards around.")
	else:
		display("You climb out of the hatch carefully and quietly.")
	print ""

	display("You wince as the hatch creaks closed.  Looking around, it seems you really are on a boat.  A rather large one, in fact, much bigger than what you had seen inside.")
	print ""
	display("No one seems to be around.  You turn and give the hatch you came from a final look.  A sign reading '4815162342' is above the entryway.  There seem to be similar hatches with other numbers written above them nearby.")
	print ""

	display("You idly fiddle with the bracelet around your wrist.  It was strange that it had forcibly been put on you, but you decide not to give it any further thought.  After all, you are now free!")
	#display("You feel a slight chill go through you.  The wind?  Or perhaps it was because of seeing those same numbers again.  Luckily you had found that mysterious hint telling you how to remove it...")
	print ""

	display("You carefully make your way towards a walkway extending from the dock.  You haven't seen anyone else, and it seems like a quiet sunny day, but you don't want to let down your guard.  You make your way off the boat, and onto solid land.")
	print "" 
	display("Freedom, at last.  For a while you thought you were dead in the water.  But now... things seem to be looking up.")
	print ""


# For unlocking the cryptex
def cryptex():
	userInput = ""
	while userInput not in ['stop', 'quit', 'put down', 'cancel', 'end', 'exit']:
		display("You fiddle with the cryptex.  It takes a five letter input.  You can stop and put down the cryptex, or enter a word.")
		print ""

		userInput = raw_input(': ').lower()
		if userInput in ['stop', 'quit', 'put down', 'cancel', 'end', 'exit']:
			display("You put down the cryptex.  Maybe you can try to open it again later.")
			return False
		if len(userInput) > 5:
			display("The word " + userInput.upper() + " is too long since it has " + str(len(userInput)) + " characters.  The cryptex only has 5 wheels, one for each letter.")
		elif len(userInput) < 5:
			display("The word " + userInput.upper() + " is too short since it has " + str(len(userInput)) + " characters.  There would be unused wheels if you used this word.")
		elif userInput == 'tyler':
			display("You turn the wheels to spell out " + userInput.upper() + ".  The cryptex opens with a click.  You slide out the central portion and find a simple wedding band in it. You put it back in the cryptex for safe keeping. Someone will be missing that!")
			return True
		else:
			display("You turn the wheels to spell out " + userInput.upper() + ".  You tug at the sides, but it does not open.  Seems that you had the incorrect word.")
		print ""

if __name__ == "__main__":
	# Same ending printed multiple times
	buttonGame()