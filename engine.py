# Engine 
# Implementation of game engine

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import room
import objectC
import gamestate
import parse
import utils
import data
from data import *
from utils import display
from utils import printHelp
from utils import roomDirectory
import story
import checksaveload
import saveGame
from saveGame import *
from gamestate import *
import sys


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
	while userInput not in ['New Game', 'New', 'new', 'new game', 'Load Game', 'load game', 'load', 'Load', 'Exit','exit','Quit', 'quit', 'test']:
		display("Please make a valid selection.")
		userInput = raw_input (": ")

	if userInput in ['New Game', 'New', 'new', 'new game', 'New game']:	#New Game
		newGame()
	elif userInput in ['Load Game', 'load game', 'load', 'Load', 'Load game']:	#Load Game
		loadGame()
	elif userInput in ['test']: # Developer testing
		playGame(3)
	else:
		exitGame()
#[END LAUNCH]

#[BEGIN NEW GAME]
def newGame():

	#Intro story
	print "                                                                                "
	display("The dream you were having fades away as you become aware of a gentle rocking motion. You open your eyes and the dimly lit room slowly comes into focus. The only source of light is coming through a small window. It's cold and the air smells damp. Sitting up slowly, you wonder where you are...")
	print ""

	playGame(0)	#New game

#[END NEW GAME]

#[BEGIN LOAD GAME]
def loadGame():
	print ""
	display("Loading your save file.")
	print ""

	playGame(1)	# Load game
#[END LOAD GAME]

#[BEGIN DEVELOPER TESTING]
def devTest():
	playGame(3)	#Manually manipulate variables for dev testing
#[END DEVELOPER TESTING]

#[BEGIN PLAY GAME]
def playGame(userSelection):

	#Initial variables
	userInput = "default"	#Default message for user input
	userRoom = 0   #Sentinel variable for room

	#Create new or load saved game
	if userSelection == 0:	#New game
		#Load game state with default starting variables {Data dev}
		global currentState
		currentState = MattsGameStateClass(1)
		currentState = resume_gamestate("0")
		#print "NEW GAME FILE CREATED"

	elif userSelection == 1: #Load game
		#Load game state with saved variables {Data dev}
		loadroom = checksaveload.checkLoading()
		if loadroom != "cancel":
			currentState = resume_gamestate(loadroom)
			print ""
			afterLoading(currentState.currRoom)
		# If cancelled, load a new game instead
		print ""
		display("Starting a new game.")
		global currentState
		currentState = MattsGameStateClass(1)
		currentState = resume_gamestate("0")
		#print "LOAD GAME FILE"

	else: # Launch developer testing

		# Developer Testing Instructions:
		# Trigger from starting screen using 'test'   Note - this option is not publically listed 
		# Update currentState variables manually to drop into any room with any combination
		#     of items. Allows for testing without repeating game sequence. 

		currentState = gamestate.GameStateClass(11,   #currentRoom
	      1, #room1
	      1, #room2
	      1, #room3
	      1, #room4
	      1, #room5
	      1, #room6
	      1, #room7
	      1, #room8
	      1, #room9
	      1, #room10
	      1, #room11
	      1, #room12
	      1, #room13
	      1, #room14
	      0, #room15          NOTE: 99 Item in inventory, 100 item permanently destroyed/used
	      99, #item1 - Board - Origin Room: 1
	      99, #item2 - Key - Origin Room: 1
	      100, #item3 - Handle - Origin Room: 2
	      99, #item4 - Skeleton Key - Origin Room: 4
	      99, #item5 - Small Key - Origin Room: 6
	      99, #item6 - Gun - Origin Room: 7 
	      99, #item7 - Lockpick - Origin Room: 0 (player crafted)
	      99, #item8 - Cryptex - Origin Room: 14
	      100, #item9 - Paper clip - Origin Room: 12 
	      99, #item10 - Keycard - Origin Room: 13
	      1, #rm1f1
	      1, #rm1f2
	      1, #rm1f3
	      1, #rm1f4
	      1, #rm1o1 - Board discovery
	      1, #rm1o2 - Keys discovery
	      1, #rm2f1
	      1, #rm2f2
	      1, #rm2f3
	      1, #rm2o1 - Handle discovery 
	      1, #rm3f1
	      1, #rm3f2
	      1, #rm3f3
	      1, #rm3f4
	      1, #rm3f5
	      1, #rm3f6
	      1, #rm4f1
	      1, #rm4f2
	      1, #rm4f3
	      1, #rm4f4
	      1, #rm4f5
	      1, #rm4f6
	      1, #rm4o1 - Skeleton key discovery
	      1, #rm5f1
	      1, #rm5f2
	      1, #rm5f3
	      1, #rm6f1
	      1, #rm6f2
	      1, #rm6f3
	      1, #rm6f4
	      1, #rm6f5
	      1, #rm6o1 - Small key discovery 
	      1, #rm7f1
	      1, #rm7f2
	      1, #rm7f3
	      1, #rm7f4
	      1, #rm7f5
	      1, #rm7o1 - Gun discovery
	      1, #rm8f1
	      1, #rm8f2
	      1, #rm8f3
	      1, #rm8f4
	      1, #rm8f5
	      1, #rm8f6
	      1, #rm9f1
	      1, #rm9f2
	      1, #rm9f3
	      1, #rm9f4
	      1, #rm10f1
	      1, #rm10f2
	      1, #rm11f1
	      1, #rm11f2
	      1, #rm11f3
	      1, #rm11f4
	      1, #rm11f5
	      1, #rm11f6
	      1, #rm12f1
	      1, #rm12f2
	      1, #rm12f3
	      1, #rm12f4
	      1, #rm12f5
	      1, #rm12f6
	      1, #rm12o1 - Lockpick discovery
	      1, #rm13f1
	      1, #rm13f2
	      1, #rm13f3
	      1, #rm13f4
	      1, #rm13f5
	      1, #rm13f6
	      1, #rm14f1
	      1, #rm14f2
	      1, #rm14f3
	      1, #rm14f4
	      1, #rm14f5
	      1, #rm14f6
	      1, #rm14o1 - Cryptex discovery
	      0, #rm15f1
	      0, #rm15f2
	      0, #rm15f3
	      0, #rm15f4
	      0, #rm15f5
	      0, #float1 - Gun fired
		  1, #pcD - Paperclip discovery
		  1) #kcD - Keycard discovery

	#Load room files {Data dev}
	data.load_rooms() 
	
	#Rename loaded rooms to be compatible with engine
	brig = rooms[1] 
	storage = rooms[2]
	hallway = rooms[3]
	observation = rooms[4]
	examination = rooms[5]

	#MIDDLE LEVEL ROOMS
	rum = rooms[6]
	armory = rooms[7]
	garrison = rooms[8]
	galley = rooms[9]
	ladder = rooms[10]

	#TOP LEVEL ROOMS
	topHall = rooms[11]
	garden = rooms[12]
	control = rooms[13]
	side = rooms[14]
	processing = rooms[15]

	#Load object files {Data dev}
	data.load_objects()

	#Rename objects for engine compatibility
	board = objects["board"]
	keys = objects["keys"]
	handle = objects["handle"]
	skeletonKey = objects["skeleton key"]

	#MIDDLE LEVEL OBJECTS
	smallKey = objects["small key"]
	gun = objects["gun"]

	#TOP LEVEL OBJECTS
	lockpick = objects["lockpick"]
	cryptex = objects["cryptex"]

	paperclip = objects["paper clip"]
	keycard = objects["keycard"]

	#Send room/item info to get format for parsing {Parsing dev}
	featureList, featureDict, itemDict, roomList = utils.formatRoomData(rooms, objects, currentState)

	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	while userInput not in ['quit', 'exit']:

		#[BEGIN ENGINE]
		if userRoom != currentState.currRoom:  #Displays room description when player moves rooms

			#Display short / long desc
			if currentState.currRoom == 1:   #Brig
				if currentState.rm01vis == 0:
					display(brig.longDesc)
					currentState.rm01vis = 1 #Update to visited
				else:
					display(brig.shortDesc)

			elif currentState.currRoom == 2:    #Storage
				if currentState.rm02vis == 0:
					display(storage.longDesc)
					currentState.rm02vis = 1 #Update to visited
				else:
					display(storage.shortDesc)

			elif currentState.currRoom == 3:  #Lower Hallway
				if currentState.rm03vis == 0:
					display(hallway.longDesc)
					currentState.rm03vis = 1 #Update to visited
				else:
					display(hallway.shortDesc)

			elif currentState.currRoom == 4:    #Observation
				if currentState.rm04vis == 0: 
					display(observation.longDesc)
					currentState.rm04vis = 1 #Update to visited
				else:
					display(observation.shortDesc)

			elif currentState.currRoom == 5:    #Examination
				if currentState.rm05vis == 0: 
				   display(examination.longDesc)
				   currentState.rm05vis = 1 #Update to visited
				else:
				   display(examination.shortDesc)

			elif currentState.currRoom == 6:    #Rum
				if currentState.rm06vis == 0: 
				   display(rum.longDesc)
				   currentState.rm06vis = 1 #Update to visited
				else:
				   display(rum.shortDesc)

			elif currentState.currRoom == 7:    #Armory
				if currentState.rm07vis == 0: 
				   display(armory.longDesc)
				   currentState.rm07vis = 1 #Update to visited
				else:
				   display(armory.shortDesc)

			elif currentState.currRoom == 8:    #Garrison
				if currentState.rm08vis == 0: 
				   display(garrison.longDesc)
				   currentState.rm08vis = 1 #Update to visited
				else:
				   display(garrison.shortDesc)

			elif currentState.currRoom == 9:    #Galley
				if currentState.rm09vis == 0: 
				   display(galley.longDesc)
				   currentState.rm09vis = 1 #Update to visited
				else:
				   display(galley.shortDesc)

			elif currentState.currRoom == 10:    #Ladder
				if currentState.rm10vis == 0: 
				   display(ladder.longDesc)
				   currentState.rm10vis = 1 #Update to visited
				else:
				   display(ladder.shortDesc)

			elif currentState.currRoom == 11:    #topHall
				if currentState.rm11vis == 0: 
					display(topHall.longDesc)
					currentState.rm11vis = 1 #Update to visited
				else:
					display(topHall.shortDesc)

			elif currentState.currRoom == 12:    #Garden
				if currentState.rm12vis == 0: 
					display(garden.longDesc)
					currentState.rm12vis = 1 #Update to visited
				else:
					display(garden.shortDesc)

			elif currentState.currRoom == 13:    #Control
				if currentState.rm13vis == 0: 
					display(control.longDesc)
					currentState.rm13vis = 1 #Update to visited
				else:
					display(control.shortDesc)

			elif currentState.currRoom == 14:    #Side
				if currentState.rm14vis == 0: 
					display(side.longDesc)
					currentState.rm14vis = 1 #Update to visited
				else:
					display(side.shortDesc)

			elif currentState.currRoom == 15:    #Processing
				if currentState.rm15vis == 0: 
					display(processing.longDesc)
					currentState.rm15vis = 1 #Update to visited
				else:
					display(processing.shortDesc)

			userRoom = currentState.currRoom #Update room the user is currently in

		#Parsing helper function {Parsing dev}
		featureList, featureDict, itemList, roomList = utils.formatRoomData(rooms, objects, currentState)	
			
		#Pend input:
		print ""
		userInput = raw_input (": ")

		#Parse user input and return code for engine action {Parsing Dev}
		userInput = parse.main(userInput, featureList, featureDict, itemDict, roomList, currentState.currRoom)
	  
		#ENGINE INTERACTIONS BASED ON PARSED USER INPUT
		if userInput == "1":#Look at feature 1 - STRAW / ENTRYWAY MARKINGS / LOCKER / EXAM ENTRYWAY / DOOR / BOTTLE / GUN CABINET / BUNKS / CANVAS FLAP / LADDER
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f1 == 0: #Before interaction
					display(brig.feat1desc)
				else: #After interaction
					display(brig.feat1interactComplete)
			#Storage
			elif currentState.currRoom == 2:
				if currentState.rm02f1 == 0: #Before interaction
					display(storage.feat1desc)
				else: #After interaction
					display(storage.feat1interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f1 == 0: #Before interaction
					display(hallway.feat1desc)
				else: #After interaction
					display(hallway.feat1interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f1 == 0: #Before interaction
					display(observation.feat1desc)
				else: #After interaction
					display(observation.feat1interactComplete)
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f1 == 0: #Before interaction
					display(examination.feat1desc)
				else: #After interaction
					display(examination.feat1interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f1 == 0: #Before interaction
					display(rum.feat1desc)
				else: #After interaction
					display(rum.feat1interactComplete)
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f1 == 0: #Before interaction
					display(armory.feat1desc)
				else: #After interaction
					display(armory.feat1interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f1 == 0: #Before interaction
					display(garrison.feat1desc)
				else: #After interaction
					display(garrison.feat1interactComplete)
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f1 == 0: #Before interaction
					display(galley.feat1desc)
				else: #After interaction
					display(galley.feat1interactComplete)
			#Ladder
			elif currentState.currRoom == 10:
				if currentState.rm10f1 == 0: #Before interaction
					display(ladder.feat1desc)
				else: #After interaction
					display(ladder.feat1interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f1 == 0: #Before interaction
					display(topHall.feat1desc)
				else: #After interaction
					display(topHall.feat1interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f1 == 0: #Before interaction
					display(garden.feat1desc) 
				else: #After interaction
					display(garden.feat1interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f1 == 0: #Before interaction
					display(control.feat1desc)
				else: #After interaction
					display(control.feat1interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f1 == 0: #Before interaction
					display(side.feat1desc)
				else: #After interaction
					display(side.feat1interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f1 == 0: #Before interaction
					display(processing.feat1desc) 
				else: #After interaction
					display(processing.feat1interactComplete)

		elif userInput == "2": #Interact with feature 1 
			#Brig
			if currentState.currRoom == 1:
				display(brig.feat1interactSuccess)
				currentState.rm01f1 = 1 #Update to interaction complete
			#Storage
			elif currentState.currRoom == 2:
				if currentState.rm02f1 == 0: #Not complete
					if currentState.obj1Loc == 99: #If have board
						display(storage.feat1interactSuccess)
						currentState.rm02f1 = 1 #Update to interaction complete
						currentState.rm02o1 = 1 #Handle discovered
					else:
						display(storage.feat1interactFail)
				else: #Interaction completed
					display(storage.feat1interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				display(hallway.feat1interactSuccess)
				currentState.rm03f1 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				display(observation.feat1interactSuccess)
				currentState.rm04f1 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				display(examination.feat1interactSuccess)
				currentState.rm05f1 = 1 #Update to interaction complete
			#Rum 
			elif currentState.currRoom == 6:
				display(rum.feat1interactSuccess)
				currentState.rm06f1 = 1 #Update to interaction complete
			#Armory 
			elif currentState.currRoom == 7:
				display(armory.feat1interactSuccess)
				currentState.rm07f1 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat1interactSuccess)
				currentState.rm08f1 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				display(galley.feat1interactSuccess)
				currentState.rm09f1 = 1 #Update to interaction complete
			#Ladder
			elif currentState.currRoom == 10:
				display(ladder.feat1interactSuccess)
				currentState.rm10f1 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				display(topHall.feat1interactSuccess)
				currentState.rm11f1 = 1 #Update to interaction complete
			#Garden
			if currentState.currRoom == 12:
				if currentState.rm12f1 == 0: #Not complete
					display(garden.feat1interactSuccess)
					currentState.rm12f1 = 1 #Update to interaction complete
					currentState.paperclipDisc = 1 #Paperclip discovered
					currentState.obj9Loc = 12 #Update Paperclip location to room 12
				else:
					display(garden.feat1interactComplete)
			#Control
			elif currentState.currRoom == 13:
				display(control.feat1interactSuccess)
				currentState.rm13f1 = 1 #Update to interaction complete
			#Side
			elif currentState.currRoom == 14:
				display(side.feat1interactSuccess)
				currentState.rm14f1 = 1 #Update to interaction complete
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f1 == 0: #Interaction not complete
					if currentState.rm15f3 == 1: 	#If bracelet has been applied
						display(processing.feat1interactSuccess)
						currentState.rm15f1 = 1 #Update to interaction complete
					else:
						display(processing.feat1interactFail)
				else: #Already completed
					display(processing.feat1interactComplete)


		elif userInput == "3": #Look at feature 2 - BENCH / BARRED DOOR / PAPER / TABLE / BARRED WINDOW / LAMP / WOODEN DOOR / TABLE / TRASH CAN / WOODEN DOOR
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f2 == 0: #Before interaction
					display(brig.feat2desc)
				else: #After interaction
					display(brig.feat2interactComplete)
			#Storage
			elif currentState.currRoom == 2:
				if currentState.rm02f2 == 0: #Before interaction
					display(storage.feat2desc)
				else: #After interaction
					display(storage.feat2interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f2 == 0: #Before interaction
					display(hallway.feat2desc)
				else: #After interaction
					display(hallway.feat2interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f2 == 0: #Before interaction
					display(observation.feat2desc)
				else: #After interaction
					display(observation.feat2interactComplete)
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f2 == 0: #Before interaction
					 display(examination.feat2desc)
				else: #After interaction
					 display(examination.feat2interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f2 == 0: #Before interaction
					display(rum.feat2desc)
				else: #After interaction
					display(rum.feat2interactComplete)
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f2 == 0: #Before interaction
					display(armory.feat2desc)
				else: #After interaction
					display(armory.feat2interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f2 == 0: #Before interaction
					display(garrison.feat2desc)
				else: #After interaction
					display(garrison.feat2interactComplete)
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f2 == 0: #Before interaction
					display(galley.feat2desc)
				else: #After interaction
					display(galley.feat2interactComplete)
			#Ladder
			elif currentState.currRoom == 10:
				if currentState.rm10f2 == 0: #Before interaction
					display(ladder.feat2desc)
				else: #After interaction
					display(ladder.feat2interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f2 == 0: #Before interaction
					display(topHall.feat2desc)
				else: #After interaction
					display(topHall.feat2interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f2 == 0: #Before interaction
					display(garden.feat2desc)
				else: #After interaction
					display(garden.feat2interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f2 == 0: #Before interaction
					display(control.feat2desc)
				else: #After interaction
					display(control.feat2interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f2 == 0: #Before interaction
					display(side.feat2desc)
				else: #After interaction
					display(side.feat2interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f2 == 0: #Before interaction
					display(processing.feat2desc)
				else: #After interaction
					display(processing.feat2interactComplete)

		elif userInput == "4": #Interact with feature 2
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f2 == 0: #Not complete
					display(brig.feat2interactSuccess)
					currentState.rm01f2 = 1 #Update to interaction complete
					currentState.rm01o1 = 1 #Board discovered
				else: #Task completed / board already discovered
					display(brig.feat2interactComplete)
			#Storage
			elif currentState.currRoom == 2:
				display(storage.feat2interactSuccess)
				currentState.rm02f2 = 1 #Update to interaction complete
			#Hallway
			elif currentState.currRoom == 3:
				display(hallway.feat2interactSuccess)
				currentState.rm03f2 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				display(observation.feat2interactSuccess)
				currentState.rm04f2 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				display(examination.feat2interactSuccess)
				currentState.rm05f2 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				display(rum.feat2interactSuccess)
				currentState.rm06f2 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				display(armory.feat2interactSuccess)
				currentState.rm07f2 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat2interactSuccess)
				currentState.rm08f2 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				display(galley.feat2interactSuccess)
				currentState.rm09f2 = 1 #Update to interaction complete
			#Ladder
			elif currentState.currRoom == 10:
				display(ladder.feat2interactSuccess)
				currentState.rm10f2 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f2 == 0: #Not complete
					if currentState.obj10Loc == 99:	#If keycard in inventory
						display(topHall.feat2interactSuccess)
						currentState.rm11f2 = 1 #Update to interaction complete
					else:
						display(topHall.feat2interactFail)
				else: #Task completed
					display(topHall.feat2interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f2 == 0: #Not complete
					display(garden.feat2interactSuccess)
					currentState.rm12f2 = 1 #Update to interaction complete
				else: #Action already completed
					display(garden.feat2interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f2 == 0: #Not complete
					if currentState.obj1Loc == 99: #If board in inventory
						display(control.feat2interactSuccess)
						currentState.rm13f2 = 1 #Update to interaction complete
						currentState.keycardDisc = 1 #Keycard discovered
						currentState.obj10Loc = 13 #Update keycard location to room 13
					else:
						display(control.feat2interactFail)
				else: #Action already completed
					display(control.feat2interactComplete)
			#Side
			elif currentState.currRoom == 14:
				display(side.feat2interactSuccess)
				currentState.rm14f2 = 1 #Update to interaction complete
			#Processing
			elif currentState.currRoom == 15:
				display(processing.feat2interactSuccess)
				currentState.rm15f2 = 1 #Update to interaction complete

		elif userInput == "5": #Look at object "board"
			if currentState.obj1Loc ==99: #In iventory
				display(board.desc)
			else: #Not in inventory
				display(board.notInInv)

		elif userInput == "6": #Look at feature 3 - WINDOW / METAL DOOR / DOOR / MIRROR / WINDOW / TRAP DOOR / LOCKER / PHOTOGRAPH / STOVE
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f3 == 0: #Before interaction
					display(brig.feat3desc)
				else: #After interaction
					display(brig.feat3interactComplete)
			#Storage
			if currentState.currRoom == 2:
				if currentState.rm02f3 == 0: #Before interaction
					display(storage.feat3desc)
				else: #After interaction
					display(storage.feat3interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f3 == 0: #Before interaction
					display(hallway.feat3desc)
				else: #After interaction
					display(hallway.feat3interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f3 == 0: #Before interaction
					display(observation.feat3desc)
				else: #After interaction
					display(observation.feat3interactComplete)
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f3 == 0: #Before interaction
					display(examination.feat3desc)
				else: #After interaction
					display(examination.feat3interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f3 == 0: #Before interaction
					display(rum.feat3desc)
				else: #After interaction
					display(rum.feat3interactComplete)
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f3 == 0: #Before interaction
					display(armory.feat3desc)
				else: #After interaction
					display(armory.feat3interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f3 == 0: #Before interaction
					display(garrison.feat3desc)
				else: #After interaction
					display(garrison.feat3interactComplete)
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f3 == 0: #Before interaction
					display(galley.feat3desc)
				else: #After interaction
					display(galley.feat3interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f3 == 0: #Before interaction
					display(topHall.feat3desc)
				else: #After interaction
					display(topHall.feat3interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f3 == 0: #Before interaction
					display(garden.feat3desc)
				else: #After interaction
					display(garden.feat3interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f3 == 0: #Before interaction
					display(control.feat3desc)
				else: #After interaction
					display(control.feat3interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f3 == 0: #Before interaction
					display(side.feat3desc)
				else: #After interaction
					display(side.feat3interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f3 == 0: #Before interaction
					display(processing.feat3desc)
				else: #After interaction
					display(processing.feat3interactComplete)

		elif userInput == "7": #Interact with feature 3
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f3 == 0: #Not complete
					if currentState.obj1Loc == 99:

						display(brig.feat3interactSuccess)
						currentState.rm01f3 = 1 #Update to interaction complete
						currentState.rm01o2 = 1 #Keys discovered
					else:
						display(brig.feat3interactFail)
				else: #Task completed
					display(brig.feat3interactComplete)
			#Storage
			elif currentState.currRoom == 2:
				display(storage.feat3interactSuccess)
				currentState.rm02f3 = 1 #Update to interaction complete
			#Hallway
			if currentState.currRoom == 3: 
				if currentState.obj3Loc == 99:   #Handle in inv
					display(hallway.feat3interactSuccess)
					currentState.rm03f3 = 1 #Update to interaction complete
					currentState.obj3Loc = 100 #Update handle to permanently used
				elif currentState.obj3Loc == 100:
					display(hallway.feat3interactComplete)
				else:
					display(hallway.feat3interactFail)
			#Observation
			elif currentState.currRoom == 4:
				display(observation.feat3interactSuccess)
				currentState.rm04f3 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				display(examination.feat3interactSuccess)
				currentState.rm05f3 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				display(rum.feat3interactSuccess)
				currentState.rm06f3 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				display(armory.feat3interactSuccess)
				currentState.rm07f3 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat3interactSuccess)
				currentState.rm08f3 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				display(galley.feat3interactSuccess)
				currentState.rm09f3 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				display(topHall.feat3interactSuccess)
				currentState.rm11f3 = 1 #Update to interaction complete
			#Garden
			elif currentState.currRoom == 12:
				display(garden.feat3interactSuccess)
				currentState.rm12f3 = 1 #Update to interaction complete
			#Control
			elif currentState.currRoom == 13:
				display(control.feat3interactSuccess)
				currentState.rm13f3 = 1 #Update to interaction complete
			#Side
			if currentState.currRoom == 14:
				if currentState.rm14f3 == 0: #Not complete
					display(side.feat3interactSuccess)
					currentState.rm14f3 = 1 #Update to interaction complete
					currentState.rm14o1 = 1 #Cryptex discovered 
				else:
					display(side.feat3interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				display(processing.feat3interactSuccess)
				currentState.rm15f3 = 1 #Update to interaction complete

		elif userInput == "8": #Look at object "keys"
			if currentState.obj2Loc ==99: #In inventory
				display(keys.desc)
			else: #Not in inventory
				display(keys.notInInv)

		elif userInput == "9": #Look at feature 4 - DOOR / WOODEN DOOR / CHEST / BARRELS / GUN CASE / WOODEN DOOR / SINK
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f4 == 0: #Before interaction
					display(brig.feat4desc)
				else: #After interaction
					display(brig.feat4interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f4 == 0: #Before interaction
					display(hallway.feat4desc)
				else: #After interaction
					display(hallway.feat4interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f4 == 0: #Before interaction
					display(observation.feat4desc)
				else: #After interaction
					display(observation.feat4interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f4 == 0: #Before interaction
					display(rum.feat4desc)
				else: #After interaction
					display(rum.feat4interactComplete)
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f4 == 0: #Before interaction
					display(armory.feat4desc)
				else: #After interaction
					display(armory.feat4interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f4 == 0: #Before interaction
					display(garrison.feat4desc)
				else: #After interaction
					display(garrison.feat4interactComplete)
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f4 == 0: #Before interaction
					display(galley.feat4desc)
				else: #After interaction
					display(galley.feat4interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f4 == 0: #Before interaction
					display(topHall.feat4desc)
				else: #After interaction
					display(topHall.feat4interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f4 == 0: #Before interaction
					display(garden.feat4desc)
				else: #After interaction
					display(garden.feat4interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f4 == 0: #Before interaction
					display(control.feat4desc)
				else: #After interaction
					display(control.feat4interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f4 == 0: #Before interaction
					display(side.feat4desc)
				else: #After interaction
					display(side.feat4interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f3 == 1: #Crank used and bracelet on
					if currentState.rm15f4 == 0: #Before interaction
						display(processing.feat4desc)
					else: #After interaction
						display(processing.feat4interactComplete)
				else: #The bracelet has not been discovered
					display("You don't have a bracelet.")

		elif userInput == "10": #Interact with feature 4
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f4 == 0: #Not complete
					if currentState.obj2Loc == 99: #Keys
						display(brig.feat4interactSuccess)
						currentState.rm01f4 = 1 #Update to interaction complete
					else:
						display(brig.feat4interactFail)
				else: #Task has been completed (prevents redisplay of action)
					display(brig.feat4interactComplete)
			#Hallway
			elif currentState.currRoom == 3:
				display(hallway.feat4interactSuccess)
				currentState.rm03f4 = 1 #Update to interaction complete
			#Observation
			if currentState.currRoom == 4:
				if currentState.rm04f4 == 0: #Not complete
					if currentState.obj2Loc == 99: #Keys
						display(observation.feat4interactSuccess)
						currentState.rm04f4 = 1 #Update to interaction complete
						currentState.rm04o1 = 1 #Skeleton key discovered
					else:
						display(observation.feat4interactFail)
				else: #Interaction complete
					display(observation.feat4interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				display(rum.feat4interactSuccess)
				currentState.rm06f4 = 1 #Update to interaction complete
				currentState.rm06o1 = 1 #Small Key discovered 
			#Armory
			if currentState.currRoom == 7:
				if currentState.obj5Loc == 99: #Small key
					display(armory.feat4interactSuccess)
					currentState.rm07f4 = 1 #Update to interaction complete
					currentState.rm07o1 = 1 #Gun discovered
				else:
					display(armory.feat4interactFail)
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat4interactSuccess)
				currentState.rm08f4 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				display(galley.feat4interactSuccess)
				currentState.rm09f4 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				display(topHall.feat4interactSuccess)
				currentState.rm11f4 = 1 #Update to interaction complete
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f4 == 0: #Not complete
					if currentState.obj4Loc == 99: 	#If skeleton key in inventory
						display(garden.feat4interactSuccess)
						currentState.rm12f4 = 1 #Update to interaction complete
					else:
						display(garden.feat4interactFail)
				else: #Task completed
					display(garden.feat4interactComplete)
			#Control
			elif currentState.currRoom == 13:
				display(control.feat4interactSuccess)
				currentState.rm13f4 = 1 #Update to interaction complete
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f4 == 0: #Not complete
					display(side.feat4interactSuccess)
					currentState.rm14f4 = 1 #Update to interaction complete
				else:
					display(side.feat4interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f3 == 1: #Crank used and bracelet on
					if currentState.rm15f4 == 0: #If interaction not previously completed
						display(processing.feat4interactSuccess)
						currentState.rm15f4 = 1 #Update to interaction complete
					else:
						display(processing.feat4interactComplete)
				else: #The bracelet has not been discovered
					display("You don't have a bracelet.")

		elif userInput == "11": #General look around room
			if currentState.currRoom == 1:
				display(brig.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 1:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 1:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 1:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 1:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 1:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 1:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 1:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 1:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 1:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 1:
					display(keycard.inRoom)

			elif currentState.currRoom == 2:
				display(storage.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 2:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 2:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 2:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 2:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 2:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 2:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 2:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 2:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 2:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 2:
					display(keycard.inRoom)

			elif currentState.currRoom == 3:
				display(hallway.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 3:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 3:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 3:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 3:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 3:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 3:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 3:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 3:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 3:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 3:
					display(keycard.inRoom)

			elif currentState.currRoom == 4:
				display(observation.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 4:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 4:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 4:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 4:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 4:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 4:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 4:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 4:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 4:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 4:
					display(keycard.inRoom)

			elif currentState.currRoom == 5:
				display(examination.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 5:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 5:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 5:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 5:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 5:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 5:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 5:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 5:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 5:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 5:
					display(keycard.inRoom)

			elif currentState.currRoom == 6:    #Rum
				display(rum.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 6:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 6:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 6:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 6:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 6:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 6:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 6:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 6:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 6:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 6:
					display(keycard.inRoom)

			elif currentState.currRoom == 7:    #Armory
				display(armory.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 7:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 7:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 7:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 7:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 7:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 7:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 7:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 7:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 7:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 7:
					display(keycard.inRoom)

			elif currentState.currRoom == 8:    #Garrison
				display(garrison.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 8:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 8:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 8:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 8:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 8:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 8:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 8:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 8:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 8:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 8:
					display(keycard.inRoom)

			elif currentState.currRoom == 9:    #Galley
				display(galley.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 9:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 9:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 9:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 9:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 9:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 9:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 9:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 9:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 9:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 9:
					display(keycard.inRoom)

			elif currentState.currRoom == 10:    #Ladder
				display(ladder.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 10:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 10:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 10:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 10:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 10:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 10:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 10:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 10:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 10:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 10:
					display(keycard.inRoom)

			elif currentState.currRoom == 11:    #topHall
				display(topHall.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 11:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 11:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 11:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 11:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 11:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 11:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 11:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 11:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 11:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 11:
					display(keycard.inRoom)

			elif currentState.currRoom == 12:    #Garden
				display(garden.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 12:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 12:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 12:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 12:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 12:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 12:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 12:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 12:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 12:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 12:
					display(keycard.inRoom)

			elif currentState.currRoom == 13:    #Control
				display(control.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 13:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 13:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 13:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 13:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 13:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 13:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 13:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 13:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 13:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 13:
					display(keycard.inRoom)

			elif currentState.currRoom == 14:    #Side
				display(side.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 14:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 14:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 14:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 14:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 14:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 14:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 14:
					display(lockpick.inRoom)
				#Object 8 - Cryptex 
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 14:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 14:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 14:
					display(keycard.inRoom)

			elif currentState.currRoom == 15:    #Processing
				display(processing.longDesc)
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 15:
					display(board.inRoom)
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 15:
					display(keys.inRoom)
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 15:
					display(handle.inRoom)
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 15:
					display(skeletonKey.inRoom)
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 15:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 15:
					display(gun.inRoom)
				#Object 7 - Lockpick
				if currentState.rm12o1 == 1 and currentState.obj7Loc == 15:
					display(lockpick.inRoom)
				#Object 8 - Cryptex
				if currentState.rm14o1 == 1 and currentState.obj8Loc == 15:
					display(cryptex.inRoom)
				#Object 9 - Paper clip
				if currentState.paperclipDisc == 1 and currentState.obj9Loc == 15:
					display(paperclip.inRoom)
				#Object 10 - Keycard
				if currentState.keycardDisc == 1 and currentState.obj10Loc == 15:
					display(keycard.inRoom)

		elif userInput == "12": #Take board
			#If object discovered and if player is in the same room as the object
			if currentState.rm01o1 == 1 and currentState.obj1Loc == currentState.currRoom:
				currentState.obj1Loc = 99 #Add board to player inventory
				display(board.take)
			else:
				display(board.notAvail)

		elif userInput == "13": #Take keys
			#If object discovered and if player is in the same room as the object
			if currentState.rm01o2 == 1 and currentState.obj2Loc == currentState.currRoom:
				currentState.obj2Loc = 99 #Add keys to player inventory
				display(keys.take)
			else:
				display(keys.notAvail)

		elif userInput == "14": #Drop board
			if currentState.obj1Loc == 99: #In inventory to drop
				currentState.obj1Loc = currentState.currRoom
				display(board.drop)
			else:
				display(board.notInInv)

		elif userInput == "15": #Drop keys
			if currentState.obj2Loc == 99: #In inventory to drop
				currentState.obj2Loc = currentState.currRoom
				display(keys.drop)
			else:
				display(keys.notInInv)

		elif userInput == "16": #Help
			utils.printHelp(featureDict, itemDict, currentState)

		elif userInput == "17": #Inventory
			print ""
			display("Inventory:")
			inventory = []

			if currentState.obj1Loc == 99:   #Board
				inventory.append(board.name)
			if currentState.obj2Loc == 99:   #Keys
				inventory.append(keys.name)
			if currentState.obj3Loc == 99:   #Handle
				inventory.append(handle.name)
			if currentState.obj4Loc == 99:   #Skeleton Key
				inventory.append(skeletonKey.name)
			if currentState.obj5Loc == 99:   #Small Key
				inventory.append(smallKey.name)
			if currentState.obj6Loc == 99:   #Gun
				inventory.append(gun.name)
			if currentState.obj7Loc == 99:   #Lockpick
				inventory.append(lockpick.name)
			if currentState.obj8Loc == 99:   #Cryptex
				inventory.append(cryptex.name)
			if currentState.obj9Loc == 99:	 #Paper clip
				inventory.append(paperclip.name)
			if currentState.obj10Loc == 99:  #Keycard
				inventory.append(keycard.name)
			if inventory: #{Parsing dev}
				inventoryString = ""
				for thing in inventory:
					if thing == inventory[0]:
						inventoryString = thing
					else:
						inventoryString = inventoryString + ", " + thing
				display(inventoryString)
			else:
				display("You have no items at this time.")
			print ""

		elif userInput == "18": #Look at feature 5 - Brig:null - LADDER / BOTTLES / WOODEN DOOR / METAL DOOR / CANVAS FLAP
			#Brig
			if currentState.currRoom == 1:
				display("Brig feature 5 null")
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f5 == 0: #Before interaction
					display(hallway.feat5desc)
				else: #After interaction
					display(hallway.feat5interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f5 == 0: #Before interaction
					display(observation.feat5desc)
				else: #After interaction
					display(observation.feat5interactComplete)
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f5 == 0: #Before interaction
					display(rum.feat5desc)
				else: #After interaction
					display(rum.feat5interactComplete)
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f5 == 0: #Before interaction
					display(armory.feat5desc)
				else: #After interaction
					display(armory.feat5interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f5 == 0: #Before interaction
					display(garrison.feat5desc)
				else: #After interaction
					display(garrison.feat5interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f5 == 0: #Before interaction
					display(topHall.feat5desc)
				else: #After interaction
					display(topHall.feat5interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f5 == 0: #Before interaction
					display(garden.feat5desc)
				else: #After interaction
					display(garden.feat5interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f5 == 0: #Before interaction
					display(control.feat5desc)
				else: #After interaction
					display(control.feat5interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f5 == 0: #Before interaction
					display(side.feat5desc)
				else: #After interaction
					display(side.feat5interactComplete)
			#Processing
			elif currentState.currRoom == 15:
				if currentState.rm15f5 == 0: #Before interaction
					display(processing.feat5desc)
				else: #After interaction
					display(processing.feat5interactComplete)

		elif userInput == "19": #Interact with feature 5  - LADDER / BOTTLES / WOODEN DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 5 null"
			#Hallway
			elif currentState.currRoom == 3:
				display(hallway.feat5interactSuccess)
				currentState.rm03f5 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				display(observation.feat5interactSuccess)
				currentState.rm04f5 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				display(rum.feat5interactSuccess)
				currentState.rm06f5 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				display(armory.feat5interactSuccess)
				currentState.rm07f5 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat5interactSuccess)
				currentState.rm08f5 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				display(topHall.feat5interactSuccess)
				currentState.rm11f5 = 1 #Update to interaction complete
			#Garden
			elif currentState.currRoom == 12:
				display(garden.feat5interactSuccess)
				currentState.rm12f5 = 1 #Update to interaction complete
			#Control
			elif currentState.currRoom == 13:
				display(control.feat5interactSuccess)
				currentState.rm13f5 = 1 #Update to interaction complete
			#Side
			elif currentState.currRoom == 14:
				display(side.feat5interactSuccess)
				currentState.rm14f5 = 1 #Update to interaction complete
			#Processing
			elif currentState.currRoom == 15:
				display(processing.feat5interactSuccess)
				currentState.rm15f5 = 1 #Update to interaction complete

		elif userInput == "20": #Look at feature 6 - Brig:null  - TRAP DOOR / PAPERS / METAL DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f6 == 0: #Before interaction
					display(hallway.feat6desc)
				else: #After interaction
					display(hallway.feat6interactComplete)
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f6 == 0: #Before interaction
					display(observation.feat6desc)
				else: #After interaction
					display(observation.feat6interactComplete)
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f6 == 0: #Before interaction
					display(garrison.feat6desc)
				else: #After interaction
					display(garrison.feat6interactComplete)
			#topHall
			elif currentState.currRoom == 11:
				if currentState.rm11f6 == 0: #Before interaction
					display(topHall.feat6desc)
				else: #After interaction
					display(topHall.feat6interactComplete)
			#Garden
			elif currentState.currRoom == 12:
				if currentState.rm12f6 == 0: #Before interaction
					display(garden.feat6desc)
				else: #After interaction
					display(garden.feat6interactComplete)
			#Control
			elif currentState.currRoom == 13:
				if currentState.rm13f6 == 0: #Before interaction
					display(control.feat6desc)
				else: #After interaction
					display(control.feat6interactComplete)
			#Side
			elif currentState.currRoom == 14:
				if currentState.rm14f6 == 0: #Before interaction
					display(side.feat6desc)
				else: #After interaction
					display(side.feat6interactComplete)

		elif userInput == "21": #Interact with feature 6
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.obj4Loc == 99:   #Skeleton Key in inv
					display(hallway.feat6interactSuccess)
					currentState.rm03f6 = 1 #Update to interaction complete
				else:
					display(hallway.feat6interactFail)
			#Observation
			elif currentState.currRoom == 4:
				display(observation.feat6interactSuccess)
				currentState.rm04f6 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				display(garrison.feat6interactSuccess)
				currentState.rm08f6 = 1 #Update to interaction complete
			#topHall
			elif currentState.currRoom == 11:
				display(topHall.feat6interactSuccess)
				currentState.rm11f6 = 1 #Update to interaction complete
			#Garden
			elif currentState.currRoom == 12:
				display(garden.feat6interactSuccess)
				currentState.rm12f6 = 1 #Update to interaction complete
			#Control
			elif currentState.currRoom == 13:
				display(control.feat6interactSuccess)
				currentState.rm13f6 = 1 #Update to interaction complete
			#Side
			elif currentState.currRoom == 14:
				if currentState.obj7Loc == 99:   #Lockpick in inv
					display(side.feat6interactSuccess)
					currentState.rm14f6 = 1 #Update to interaction complete
				else:
					display(side.feat6interactFail)

		elif userInput == "22": #GO NORTH
			if currentState.currRoom == 1: #Brig
				if currentState.rm01f4 == 1: #If door unlocked, proceed North into Lower Hallway
					currentState.currRoom = 3 #Updates current user location to ID 3 (Lower Hallway)
				else:
					display(brig.feat4interactFail)  #Else, failure statement

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.north #Updates current user location to ID 5 (Examination Room)

			elif currentState.currRoom == 4: #Observation
				display("You cannot go that way.")

			elif currentState.currRoom == 5: #Examination
				display("You cannot go that way.")
			elif currentState.currRoom == 6: #Rum
				currentState.currRoom = rum.north #Updates current user location to ID 7 (Armory Room)

			elif currentState.currRoom == 7: #Armory
				currentState.currRoom = armory.north #Updates current user location to ID 8 (Garrison)

			elif currentState.currRoom == 8: #Garrison
				currentState.currRoom = garrison.north #Updates current user location to ID 9 (Galley)

			elif currentState.currRoom == 9: #Galley
				display("You cannot go that way.")

			elif currentState.currRoom == 10: #Ladder
				display("You cannot go that way.")

			elif currentState.currRoom == 11: #topHall
				currentState.currRoom = topHall.north #Updates current user location to ID 13 (Control)

			elif currentState.currRoom == 12: #Garden
				display("You cannot go that way.")

			elif currentState.currRoom == 13: #Control
				display("You cannot go that way.")

			elif currentState.currRoom == 14: #Side
				display("You cannot go that way.")

			elif currentState.currRoom == 15: #Processing
				display("You cannot go that way.")

		elif userInput == "23": #GO SOUTH
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.south #Updates current user location to ID 1 (Brig)
				#currentState.currRoom = 1 #Updates current user location to ID 1 (Brig)

			elif currentState.currRoom == 4: #Observation
				display("You cannot go that way.")

			elif currentState.currRoom == 5: #Examination
				currentState.currRoom = examination.south #Updates current user location to ID 3 (Hallway)

			elif currentState.currRoom == 6: #Rum
				display("You cannot go that way.")

			elif currentState.currRoom == 7: #Armory
				currentState.currRoom = armory.south #Updates current user location to ID 6 (Rum)

			elif currentState.currRoom == 8: #Garrison
				currentState.currRoom = garrison.south #Updates current user location to ID 7 (Armory)

			elif currentState.currRoom == 9: #Galley
				currentState.currRoom = galley.south #Updates current user location to ID 8 (Garrison)

			elif currentState.currRoom == 10: #Ladder
				display("You cannot go that way.")

			elif currentState.currRoom == 11: #topHall
				display("You cannot go that way.")

			elif currentState.currRoom == 12: #Garden
				currentState.currRoom = garden.south #Updates current user location to ID 11 (topHall)

			elif currentState.currRoom == 13: #Control
				display("You cannot go that way.")

			elif currentState.currRoom == 14: #Side
				display("You cannot go that way.")

			elif currentState.currRoom == 15: #Processing
				display("You cannot go that way.")

		elif userInput == "24": #GO WEST
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.west #Updates current user location to ID 2 (Storage Room)

			elif currentState.currRoom == 4: #Observation
				currentState.currRoom = observation.west #Updates current user location to ID 3 (Hallway)

			elif currentState.currRoom == 5: #Examination
				display("You cannot go that way.")

			elif currentState.currRoom == 6: #Rum
				display("You cannot go that way.")

			elif currentState.currRoom == 7: #Armory
				display("You cannot go that way.")

			elif currentState.currRoom == 8: #Garrison
				display("You cannot go that way.")

			elif currentState.currRoom == 9: #Galley
				display("You cannot go that way.")

			elif currentState.currRoom == 10: #Ladder
				currentState.currRoom = ladder.west #Updates current user location to ID 8 (Garrison)

			elif currentState.currRoom == 11: #topHall
				if currentState.rm11f2 == 1: #If door unlocked, proceed West into Processing
					currentState.currRoom = topHall.west #Updates current user location to ID 15 (Processing)
				else:
					display(topHall.feat2interactFail)  #Else, failure statement

			elif currentState.currRoom == 12: #Garden
				currentState.currRoom = garden.west #Updates current user location to ID 13 (Control)

			elif currentState.currRoom == 13: #Control
				display("You cannot go that way.")

			elif currentState.currRoom == 14: #Side
				currentState.currRoom = side.west #Updates current user location to ID 12 (Garden)

			elif currentState.currRoom == 15: #Processing
				display("You cannot go that way.")

		elif userInput == "25": #GO EAST
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				currentState.currRoom = storage.east #Updates current user location to ID 3 (Hallway)

			elif currentState.currRoom == 3: #Lower Hallway
				if currentState.rm03f3 == 1: #If door unlocked, proceed North into Lower Hallway
					currentState.currRoom = hallway.east #Updates current user location to ID 4 (Observation)
				else:
					display(hallway.feat3interactFail)  #Else, failure statement

			elif currentState.currRoom == 4: #Observation
				display("You cannot go that way.")

			elif currentState.currRoom == 5: #Examination
				display("You cannot go that way.")

			elif currentState.currRoom == 6: #Rum
				display("You cannot go that way.")

			elif currentState.currRoom == 7: #Armory
				display("You cannot go that way.")

			elif currentState.currRoom == 8: #Garrison
				currentState.currRoom = garrison.east #Updates current user location to ID 10 (Ladder)

			elif currentState.currRoom == 9: #Galley
				display("You cannot go that way.")

			elif currentState.currRoom == 10: #Ladder
				display("You cannot go that way.")

			elif currentState.currRoom == 11: #topHall
				display("You cannot go that way.")

			elif currentState.currRoom == 12: #Garden
				if currentState.rm12f4 == 1: 	#If door unlocked
					currentState.currRoom = garden.east #Updates current user location to ID 14 (Side)
				else:
					display(garden.feat4interactFail)	#Else, failure statement

			elif currentState.currRoom == 13: #Control
				currentState.currRoom = control.east #Updates current user location to ID 12 (Garden)

			elif currentState.currRoom == 14: #Side
				display("You cannot go that way.")

			elif currentState.currRoom == 15: #Processing
				currentState.currRoom = processing.east #Updates current user location to ID 11 (Hallway)

		elif userInput == "26": #GO UP
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				if currentState.rm03f6 == 1: #If trap door unlocked, proceed UP into Rum Room
					currentState.currRoom = hallway.up #Updates current user location to ID 6 (Rum)
				else:
					display(hallway.feat6interactFail)  #Else, failure statement

			elif currentState.currRoom == 4: #Observation
				display("You cannot go that way.")

			elif currentState.currRoom == 5: #Examination
				display("You cannot go that way.")

			elif currentState.currRoom == 6: #Rum
				display("You cannot go that way.")

			elif currentState.currRoom == 7: #Armory
				display("You cannot go that way.")

			elif currentState.currRoom == 8: #Garrison
				display("You cannot go that way.")

			elif currentState.currRoom == 9: #Galley
				display("You cannot go that way.")

			elif currentState.currRoom == 10: #Ladder
				currentState.currRoom = ladder.up #Updates current user location to ID 11 (topHall)

			elif currentState.currRoom == 11: #topHall
				display("You cannot go that way.")

			elif currentState.currRoom == 12: #Garden
				display("You cannot go that way.")

			elif currentState.currRoom == 13: #Control
				display("You cannot go that way.")

			elif currentState.currRoom == 14: #Side
				display("You cannot go that way.")

			elif currentState.currRoom == 15: #Processing
				display("You cannot go that way.")

		elif userInput == "27": #GO DOWN
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				display("You cannot go that way.")

			elif currentState.currRoom == 4: #Observation
				display("You cannot go that way.")

			elif currentState.currRoom == 5: #Examination
				display("You cannot go that way.")

			elif currentState.currRoom == 6: #Rum
				currentState.currRoom = rum.down #Updates current user location to ID 6 (Rum)

			elif currentState.currRoom == 7: #Armory
				display("You cannot go that way.")

			elif currentState.currRoom == 8: #Garrison
				display("You cannot go that way.")

			elif currentState.currRoom == 9: #Galley
				display("You cannot go that way.")

			elif currentState.currRoom == 10: #Ladder
				display("You cannot go that way.")

			elif currentState.currRoom == 11: #topHall
				currentState.currRoom = topHall.down #Updates current user location to ID 10 (Ladder)

			elif currentState.currRoom == 12: #Garden
				display("You cannot go that way.")

			elif currentState.currRoom == 13: #Control
				display("You cannot go that way.")

			elif currentState.currRoom == 14: #Side
				display("You cannot go that way.")

			elif currentState.currRoom == 15: #Processing
				display("You cannot go that way.")

		elif userInput == "28": #Take handle
			#If object discovered and if player is in the same room as the object
			if currentState.rm02o1 == 1 and currentState.obj3Loc == currentState.currRoom:
				currentState.obj3Loc = 99 #Add handle to player inventory
				display(handle.take)
			else:
				display(handle.notAvail)

		elif userInput == "29": #Drop handle
			if currentState.obj3Loc == 99: #In inventory to drop
				currentState.obj3Loc = currentState.currRoom
				display(handle.drop)
			else:
				display(handle.notInInv)

		elif userInput == "30": #Take skeleton key
			#If object discovered and if player is in the same room as the object
			if currentState.rm04o1 == 1 and currentState.obj4Loc == currentState.currRoom:
				currentState.obj4Loc = 99 #Add skeleton key to player inventory
				display(skeletonKey.take)
			else:
				display(skeletonKey.notAvail)

		elif userInput == "31": #Drop skeleton key
			if currentState.obj4Loc == 99: #In inventory to drop
				currentState.obj4Loc = currentState.currRoom
				display(skeletonKey.drop)
			else:
				display(skeletonKey.notInInv)

		elif userInput == "32": #Look at object "handle"
			if currentState.obj3Loc ==99: #In inventory
				display(handle.desc)
			else: #Not in inventory
				display(handle.notInInv)

		elif userInput == "33": #Look at object "skeleton key"
			if currentState.obj4Loc ==99: #In inventory
				display(skeletonKey.desc)
			else: #Not in inventory
				display(skeletonKey.notInInv)

		elif userInput == "34": #Look at object "small key"
			if currentState.obj5Loc ==99: #In inventory
				display(smallKey.desc)
			else: #Not in inventory
				display(smallKey.notInInv)

		elif userInput == "35": #Take small key
			#If object discovered and if player is in the same room as the object
			if currentState.rm06o1 == 1 and currentState.obj5Loc == currentState.currRoom:
				currentState.obj5Loc = 99 #Add board to player inventory
				display(smallKey.take)
			else:
				display(smallKey.notAvail)

		elif userInput == "36": #Drop small key
			if currentState.obj5Loc == 99: #In inventory to drop
				currentState.obj5Loc = currentState.currRoom
				display(smallKey.drop)
			else:
				display(smallKey.notInInv)

		elif userInput == "37": #Look at object "gun"
			if currentState.obj6Loc == 99: #In inventory
				display(gun.desc)
			else: #Not in inventory
				display(gun.notInInv)

		elif userInput == "38": #Take gun
			#If object discovered and if player is in the same room as the object
			if currentState.rm07o1 == 1 and currentState.obj6Loc == currentState.currRoom:
				currentState.obj6Loc = 99 #Add board to player inventory
				display(gun.take)
			else:
				display(gun.notAvail)

		elif userInput == "39": #Drop gun
			if currentState.obj6Loc == 99: #In inventory to drop
				currentState.obj6Loc = currentState.currRoom
				display(gun.drop)
			else:
				display(gun.notInInv)

		elif userInput == "40": #Look at object "lockpick"
			if currentState.obj7Loc == 99: #In inventory
				display(lockpick.desc)
			else: #Not in inventory
				display(lockpick.notInInv)

		elif userInput == "41": #Take lockpick
			#If object discovered and if player is in the same room as the object
			if currentState.rm12o1 == 1 and currentState.obj7Loc == currentState.currRoom:
				currentState.obj7Loc = 99 #Add board to player inventory
				display(lockpick.take)
			else:
				display(lockpick.notAvail)

		elif userInput == "42": #Drop lockpick
			if currentState.obj7Loc == 99: #In inventory to drop
				currentState.obj7Loc = currentState.currRoom
				display(lockpick.drop)
			else:
				display(lockpick.notInInv)

		elif userInput == "43": #Look at object "cryptex"
			if currentState.obj8Loc == 99: #In inventory
				display(cryptex.desc)
			else: #Not in inventory
				display(cryptex.notInInv)

		elif userInput == "44": #Take cryptex
			#If object discovered and if player is in the same room as the object
			if currentState.rm14o1 == 1 and currentState.obj8Loc == currentState.currRoom:
				currentState.obj8Loc = 99 #Add board to player inventory
				display(cryptex.take)
			else:
				display(cryptex.notAvail)

		elif userInput == "45": #Drop cryptex
			if currentState.obj8Loc == 99: #In inventory to drop
				currentState.obj8Loc = currentState.currRoom
				display(cryptex.drop)
			else:
				display(cryptex.notInInv)

		#USE / FIRE GUN 
		elif userInput == "46": #Utilize gun
			if currentState.obj6Loc == 99: #Gun in inventory to use
				display("You hold up the gun and slowly squeeze the trigger. You feel an odd resistance as you squeeze down. Suddenly, the gun explodes with a BANG! It leaves a painful burn mark on your hand. Maybe violence isn't the answer.")
				currentState.obj6Loc = 100 #Update gun to destroyed
				currentState.floatGun = 1 #Update gun tracking variable to 1 (used)
			else:
				display("You don't have a gun.")

		#BEND / TWIST / STRAIGHTEN PAPERCLIP
		elif userInput == "47": #Change paperclip into lockpick 
			if currentState.obj9Loc == 99: #If paperclip in inventory
				display("You take the paper clip and straighten it out.  It'll do as a make shift lockpick! Oops, you dropped it.")
				currentState.obj9Loc = 100 #Update paperclip to permanently used
				currentState.rm12o1 = 1 #Update lockpick discovered
				currentState.obj7Loc = currentState.currRoom #Lockpick falls onto floor of current room
			else:
				display("You don't have a paper clip.")

		#OPEN CRYPTEX
		elif userInput == "48": 
			if currentState.obj8Loc == 99: #If cryptex in inventory
				# If True - successfully passed; False = unchanged, not opened
				if(story.cryptex()):
					print "Cryptex has been opened - set flag" #PENDING
				#END CRYPTEX PUZZLE
			else:
				display(cryptex.notAvail)

		elif userInput == "49": #Look at object "paper clip"
			if currentState.obj9Loc == 99: #In inventory
				display(paperclip.desc)
			else: #Not in inventory
				display(paperclip.notInInv)

		elif userInput == "50": #Take paper clip
			#If object discovered and if player is in the same room as the object
			if currentState.paperclipDisc == 1 and currentState.obj9Loc == currentState.currRoom:
				currentState.obj9Loc = 99 #Add paper clip to player inventory
				display(paperclip.take)
			else:
				display(paperclip.notAvail)

		elif userInput == "51": #Drop paperclip
			if currentState.obj9Loc == 99: #In inventory to drop
				currentState.obj9Loc = currentState.currRoom
				display(paperclip.drop)
			else:
				display(paperclip.notInInv)

		elif userInput == "52": #Look at object "keycard"
			if currentState.obj10Loc == 99: #In inventory
				display(keycard.desc)
			else: #Not in inventory
				display(keycard.notInInv)

		elif userInput == "53": #Take keycard
			#If object discovered and if player is in the same room as the object
			if currentState.keycardDisc == 1 and currentState.obj10Loc == currentState.currRoom:
				currentState.obj10Loc = 99 #Add keycard to player inventory
				display(keycard.take)
			else:
				display(keycard.notAvail)

		elif userInput == "54": #Drop keycard
			if currentState.obj10Loc == 99: #In inventory to drop
				currentState.obj10Loc = currentState.currRoom
				display(keycard.drop)
			else:
				display(keycard.notInInv)

		elif userInput == "99": #Test ending {Parsing dev}
			story.ending(currentState)
			exitGame()

		#else:
		#	display("Invalid input")
		#[END ENGINE]

		elif userInput == "loadgame":

			loadroom = checksaveload.checkLoading()
			if loadroom != "cancel":
				currentState = resume_gamestate(loadroom)
				print ""
				display(rooms[int(currentState.currRoom)].name)
				display(rooms[int(currentState.currRoom)].longDesc)
			
		elif userInput == "savegame":
			saveroom = checksaveload.checkSaving()
			if saveroom != "cancel":
				save_gamestate(saveroom, currentState)
			
		elif userInput in ["quit", "exit"]:
			exitGame()

#[END PLAY GAME]


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
	sys.exit()
#[END EXIT GAME]

#[References]
#ASCII Title Art Generator - http://patorjk.com/software/taag/#p=display&f=Doom&t=Dead%0AIn%0AThe%20%0AWater