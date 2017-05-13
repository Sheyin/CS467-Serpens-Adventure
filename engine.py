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
#import data
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
		print "NEW GAME FILE CREATED"
		
		#PENDING - Load game state with default starting variables {Data dev}
		currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 1, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

	else:
		print "LOAD GAME FILE"
		#PENDING - Load game state with saved variables {Data dev}

	#PENDING - Load room files {Data dev}
	#data.load_rooms() - not working 
	#testID = rooms[1].id
	#print testID - not working, type error
	#brig = rooms[1] - not working, type error


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
	  
		#ENGINE INTERACTIONS BASED ON PARSED USER INPUT
		if userInput == "1":#Look at feature 1 - STRAW / ENTRYWAY MARKINGS / LOCKER / EXAM ENTRYWAY / DOOR
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

			elif userInput == "3": #Look at feature 2 - BENCH / BARRED DOOR / PAPER / TABLE / BARRED WINDOW
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

			elif userInput == "5": #Look at object "board"
			   if currentState.obj1Loc ==99: #In iventory
			      print board.desc
			   else: #Not in inventory
			      print board.notInInv

			elif userInput == "6": #Look at feature 3 - WINDOW / METAL DOOR / DOOR / MIRROR / WINDOW
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

	  	#PEND ADD REST OF ENGINE CODE

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