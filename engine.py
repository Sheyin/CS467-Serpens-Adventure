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

	#Send room/item info to get format for parsing
	featureList, featureDict, itemDict, roomList = utils.formatRoomData(rooms, objects, currentState.currRoom)

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

			elif currentState.currRoom == 6:    #Rum
				if currentState.rm06vis == 0: 
				   print rum.longDesc
				   currentState.rm06vis = 1 #Update to visited
				else:
				   print rum.shortDesc

			elif currentState.currRoom == 7:    #Armory
				if currentState.rm07vis == 0: 
				   print armory.longDesc
				   currentState.rm07vis = 1 #Update to visited
				else:
				   print armory.shortDesc

			elif currentState.currRoom == 8:    #Garrison
				if currentState.rm08vis == 0: 
				   print garrison.longDesc
				   currentState.rm08vis = 1 #Update to visited
				else:
				   print garrison.shortDesc

			elif currentState.currRoom == 9:    #Galley
				if currentState.rm09vis == 0: 
				   print galley.longDesc
				   currentState.rm09vis = 1 #Update to visited
				else:
				   print galley.shortDesc

			elif currentState.currRoom == 10:    #Ladder
				if currentState.rm10vis == 0: 
				   print ladder.longDesc
				   currentState.rm10vis = 1 #Update to visited
				else:
				   print ladder.shortDesc

			userRoom = currentState.currRoom #Update room the user is currently in

		#Pend input:
		userInput = raw_input (": ")

		#Parse user input and return code for engine action {Parsing Dev}
		userInput = parse.main(userInput, featureList, featureDict, itemDict, roomList)
	  
		#ENGINE INTERACTIONS BASED ON PARSED USER INPUT
		if userInput == "1":#Look at feature 1 - STRAW / ENTRYWAY MARKINGS / LOCKER / EXAM ENTRYWAY / DOOR / BOTTLE / GUN CABINET / BUNKS / CANVAS FLAP / LADDER
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f1 == 0: #Before interaction
					print brig.feat1desc 
				else: #After interaction
					print brig.feat1interactComplete
			#Storage
			elif currentState.currRoom == 2:
				if currentState.rm02f1 == 0: #Before interaction
					print storage.feat1desc 
				else: #After interaction
					print storage.feat1interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f1 == 0: #Before interaction
					print hallway.feat1desc 
				else: #After interaction
					print hallway.feat1interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f1 == 0: #Before interaction
					print observation.feat1desc 
				else: #After interaction
					print observation.feat1interactComplete
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f1 == 0: #Before interaction
					print examination.feat1desc 
				else: #After interaction
					print examination.feat1interactComplete
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f1 == 0: #Before interaction
					print rum.feat1desc 
				else: #After interaction
					print rum.feat1interactComplete
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f1 == 0: #Before interaction
					print armory.feat1desc 
				else: #After interaction
					print armory.feat1interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f1 == 0: #Before interaction
					print garrison.feat1desc 
				else: #After interaction
					print garrison.feat1interactComplete
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f1 == 0: #Before interaction
					print galley.feat1desc 
				else: #After interaction
					print galley.feat1interactComplete
			#Ladder
			elif currentState.currRoom == 10:
				if currentState.rm10f1 == 0: #Before interaction
					print ladder.feat1desc 
				else: #After interaction
					print ladder.feat1interactComplete

		elif userInput == "2": #Interact with feature 1 
			#Brig
			if currentState.currRoom == 1:
				print brig.feat1interactSuccess
				currentState.rm01f1 = 1 #Update to interaction complete
			#Storage
			elif currentState.currRoom == 2:
				if currentState.obj1Loc == 99: #If have board
					print storage.feat1interactSuccess
					currentState.rm02f1 = 1 #Update to interaction complete
					currentState.rm02o1 = 1 #Handle discovered
				else:
					print storage.feat1interactFail
			#Hallway
			elif currentState.currRoom == 3:
				print hallway.feat1interactSuccess
				currentState.rm03f1 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				print observation.feat1interactSuccess
				currentState.rm04f1 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				print examination.feat1interactSuccess
				currentState.rm05f1 = 1 #Update to interaction complete
			#Rum 
			elif currentState.currRoom == 6:
				print rum.feat1interactSuccess
				currentState.rm06f1 = 1 #Update to interaction complete
			#Armory 
			elif currentState.currRoom == 7:
				print armory.feat1interactSuccess
				currentState.rm07f1 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				print garrison.feat1interactSuccess
				currentState.rm08f1 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				print galley.feat1interactSuccess
				currentState.rm09f1 = 1 #Update to interaction complete
			#Ladder
			elif currentState.currRoom == 10:
				print ladder.feat1interactSuccess
				currentState.rm10f1 = 1 #Update to interaction complete

		elif userInput == "3": #Look at feature 2 - BENCH / BARRED DOOR / PAPER / TABLE / BARRED WINDOW / LAMP / WOODEN DOOR / TABLE / TRASH CAN / WOODEN DOOR
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f2 == 0: #Before interaction
					print brig.feat2desc 
				else: #After interaction
					print brig.feat2interactComplete
			#Storage
			elif currentState.currRoom == 2:
				if currentState.rm02f2 == 0: #Before interaction
					print storage.feat2desc 
				else: #After interaction
					print storage.feat2interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f2 == 0: #Before interaction
					print hallway.feat2desc 
				else: #After interaction
					print hallway.feat2interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f2 == 0: #Before interaction
					print observation.feat2desc 
				else: #After interaction
					print observation.feat2interactComplete
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f2 == 0: #Before interaction
					 print examination.feat2desc 
				else: #After interaction
					 print examination.feat2interactComplete
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f2 == 0: #Before interaction
					print rum.feat2desc 
				else: #After interaction
					print rum.feat2interactComplete
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f2 == 0: #Before interaction
					print armory.feat2desc 
				else: #After interaction
					print armory.feat2interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f2 == 0: #Before interaction
					print garrison.feat2desc 
				else: #After interaction
					print garrison.feat2interactComplete
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f2 == 0: #Before interaction
					print galley.feat2desc 
				else: #After interaction
					print galley.feat2interactComplete
			#Ladder
			elif currentState.currRoom == 10:
				if currentState.rm10f2 == 0: #Before interaction
					print ladder.feat2desc 
				else: #After interaction
					print ladder.feat2interactComplete

		elif userInput == "4": #Interact with feature 2
			#Brig
			if currentState.currRoom == 1:
				print brig.feat2interactSuccess
				currentState.rm01f2 = 1 #Update to interaction complete
				currentState.rm01o1 = 1 #Board discovered
			#Storage
			elif currentState.currRoom == 2:
				print storage.feat2interactSuccess
				currentState.rm02f2 = 1 #Update to interaction complete
			#Hallway
			elif currentState.currRoom == 3:
				print hallway.feat2interactSuccess
				currentState.rm03f2 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				print observation.feat2interactSuccess
				currentState.rm04f2 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				print examination.feat2interactSuccess
				currentState.rm05f2 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				print rum.feat2interactSuccess
				currentState.rm06f2 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				print armory.feat2interactSuccess
				currentState.rm07f2 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				print garrison.feat2interactSuccess
				currentState.rm08f2 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				print galley.feat2interactSuccess
				currentState.rm09f2 = 1 #Update to interaction complete
			#Ladder
			elif currentState.currRoom == 10:
				print ladder.feat2interactSuccess
				currentState.rm10f2 = 1 #Update to interaction complete

		elif userInput == "5": #Look at object "board"
			if currentState.obj1Loc ==99: #In iventory
				print board.desc
			else: #Not in inventory
				print board.notInInv 

		elif userInput == "6": #Look at feature 3 - WINDOW / METAL DOOR / DOOR / MIRROR / WINDOW / TRAP DOOR / LOCKER / PHOTOGRAPH / STOVE
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f3 == 0: #Before interaction
					print brig.feat3desc 
				else: #After interaction
					print brig.feat3interactComplete
			#Storage
			if currentState.currRoom == 2:
				if currentState.rm02f3 == 0: #Before interaction
					print storage.feat3desc 
				else: #After interaction
					print storage.feat3interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f3 == 0: #Before interaction
					print hallway.feat3desc 
				else: #After interaction
					print hallway.feat3interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f3 == 0: #Before interaction
					print observation.feat3desc 
				else: #After interaction
					print observation.feat3interactComplete
			#Examination
			elif currentState.currRoom == 5:
				if currentState.rm05f3 == 0: #Before interaction
					print examination.feat3desc 
				else: #After interaction
					print examination.feat3interactComplete
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f3 == 0: #Before interaction
					print rum.feat3desc 
				else: #After interaction
					print rum.feat3interactComplete
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f3 == 0: #Before interaction
					print armory.feat3desc 
				else: #After interaction
					print armory.feat3interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f3 == 0: #Before interaction
					print garrison.feat3desc 
				else: #After interaction
					print garrison.feat3interactComplete
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f3 == 0: #Before interaction
					print galley.feat3desc 
				else: #After interaction
					print galley.feat3interactComplete

		elif userInput == "7": #Interact with feature 3
			#Brig
			if currentState.currRoom == 1:
				if currentState.obj1Loc == 99:

					print brig.feat3interactSuccess
					currentState.rm01f3 = 1 #Update to interaction complete
					currentState.rm01o2 = 1 #Keys discovered
				else:
					print brig.feat3interactFail
			#Storage
			elif currentState.currRoom == 2:
				print storage.feat3interactSuccess
				currentState.rm02f3 = 1 #Update to interaction complete
			#Hallway
			if currentState.currRoom == 3: #NOTE TO CHECK: HANDLE PERMANENTLY USED?
				if currentState.obj3Loc == 99:   #Handle in inv
					print hallway.feat3interactSuccess
					currentState.rm03f3 = 1 #Update to interaction complete
					currentState.obj3Loc = 100 #Update handle to permanently used
				elif currentState.obj3Loc == 100:
					print hallway.feat3interactComplete
				else:
					print hallway.feat3interactFail
			#Observation
			elif currentState.currRoom == 4:
				print observation.feat3interactSuccess
				currentState.rm04f3 = 1 #Update to interaction complete
			#Examination
			elif currentState.currRoom == 5:
				print examination.feat3interactSuccess
				currentState.rm05f3 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				print rum.feat3interactSuccess
				currentState.rm06f3 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				print armory.feat3interactSuccess
				currentState.rm07f3 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				print garrison.feat3interactSuccess
				currentState.rm08f3 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 9:
				print galley.feat3interactSuccess
				currentState.rm09f3 = 1 #Update to interaction complete

		elif userInput == "8": #Look at object "keys"
			if currentState.obj2Loc ==99: #In inventory
				print keys.desc
			else: #Not in inventory
				print keys.notInInv

		elif userInput == "9": #Look at feature 4 - DOOR / WOODEN DOOR / CHEST / BARRELS / GUN CASE / WOODEN DOOR / SINK
			#Brig
			if currentState.currRoom == 1:
				if currentState.rm01f4 == 0: #Before interaction
					print brig.feat4desc 
				else: #After interaction
					print brig.feat4interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f4 == 0: #Before interaction
					print hallway.feat4desc 
				else: #After interaction
					print hallway.feat4interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f4 == 0: #Before interaction
					print observation.feat4desc 
				else: #After interaction
					print observation.feat4interactComplete
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f4 == 0: #Before interaction
					print rum.feat4desc 
				else: #After interaction
					print rum.feat4interactComplete
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f4 == 0: #Before interaction
					print armory.feat4desc 
				else: #After interaction
					print armory.feat4interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f4 == 0: #Before interaction
					print garrison.feat4desc 
				else: #After interaction
					print garrison.feat4interactComplete
			#Galley
			elif currentState.currRoom == 9:
				if currentState.rm09f4 == 0: #Before interaction
					print galley.feat4desc 
				else: #After interaction
					print galley.feat4interactComplete

		elif userInput == "10": #Interact with feature 4
			#Brig
			if currentState.currRoom == 1:
				if currentState.obj2Loc == 99: #Keys
					print brig.feat4interactSuccess
					currentState.rm01f4 = 1 #Update to interaction complete
				else:
					print brig.feat4interactFail
			#Hallway
			elif currentState.currRoom == 3:
				print hallway.feat4interactSuccess
				currentState.rm03f4 = 1 #Update to interaction complete
			#Observation
			if currentState.currRoom == 4:
				if currentState.obj2Loc == 99: #Keys
					print observation.feat4interactSuccess
					currentState.rm04f4 = 1 #Update to interaction complete
					currentState.rm04o1 = 1 #Skeleton key discovered
				else:
					print observation.feat4interactFail
			#Rum
			elif currentState.currRoom == 6:
				print rum.feat4interactSuccess
				currentState.rm06f4 = 1 #Update to interaction complete
				currentState.rm06o1 = 1 #Small Key discovered 
			#Armory
			if currentState.currRoom == 7:
				if currentState.obj5Loc == 99: #Small key
					print armory.feat4interactSuccess
					currentState.rm07f4 = 1 #Update to interaction complete
					currentState.rm07o1 = 1 #Gun discovered
				else:
					print armory.feat4interactFail
			#Garrison
			elif currentState.currRoom == 8:
				print garrison.feat4interactSuccess
				currentState.rm08f4 = 1 #Update to interaction complete
			#Galley
			elif currentState.currRoom == 9:
				print galley.feat4interactSuccess
				currentState.rm09f4 = 1 #Update to interaction complete

		elif userInput == "11": #General look around room
			if currentState.currRoom == 1:
				print brig.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 1:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 1:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 1:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 1:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 1:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 1:
					print gun.inRoom

			elif currentState.currRoom == 2:
				print storage.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 2:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 2:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 2:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 2:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 2:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 2:
					print gun.inRoom

			elif currentState.currRoom == 3:
				print hallway.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 3:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 3:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 3:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 3:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 3:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 3:
					print gun.inRoom

			elif currentState.currRoom == 4:
				print observation.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 4:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 4:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 4:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 4:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 4:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 4:
					print gun.inRoom

			elif currentState.currRoom == 5:
				print examination.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 5:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 5:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 5:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 5:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm05o1 == 1 and currentState.obj5Loc == 5:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 5:
					print gun.inRoom

			elif currentState.currRoom == 6:    #Rum
				print rum.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 6:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 6:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 6:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 6:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 6:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 6:
					print gun.inRoom

			elif currentState.currRoom == 7:    #Armory
				print armory.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 7:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 7:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 7:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 7:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 7:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 7:
					print gun.inRoom

			elif currentState.currRoom == 8:    #Garrison
				print garrison.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 8:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 8:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 8:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 8:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 8:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 8:
					print gun.inRoom

			elif currentState.currRoom == 9:    #Galley
				print galley.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 9:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 9:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 9:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 9:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 9:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 9:
					print gun.inRoom

			elif currentState.currRoom == 10:    #Ladder
				print galley.longDesc
				#Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
				#Object 1 - board
				if currentState.rm01o1 == 1 and currentState.obj1Loc == 10:
					print board.inRoom
				#Object 2 - keys
				if currentState.rm01o2 == 1 and currentState.obj2Loc == 10:
					print keys.inRoom
				#Object 3 - handle
				if currentState.rm02o1 == 1 and currentState.obj3Loc == 10:
					print handle.inRoom
				#Object 4 - skeleton key
				if currentState.rm04o1 == 1 and currentState.obj4Loc == 10:
					print skeletonKey.inRoom
				#Object 5 - small key
				if currentState.rm06o1 == 1 and currentState.obj5Loc == 10:
					print smallKey.inRoom
				#Object 6 - Gun
				if currentState.rm07o1 == 1 and currentState.obj6Loc == 10:
					print gun.inRoom

		elif userInput == "12": #Take board
			#If object discovered and if player is in the same room as the object
			if currentState.rm01o1 == 1 and currentState.obj1Loc == currentState.currRoom:
				currentState.obj1Loc = 99 #Add board to player inventory
				print board.take
			else:
				print board.notAvail

		elif userInput == "13": #Take keys
			#If object discovered and if player is in the same room as the object
			if currentState.rm01o2 == 1 and currentState.obj2Loc == currentState.currRoom:
				currentState.obj2Loc = 99 #Add keys to player inventory
				print keys.take
			else:
				print keys.notAvail

		elif userInput == "14": #Drop board
			if currentState.obj1Loc == 99: #In inventory to drop
				currentState.obj1Loc = currentState.currRoom
				print board.drop
			else:
				print board.notInInv

		elif userInput == "15": #Drop keys
			if currentState.obj2Loc == 99: #In inventory to drop
				currentState.obj2Loc = currentState.currRoom
				print keys.drop
			else:
				print keys.notInInv

		elif userInput == "16": #Help
			print "HELPFUL TIPS:"
			print "Take a closer look at the room's features.  Sometimes you may need to examine a detail on a feature even more closely."
			print "Don't forget to take (pick up) items after you've revealed them."
			print "\nPossible items: " + str(itemDict.keys())
			print "Possible features and actions: " 
			for feature in featureList:
				print str(feature) + ": " + str(parse.getActions(feature, featureDict))

		elif userInput == "17": #Inventory
			print ""
			print "Inventory:"
			if currentState.obj1Loc == 99:   #Board
				print board.name
			if currentState.obj2Loc == 99:   #Keys
				print keys.name
			if currentState.obj3Loc == 99:   #Handle
				print handle.name
			if currentState.obj4Loc == 99:   #Skeleton Key
				print skeletonKey.name
			if currentState.obj5Loc == 99:   #Small Key
				print smallKey.name
			if currentState.obj6Loc == 99:   #Gun
				print gun.name
			print ""

		elif userInput == "18": #Look at feature 5 - Brig:null - LADDER / BOTTLES / WOODEN DOOR / METAL DOOR / CANVAS FLAP
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 5 null"
				#if currentState.rm01f4 == 0: #Before interaction
				#   print brig.feat4desc 
				#else: #After interaction
				#   print brig.feat4interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f5 == 0: #Before interaction
					print hallway.feat5desc 
				else: #After interaction
					print hallway.feat5interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f5 == 0: #Before interaction
					print observation.feat5desc 
				else: #After interaction
					print observation.feat5interactComplete
			#Rum
			elif currentState.currRoom == 6:
				if currentState.rm06f5 == 0: #Before interaction
					print rum.feat5desc 
				else: #After interaction
					print rum.feat5interactComplete
			#Armory
			elif currentState.currRoom == 7:
				if currentState.rm07f5 == 0: #Before interaction
					print armory.feat5desc 
				else: #After interaction
					print armory.feat5interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f5 == 0: #Before interaction
					print garrison.feat5desc 
				else: #After interaction
					print garrison.feat5interactComplete

		elif userInput == "19": #Interact with feature 5  - LADDER / BOTTLES / WOODEN DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 5 null"
				#if currentState.obj2Loc == 99: #Keys
				#   print brig.feat4interactSuccess
				#   currentState.rm01f4 = 1 #Update to interaction complete
				#else:
				#   print brig.feat4interactFail
			#Hallway
			elif currentState.currRoom == 3:
				print hallway.feat5interactSuccess
				currentState.rm03f5 = 1 #Update to interaction complete
			#Observation
			elif currentState.currRoom == 4:
				print observation.feat5interactSuccess
				currentState.rm04f5 = 1 #Update to interaction complete
			#Rum
			elif currentState.currRoom == 6:
				print rum.feat5interactSuccess
				currentState.rm06f5 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 7:
				print armory.feat5interactSuccess
				currentState.rm07f5 = 1 #Update to interaction complete
			#Garrison
			elif currentState.currRoom == 8:
				print garrison.feat5interactSuccess
				currentState.rm08f5 = 1 #Update to interaction complete

		elif userInput == "20": #Look at feature 6 - Brig:null  - TRAP DOOR / PAPERS / METAL DOOR
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
				#if currentState.rm01f4 == 0: #Before interaction
				#   print brig.feat4desc 
				#else: #After interaction
				#   print brig.feat4interactComplete
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.rm03f6 == 0: #Before interaction
					print hallway.feat6desc 
				else: #After interaction
					print hallway.feat6interactComplete
			#Observation
			elif currentState.currRoom == 4:
				if currentState.rm04f6 == 0: #Before interaction
					print observation.feat6desc 
				else: #After interaction
					print observation.feat6interactComplete
			#Garrison
			elif currentState.currRoom == 8:
				if currentState.rm08f6 == 0: #Before interaction
					print armory.feat6desc 
				else: #After interaction
					print armory.feat6interactComplete

		elif userInput == "21": #Interact with feature 6
			#Brig
			if currentState.currRoom == 1:
				print "Brig feature 6 null"
				#if currentState.obj2Loc == 99: #Keys
				#   print brig.feat4interactSuccess
				#   currentState.rm01f4 = 1 #Update to interaction complete
				#else:
				#   print brig.feat4interactFail
			#Hallway
			elif currentState.currRoom == 3:
				if currentState.obj4Loc == 99:   #Skeleton Key in inv
					print hallway.feat6interactSuccess
					currentState.rm03f6 = 1 #Update to interaction complete
				else:
					print hallway.feat6interactFail
			#Observation
			elif currentState.currRoom == 4:
				print observation.feat6interactSuccess
				currentState.rm04f6 = 1 #Update to interaction complete
			#Armory
			elif currentState.currRoom == 8:
				print armory.feat6interactSuccess
				currentState.rm08f6 = 1 #Update to interaction complete

		elif userInput == "22": #GO NORTH
			if currentState.currRoom == 1: #Brig
				if currentState.rm01f4 == 1: #If door unlocked, proceed North into Lower Hallway
					currentState.currRoom = 3 #Updates current user location to ID 3 (Lower Hallway)
				else:
					print brig.feat4interactFail  #Else, failure statement

			elif currentState.currRoom == 2: #Storage
				print "You cannot go that way."

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.north #Updates current user location to ID 5 (Examination Room)

			elif currentState.currRoom == 4: #Observation
				print "You cannot go that way."

			elif currentState.currRoom == 5: #Examination
				print "You cannot go that way."
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
					print hallway.feat3interactFail  #Else, failure statement

			elif currentState.currRoom == 4: #Observation
				print "You cannot go that way."

			elif currentState.currRoom == 5: #Examination
				print "You cannot go that way."

			elif currentState.currRoom == 6: #Rum
				print "You cannot go that way."

			elif currentState.currRoom == 7: #Armory
				print "You cannot go that way."

			elif currentState.currRoom == 8: #Garrison
				currentState.currRoom = garrison.east #Updates current user location to ID 10 (Ladder)

			elif currentState.currRoom == 9: #Galley
				print "You cannot go that way."

			elif currentState.currRoom == 10: #Ladder
				print "You cannot go that way."

		elif userInput == "26": #GO UP
			if currentState.currRoom == 1: #Brig
				print "You cannot go that way."

			elif currentState.currRoom == 2: #Storage
				print "You cannot go that way."

			elif currentState.currRoom == 3: #Lower Hallway
				currentState.currRoom = hallway.up #Updates current user location to ID 6 (Rum)

			elif currentState.currRoom == 4: #Observation
				print "You cannot go that way."

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
				print "UPPER LEVEL"
				currentState.currRoom = ladder.up #Updates current user location to ID 11 (**PENDING**)

		elif userInput == "27": #GO DOWN
			if currentState.currRoom == 1: #Brig
				print "You cannot go that way."

			elif currentState.currRoom == 2: #Storage
				print "You cannot go that way."

			elif currentState.currRoom == 3: #Lower Hallway
				print "You cannot go that way."

			elif currentState.currRoom == 4: #Observation
				print "You cannot go that way."

			elif currentState.currRoom == 5: #Examination
				print "You cannot go that way."

			elif currentState.currRoom == 6: #Rum
				currentState.currRoom = rum.down #Updates current user location to ID 6 (Rum)

			elif currentState.currRoom == 7: #Armory
				print "You cannot go that way."

			elif currentState.currRoom == 8: #Garrison
				print "You cannot go that way."

			elif currentState.currRoom == 9: #Galley
				print "You cannot go that way."

			elif currentState.currRoom == 10: #Ladder
				print "You cannot go that way."

		elif userInput == "28": #Take handle
			#If object discovered and if player is in the same room as the object
			if currentState.rm02o1 == 1 and currentState.obj3Loc == currentState.currRoom:
				currentState.obj3Loc = 99 #Add handle to player inventory
				print handle.take
			else:
				print handle.notAvail

		elif userInput == "29": #Drop handle
			if currentState.obj3Loc == 99: #In inventory to drop
				currentState.obj3Loc = currentState.currRoom
				print handle.drop
			else:
				print handle.notInInv

		elif userInput == "30": #Take skeleton key
			#If object discovered and if player is in the same room as the object
			if currentState.rm04o1 == 1 and currentState.obj4Loc == currentState.currRoom:
				currentState.obj4Loc = 99 #Add skeleton key to player inventory
				print skeletonKey.take
			else:
				print skeletonKey.notAvail

		elif userInput == "31": #Drop skeleton key
			if currentState.obj4Loc == 99: #In inventory to drop
				currentState.obj4Loc = currentState.currRoom
				print skeletonKey.drop
			else:
				print skeletonKey.notInInv

		elif userInput == "32": #Look at object "handle"
			if currentState.obj3Loc ==99: #In inventory
				print handle.desc
			else: #Not in inventory
				print handle.notInInv 

		elif userInput == "33": #Look at object "skeleton key"
			if currentState.obj4Loc ==99: #In inventory
				print skeletonKey.desc
			else: #Not in inventory
				print skeletonKey.notInInv 

		elif userInput == "34": #Look at object "small key"
			if currentState.obj5Loc ==99: #In inventory
				print smallKey.desc
			else: #Not in inventory
				print smallKey.notInInv 

		elif userInput == "35": #Take small key
			#If object discovered and if player is in the same room as the object
			if currentState.rm06o1 == 1 and currentState.obj5Loc == currentState.currRoom:
				currentState.obj5Loc = 99 #Add board to player inventory
				print smallKey.take
			else:
				print smallKey.notAvail

		elif userInput == "36": #Drop small key
			if currentState.obj5Loc == 99: #In inventory to drop
				currentState.obj5Loc = currentState.currRoom
				print smallKey.drop
			else:
				print smallKey.notInInv

		elif userInput == "37": #Look at object "gun"
			if currentState.obj6Loc == 99: #In inventory
				print gun.desc
			else: #Not in inventory
				print gun.notInInv 

		elif userInput == "38": #Take gun
			#If object discovered and if player is in the same room as the object
			if currentState.rm07o1 == 1 and currentState.obj6Loc == currentState.currRoom:
				currentState.obj6Loc = 99 #Add board to player inventory
				print gun.take
			else:
				print gun.notAvail

		elif userInput == "39": #Drop gun
			if currentState.obj6Loc == 99: #In inventory to drop
				currentState.obj6Loc = currentState.currRoom
				print gun.drop
			else:
				print gun.notInInv

		else:
			print "Invalid input"
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