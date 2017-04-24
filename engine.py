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
	print "only source of light is a small lantern hanging from the ceiling. The air "
	print "smells stale with a hint of fuel. Sitting up slowly, you wonder where you are..."
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
		#Testing: 
		currentRoom = room.RoomClass("default N", "default S", "default E", "default W", "default Up", "default Down", "long Desc", "short Desc", "Name of Room", "feature 1", "feature 2")

		#PENDING - Load game state with default starting variables {Data dev}
	else:
		print "LOAD GAME FILE"
		#PENDING - Load game state with saved variables {Data dev}

	#PENDING - Load room files {Data dev}

	#PENDING - Load object files {Data dev}

	#userInput = raw_input (": ")
	#Parse user input and return code for engine action {Parsing Dev}

	#[BEGIN TEXT PARSING]
	keepLooping = True
	while (keepLooping):
		keepLooping = parseCommands.getInput()
	#[END TEXT PARSING]



	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	#while userInput not in ['loadgame', 'savegame', 'quit']:
		#Check game state for current room
		#currentRoom = gamestate

		#If visited is false, display long description
		#Else, display short description & update game state to show visited

		#Pend input:
		#userInput = raw_input (": ")
		#Parse user input {Parsing Dev}
		#print "input rec"

		#if parsedText == "TN": #Travel North
		#	print "Travel north"

		#Respond to user input and update necessary variables in game state


#[END PLAY GAME]

# Engine Actions
# savegame {Data Dev}
# loadgame {Data Dev}
# exit 
# go (north, south, east, west, down, up)
# drop item
# take item
# look 
# look at object
# look at feature
# help 
# inventory



#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater