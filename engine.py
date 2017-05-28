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
	while userInput not in ['New Game', 'New', 'new', 'new game', 'Load Game', 'load game', 'load', 'Load', 'Exit','exit','Quit', 'quit']:
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
		#print "NEW GAME FILE CREATED"
		
		#PENDING - Load game state with default starting variables {Data dev}
		#Initialize gamestate class - NOTE: MODIFIED TO START IN ROOM 6
		currentState = gamestate.GameStateClass(6,   #currentRoom
		  0, #room1
		  0, #room2
		  0, #room3
		  0, #room4
		  0, #room5
		  0, #room6
		  0, #room7
		  0, #room8
		  0, #room9
		  0, #room10
		  99, #item1 - Board
		  99, #item2 - Key
		  99, #item3 - Handle
		  99, #item4 - Skeleton Key
		  6, #item5 - Small Key
		  7, #item6 - Gun
		  0, #rm1f1
		  0, #rm1f2
		  0, #rm1f3
		  0, #rm1f4
		  1, #rm1o1 - Board discovery
		  1, #rm1o2 - Keys discovery
		  0, #rm2f1
		  0, #rm2f2
		  0, #rm2f3
		  1, #rm2o1 - Handle discovery 
		  0, #rm3f1
		  0, #rm3f2
		  0, #rm3f3
		  0, #rm3f4
		  0, #rm3f5
		  0, #rm3f6
		  0, #rm4f1
		  0, #rm4f2
		  0, #rm4f3
		  0, #rm4f4
		  0, #rm4f5
		  0, #rm4f6
		  1, #rm4o1 - Skeleton key discovery
		  0, #rm5f1
		  0, #rm5f2
		  0, #rm5f3
		  0, #rm6f1
		  0, #rm6f2
		  0, #rm6f3
		  0, #rm6f4
		  0, #rm6f5
		  0, #rm6o1 - Small key discovery 
		  0, #rm7f1
		  0, #rm7f2
		  0, #rm7f3
		  0, #rm7f4
		  0, #rm7f5
		  0, #rm7o1 - Gun discovery
		  0, #rm8f1
		  0, #rm8f2
		  0, #rm8f3
		  0, #rm8f4
		  0, #rm8f5
		  0, #rm8f6
		  0, #rm9f1
		  0, #rm9f2
		  0, #rm9f3
		  0, #rm9f4
		  0, #rm10f1
		  0) #rm10f2

	else:
		print "LOAD GAME FILE"
		#PENDING - Load game state with saved variables {Data dev}

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

	#Send room/item info to get format for parsing
	featureList, featureDict, itemDict, roomList = utils.formatRoomData(rooms, objects, currentState.currRoom)

	#While loop repeatedly prompts user for input until user requests to load, save, or quit game
	while userInput not in ['loadgame', 'savegame', 'quit', 'exit']:

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

			userRoom = currentState.currRoom #Update room the user is currently in

		#Parsing helper function
		featureList, featureDict, itemList, roomList = utils.formatRoomData(rooms, objects, currentState.currRoom)	
			
		#Pend input:
		userInput = raw_input (": ")

		#Parse user input and return code for engine action {Parsing Dev}
		userInput = parse.main(userInput, featureList, featureDict, itemDict, roomList)
	  
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

		elif userInput == "2": #Interact with feature 1 
			#Brig
			if currentState.currRoom == 1:
				display(brig.feat1interactSuccess)
				currentState.rm01f1 = 1 #Update to interaction complete
			#Storage
			elif currentState.currRoom == 2:
				if currentState.obj1Loc == 99: #If have board
					display(storage.feat1interactSuccess)
					currentState.rm02f1 = 1 #Update to interaction complete
					currentState.rm02o1 = 1 #Handle discovered
				else:
					display(storage.feat1interactFail)
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

		elif userInput == "4": #Interact with feature 2
			#Brig
			if currentState.currRoom == 1:
				display(brig.feat2interactSuccess)
				currentState.rm01f2 = 1 #Update to interaction complete
				currentState.rm01o1 = 1 #Board discovered
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

		elif userInput == "7": #Interact with feature 3
			#Brig
			if currentState.currRoom == 1:
				if currentState.obj1Loc == 99:

					display(brig.feat3interactSuccess)
					currentState.rm01f3 = 1 #Update to interaction complete
					currentState.rm01o2 = 1 #Keys discovered
				else:
					display(brig.feat3interactFail)
			#Storage
			elif currentState.currRoom == 2:
				display(storage.feat3interactSuccess)
				currentState.rm02f3 = 1 #Update to interaction complete
			#Hallway
			if currentState.currRoom == 3: #NOTE TO CHECK: HANDLE PERMANENTLY USED?
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
			#Garrison
			elif currentState.currRoom == 9:
				display(galley.feat3interactSuccess)
				currentState.rm09f3 = 1 #Update to interaction complete

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

		elif userInput == "10": #Interact with feature 4
			#Brig
			if currentState.currRoom == 1:
				if currentState.obj2Loc == 99: #Keys
					display(brig.feat4interactSuccess)
					currentState.rm01f4 = 1 #Update to interaction complete
				else:
					display(brig.feat4interactFail)
			#Hallway
			elif currentState.currRoom == 3:
				display(hallway.feat4interactSuccess)
				currentState.rm03f4 = 1 #Update to interaction complete
			#Observation
			if currentState.currRoom == 4:
				if currentState.obj2Loc == 99: #Keys
					display(observation.feat4interactSuccess)
					currentState.rm04f4 = 1 #Update to interaction complete
					currentState.rm04o1 = 1 #Skeleton key discovered
				else:
					display(observation.feat4interactFail)
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
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 1:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 1:
					display(gun.inRoom)

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
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 2:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 2:
					display(gun.inRoom)

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
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 3:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 3:
					display(gun.inRoom)

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
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 4:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 4:
					display(gun.inRoom)

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
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 5:
					display(smallKey.inRoom)
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 5:
					display(gun.inRoom)

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

			elif currentState.currRoom == 10:    #Ladder
				display(galley.longDesc)
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
			utils.printHelp(featureDict, itemDict)

		elif userInput == "17": #Inventory
			print ""
			display("Inventory:")
			if currentState.obj1Loc == 99:   #Board
				display(board.name)
			if currentState.obj2Loc == 99:   #Keys
				display(keys.name)
			if currentState.obj3Loc == 99:   #Handle
				display(handle.name)
			if currentState.obj4Loc == 99:   #Skeleton Key
				display(skeletonKey.name)
			if currentState.obj5Loc == 99:   #Small Key
				display(smallKey.name)
			if currentState.obj6Loc == 99:   #Gun
				display(gun.name)
			print ""

		elif userInput == "18": #Look at feature 5 - Brig:null - LADDER / BOTTLES / WOODEN DOOR / METAL DOOR / CANVAS FLAP
			#Brig
			if currentState.currRoom == 1:
				display("Brig feature 5 null")
				#if currentState.rm01f4 == 0: #Before interaction
				#   display(brig.feat4desc)
				#else: #After interaction
				#   display(brig.feat4interactComplete)
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

		elif userInput == "19": #Interact with feature 5  - LADDER / BOTTLES / WOODEN DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 5 null"
				#if currentState.obj2Loc == 99: #Keys
				#   display(brig.feat4interactSuccess)
				#   currentState.rm01f4 = 1 #Update to interaction complete
				#else:
				#   display(brig.feat4interactFail)
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

		elif userInput == "20": #Look at feature 6 - Brig:null  - TRAP DOOR / PAPERS / METAL DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
				#if currentState.rm01f4 == 0: #Before interaction
				#   display(brig.feat4desc)
				#else: #After interaction
				#   display(brig.feat4interactComplete)
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
					display(armory.feat6desc)
				else: #After interaction
					display(armory.feat6interactComplete)

		elif userInput == "21": #Interact with feature 6
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
				#if currentState.obj2Loc == 99: #Keys
				#   display(brig.feat4interactSuccess)
				#   currentState.rm01f4 = 1 #Update to interaction complete
				#else:
				#   display(brig.feat4interactFail)
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
			#Armory
			elif currentState.currRoom == 8:
				display(armory.feat6interactSuccess)
				currentState.rm08f6 = 1 #Update to interaction complete

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
				print "You cannot go that way."

			elif currentState.currRoom == 10: #Ladder
				print "You cannot go that way."

		elif userInput == "23": #GO SOUTH
			if currentState.currRoom == 1: #Brig
				print "You cannot go that way."

			elif currentState.currRoom == 2: #Storage
				print "You cannot go that way."

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.south #Updates current user location to ID 1 (Brig)
				#currentState.currRoom = 1 #Updates current user location to ID 1 (Brig)

			elif currentState.currRoom == 4: #Observation
				print "You cannot go that way."

			elif currentState.currRoom == 5: #Examination
				currentState.currRoom = examination.south #Updates current user location to ID 3 (Hallway)

			elif currentState.currRoom == 6: #Rum
				print "You cannot go that way."

			elif currentState.currRoom == 7: #Armory
				currentState.currRoom = armory.south #Updates current user location to ID 6 (Rum)

			elif currentState.currRoom == 8: #Garrison
				currentState.currRoom = garrison.south #Updates current user location to ID 7 (Armory)

			elif currentState.currRoom == 9: #Galley
				currentState.currRoom = galley.south #Updates current user location to ID 8 (Garrison)

			elif currentState.currRoom == 10: #Ladder
				print "You cannot go that way."

		elif userInput == "24": #GO WEST
			if currentState.currRoom == 1: #Brig
				print "You cannot go that way."

			elif currentState.currRoom == 2: #Storage
				print "You cannot go that way."

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.west #Updates current user location to ID 2 (Storage Room)

			elif currentState.currRoom == 4: #Observation
				currentState.currRoom = observation.west #Updates current user location to ID 3 (Hallway)

			elif currentState.currRoom == 5: #Examination
				print "You cannot go that way."

			elif currentState.currRoom == 6: #Rum
				print "You cannot go that way."

			elif currentState.currRoom == 7: #Armory
				print "You cannot go that way."

			elif currentState.currRoom == 8: #Garrison
				print "You cannot go that way."

			elif currentState.currRoom == 9: #Galley
				print "You cannot go that way."

			elif currentState.currRoom == 10: #Ladder
				currentState.currRoom = ladder.west #Updates current user location to ID 8 (Garrison)

		elif userInput == "25": #GO EAST
			if currentState.currRoom == 1: #Brig
				print "You cannot go that way."

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

		elif userInput == "26": #GO UP
			if currentState.currRoom == 1: #Brig
				display("You cannot go that way.")

			elif currentState.currRoom == 2: #Storage
				display("You cannot go that way.")

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.up #Updates current user location to ID 6 (Rum)

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
				display("UPPER LEVEL")
				currentState.currRoom = ladder.up #Updates current user location to ID 11 (**PENDING**)

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

		else:
			display("Invalid input")
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