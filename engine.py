# Engine 
# Implementation of game engine

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

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
#[END LAUNCH]

#[BEGIN NEW GAME]
def newGame():
	print "Starting a new game"

	#Load game state with default starting variables {Data dev}

	#Intro story

	playGame()

#[END NEW GAME]

#[BEGIN LOAD GAME]
def loadGame():
	print "Loading a saved game"

	#Load game state with saved variables {Data dev}

	playGame()
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
def playGame():
	print "Game play function"

	#Variables
	userInput = "default"

	#Load room files {Data dev}

	#Load object files {Data dev}

	#while ((userInput != "loadgame") or (userInput != "savegame") or (userInput != "quit"))
	#	userInput = raw_input (": ")
	#	print "playing the game"
	while userInput not in ['loadgame', 'savegame', 'quit']:
		userInput = raw_input (": ")
		print "play!"


#[END PLAY GAME]

#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater