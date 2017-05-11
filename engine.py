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
   	print "   Load Game -- COMING SOON"
   	print "   Exit"
   	print ""
   	print ""
   	userInput = raw_input (": ")
   	while userInput not in ['New Game', 'New', 'new', 'Load Game', 'load game', 'load','Exit','exit','Quit', 'quit']:
		print "Please make a valid selection"
		userInput = raw_input (": ")

	if userInput in ['New Game', 'New', 'new', 'new game', 'New game']:	#New Game
		newGame()
	elif userInput in ['Load Game', 'load game', 'load', 'Load', 'Load game']:	#Load Game
		loadGame()
	else:
		exitGame()

	#Exit
#[END LAUNCH]

#[BEGIN NEW GAME]
def newGame():

	#Intro story
	print "                                                                                "
	print "The dream you were having fades away as you become aware of a gentle rocking"
	print "motion. You open your eyes and the dimly lit room slowly comes into focus. The "
	print "only source of light is coming through a small window. It's cold and the air  "
	print "smells damp. Sitting up slowly, you wonder where you are..."
	print ""

	playGame(0)	#New game

#[END NEW GAME]

#[BEGIN LOAD GAME]
def loadGame():
	print ""
	print "Loading your save file."
	print ""

	playGame(1)	# Load game
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

	#Initial variables
   	userInput = "default"	#Default message for user input
   	userRoom = 0   #Sentinel variable for room

	#Create new or load saved game
	if userSelection == 0:	#New game
		print "NEW GAME FILE CREATED"
		
		#PENDING - Load game state with default starting variables {Data dev}
		currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 1, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

	else:
		print "LOAD GAME FILE"
		#PENDING - Load game state with saved variables {Data dev}

	#PENDING - Load room files {Data dev}

	#PENDING - Load object files {Data dev}


	#Parse user input and return code for engine action {Parsing Dev}

	#[BEGIN TEXT PARSING]
	#keepLooping = True
	#while (keepLooping):
	#	keepLooping = parseCommands.getInput()
	#[END TEXT PARSING]

	#TEMPORARY - ENGINE PARSING
	#userInput = raw_input (": ")

	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	while userInput not in ['loadgame', 'savegame', 'quit', 'exit']:

		#[BEGIN ENGINE]
		#Level One - Midpoint Check 

		if userRoom != currentState.currRoom:  #Displays room description when player moves rooms

			#Display short / long desc
			if currentState.currRoom == 1:   #Brig
				if currentState.rm01vis == 0:
					print brig.longDesc
					currentState.rm01vis = 1 #Update to visited
				else:
					print brig.shortDesc

			elif currentState.currRoom == 2:    #Storage
				if currentState.rm02vis == 0:
					print storage.longDesc
					currentState.rm02vis = 1 #Update to visited
				else:
					print storage.shortDesc

			elif currentState.currRoom == 3:  #Lower Hallway
				if currentState.rm03vis == 0:
					print hallway.longDesc
					currentState.rm03vis = 1 #Update to visited
				else:
					print hallway.shortDesc

			elif currentState.currRoom == 4:    #Observation
				if currentState.rm04vis == 0: 
					print observation.longDesc
					currentState.rm04vis = 1 #Update to visited
				else:
					print observation.shortDesc

			elif currentState.currRoom == 5:    #Examination
				if currentState.rm05vis == 0: 
					print examination.longDesc
					currentState.rm05vis = 1 #Update to visited
				else:
					print examination.shortDesc

			userRoom = currentState.currRoom #Update room the user is currently in

		#Pend input:
		serInput = raw_input (": ")

		#Parse user input {Parsing Dev}
		userInput = parseCommands.getInput(userInput, currentState.currRoom)
	  

		#[END ENGINE]

	if userInput == "loadgame":
		print "Load game"
		#PENDING - Load game function {Data Dev}

	elif userInput == "savegame":
		print "Save game"
		#PENDING - Save game function {Data Dev}

	elif userInput == "quit" or "exit":
		exitGame()

#[END PLAY GAME]


#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater