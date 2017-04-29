# Engine 
# Implementation of game engine

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import room
import objectC
import gamestate
import parseCommands
#[END IMPORTS]

#[BEGIN LAUNCH]
def launch():
	#Display title and menu
	print "______               _   _____                "
	print "|  _  \             | | |_   _|               "
	print "| | | |___  __ _  __| |   | | _ __            "
	print "| | | / _ \/ _` |/ _` |   | || '_ \           "
	print "| |/ /  __/ (_| | (_| |  _| || | | |          "
	print "|___/ \___|\__,_|\__,_|  \___/_| |_|          "
	print ""
	print ""
	print " _____ _            _    _       _            "
	print "|_   _| |          | |  | |     | |           "
	print "  | | | |__   ___  | |  | | __ _| |_ ___ _ __ "
	print "  | | | '_ \ / _ \ | |/\| |/ _` | __/ _ \ '__|"
	print "  | | | | | |  __/ \  /\  / (_| | ||  __/ |   "
	print "  \_/ |_| |_|\___|  \/  \/ \__,_|\__\___|_|   "
 	print ""
 	print ""
   	print "Please make a selection: "
   	print "   New Game"
   	print "   Load Game"
   	print "   Exit"
   	print ""
   	print ""
   	userInput = raw_input (": ")
   	while userInput not in ['New Game', 'New', 'new', 'Load Game', 'load game', 'load','Exit','exit','Quit', 'quit']:
		print "Please make a valid selection"
		userInput = raw_input (": ")

	if userInput in ['New Game', 'New', 'new']:	#New Game
		newGame()
	elif userInput in ['Load Game', 'load game', 'load']:	#Load Game
		loadGame()
	else:
		exitGame()

	#Exit
#[END LAUNCH]

#[BEGIN NEW GAME]
def newGame():
	print "Starting a new game"

	#Intro story
	print "                                                                                "
	print "The dream you were having fades away as you become aware of a gentle rocking"
	print "motion. You open your eyes and the dimly lit room slowly comes into focus. The "
	print "only source of light is coming through a small window. It's cold and the air  "
	print "smells damp. Sitting up slowly, you wonder where you are..."
	print ""

	playGame(0)

#[END NEW GAME]

#[BEGIN LOAD GAME]
def loadGame():
	print "Loading a saved game..."

	playGame(1)
#[END LOAD GAME]

#[BEGIN EXIT GAME]
def exitGame():
	print ""
	print "Roll the credits!"
	print ""
	print "Parsing Dev - Cheryl See"
	print "Engine Dev - Karen Thrasher"
	print "Data Dev - Matt Hillman"
	print ""
	print "Thank you for playing!"
	print ""
#[END EXIT GAME]

#[BEGIN PLAY GAME]
def playGame(userSelection):
	print "Game play function"

	#Variables
	userInput = "default"

	#Create new or load saved game
	if userSelection == 0:	#New game
		print "NEW GAME FILE CREATED"
		#currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 
		#	1, 4, 2,
		#	0)

		#PENDING - Load game state with default starting variables {Data dev}
	else:
		print "LOAD GAME FILE"
		#PENDING - Load game state with saved variables {Data dev}

	#PENDING - Load room files {Data dev}
	#brig = room.RoomClass("1", "Brig", "3", "null", "null", "null", "null", "null", 
	#	"You are in a cold, damp room. The only source of light is coming through a barred window. There is straw on the floor and a low wooden bench in the corner. The only exit is a barred door to the North.", 
	#	"You are in a room that has straw on the floor and a bench in the corner. Light is coming through a barred window and there is a barred door to the North.", 
	#	"straw", 
	#	"There is thick layer of straw on the floor. It smells musty.",
	#	"search, move, lift"
	#	"You shift the straw around throughout the room. It's slimy underneath but there's nothing else there."
	#	"feature 2")

	#PENDING - Load object files {Data dev}



	#Parse user input and return code for engine action {Parsing Dev}

	#[BEGIN TEXT PARSING]
	#keepLooping = True
	#while (keepLooping):
	#	keepLooping = parseCommands.getInput()
	#[END TEXT PARSING]

	#TEMPORARY - ENGINE PARSING
	#userInput = raw_input (": ")

	#Initial variables
	currentRoom = currentState.currRoom
	print "Current Room: " 
   	print currentRoom

	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	while userInput not in ['loadgame', 'savegame', 'quit']:
		#Check game state for current room
		#currentRoom = gamestate

		#If visited is false, display long description
		#Else, display short description & update game state to show visited

		#Pend input:
		userInput = raw_input (": ")
		#Parse user input {Parsing Dev}
		print "input rec"

		#if parsedText == "TN": #Travel North
		#	print "Travel north"

		#Respond to user input and update necessary variables in game state
		#Engine receives action code (listed below) and performs relevant action

#[END PLAY GAME]

# Engine Actions
# 1 - savegame {Data Dev}
# 2 - loadgame {Data Dev}
# 3 - exit 
# 4 - go north
# 5 - go south
# 6 - go east
# 7 - go west
# 8 - go down
# 9 - go up
# 10 - drop item
# 11 - take item
# 12 - look 
# 13 - look at object
# 14 - look at feature
# 15 - help 
# 16 - inventory



#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater