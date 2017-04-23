# Engine 
# Implementation of game engine

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import room
import objectC
import gamestate
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
	print "Roll the credits!"
	print ""
	print "Parsing Dev - Cheryl See"
	print "Engine Dev - Karen Thrasher"
	print "Data Dev - Matt Hillman"
#[END EXIT GAME]

#[BEGIN PLAY GAME]
def playGame(userSelection):
	print "Game play function"

	#Variables
	userInput = "default"

	#Create new or load saved game
	if userSelection == 0:	#New game
		print "NEW GAME FILE CREATED"
		#Load game state with default starting variables {Data dev}
	else:
		print "LOAD GAME FILE"
		#Load game state with saved variables {Data dev}

	#Load room files {Data dev}

	#Load object files {Data dev}

	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	while userInput not in ['loadgame', 'savegame', 'quit']:
		userInput = raw_input (": ")
		#Parse user input {Parsing Dev}
		print "play!"


#[END PLAY GAME]

#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater