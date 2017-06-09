# Story-specific bits.  More specifically, the conclusion.
from utils import display
import textwrap

# This reads the gamestate file and populates the variables for the conclusion text
def ending(gamestate):
	flags_to_check = {
	# Temporarily putting paperclipDisc for bracelet since it isn't in the gamestate yet
		'injured': 'floatGun', 'bracelet': 'paperclipDisc',
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


def endingText(injured = True, bracelet = True):
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

	if bracelet:
		display("You idly fiddle with the bracelet around your wrist.  It was strange that it had forcibly been put on you, but you decide not to give it any further thought.  After all, you are now free!")
	else:
		display("You feel a slight chill go through you.  The wind?  Or perhaps it was because of seeing those same numbers again.  Luckily you had found that mysterious hint telling you how to remove it...")
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
			display("You turn the wheels to spell out " + userInput.upper() + ".  The cryptex opens with a click.  You slide out the central portion revealing a keycard.  Wonder what it's used for?")
			print ""
			display("You also find a note in there with some numbers on it.  It reads '4815162342' on it.  You have no idea what it means, but it seems significant.  Maybe you should commit this to memory.  If only you had a pen and paper...")
			return True
		else:
			display("You turn the wheels to spell out " + userInput.upper() + ".  You tug at the sides, but it does not open.  Seems that you had the incorrect word.")
		print ""

# For the control room button pushing
# This minigame is like operating a crane but the controls are a bit mixed up.
# Succeeding lifts the glass over the keycard
'''
def buttonGame():
	correct = 0
	incorrect = 0
	answered = []

	display("You sit down in the chair.  It's a bit uncomfortable, but as you do so, the screen in front of you changes.")
	print ""
	display("The screen reads: ")
	display("This is a memory test.  The answers are all single-word answers.  You may pass if you do not know the answer to the question.  There are 10 questions in total.  Please note that if you leave, the questions will be reset and randomized.")

	userInput = ""

	questions = {
	1: "What is under the straw?", 
	2: "What was in the locker?",
	3: "How many doors were in the first hallway?",
	4: "What was in the first chest?",
	5: "What is on the table on the first floor?",
	6: "Name something hanging from the ceiling in the rum room.",
	7: "What did you get from using the small key?",
	8: "What did you find in the garrison?",
	9: "What was behind the glass door?",
	}

# single word answers or correct the instructions
	answers = {
	1: ("nothing"),
	2: ("handle"),
	3: ("five"),
	4: ("skeleton key"),
	5: ("carving"),
	6: ("lamp", "bottle", "oil lamp"),
	7: ("gun"),
	8: ("beds", "photograph", "table"),
	9: ("garden"),
	}

	display(questions[1])
	'''

	'''
	while userInput not in ['stop', 'quit', 'walk away', 'get up', 'cancel', 'end', 'exit']:
		display("")
		print ""
		userInput = raw_input(': ').lower()
	'''

# This is supposed to work with the button() function and display a game board
# Textwrap requires a string as input (10 characters across including spaces)
# make sure the height is not very high either
'''
def gamescreen(input):
	textToPrint = textwrap.wrap(input, 13)
	for line in textToPrint:
		print '  ' + line


def button_input():
	while userInput not in ['stop', 'quit', 'walk away', 'get up', 'cancel', 'end', 'exit']:
		display("")
		print ""
		userInput = raw_input(': ').lower()	\
'''


if __name__ == "__main__":
	# Same ending printed multiple times
	buttonGame()