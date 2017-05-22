# Engine Test
# Handles testing of engine components 

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import engine
import room
import objectC
import gamestate
import parse
import data
from data import *
import utils
#[END IMPORTS]

#[BEGIN SPECIFY ROOM TESTING]
def specifyRoomTest(myRoom):
   print ""
   print "Specify Room Testing"
   print "Starting Point Room " + myRoom
   print ""

#[END SPECIFY ROOM TESTING]

#[BEGIN FINAL LEVEL TESTING]
def finalLevelTest():
   print ""
   print "Final Level Testing"
   print ""

   #Initial variables
   userInput = "default"   #Default message for user input
   userRoom = 0   #Sentinel variable for room

   #Initialize gamestate class - NOTE: MODIFIED TO START IN ROOM 11
   currentState = gamestate.GameStateClass(11,   #currentRoom
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

   #Load rooms
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

   #Load objects
   data.load_objects()

   #Rename objects for engine compatibility
   board = objects["board"]
   keys = objects["keys"]
   handle = objects["handle"]
   skeletonKey = objects["skeleton key"]

   #MIDDLE LEVEL OBJECTS
   smallKey = objects["small key"]
   gun = objects["gun"]

#[END FINAL LEVEL TESTING]

#[BEGIN MID LEVEL TESTING]
def middleLevelTest():
   print ""
   print "Middle Level Testing"
   print ""

   #Initial variables
   userInput = "default"   #Default message for user input
   userRoom = 0   #Sentinel variable for room

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

   #Load rooms
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

   #Load objects
   data.load_objects()

   #Rename objects for engine compatibility
   board = objects["board"]
   keys = objects["keys"]
   handle = objects["handle"]
   skeletonKey = objects["skeleton key"]

   #MIDDLE LEVEL OBJECTS
   smallKey = objects["small key"]
   gun = objects["gun"]

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
      featureList, featureDict, itemList, roomList = utils.formatRoomData(rooms, objects, currentState.currRoom)
      userInput = parse.main(userInput, featureList, featureDict, itemList, roomList)
     
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

         elif currentState.currRoom == 7:    #Garrison
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
         print "HELPFUL TIPS (NEED TO ADD)"
         print "LIST OF RECOGNIZED VERBS (NEED TO ADD)"

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
         #Hallway
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

#[END MID LEVEL TESTING]

#[BEGIN ROOM TESTING]
def roomTest():
	#Testing - create and assign variables to room class
   room1 = room.RoomClass("1", "Brig", "default N", "default S", "default E", "default W", "default Up", "default Down", "long Desc", "short Desc", "feature 1", "feature 2")  

   rm1id = room1.id
   rm1name = room1.name

   rm1north = room1.north
   rm1south = room1.south
   rm1east = room1.east
   rm1west = room1.west
   rm1up = room1.up
   rm1down = room1.down

   rm1LD = room1.longDesc
   rm1SD = room1.shortDesc

   rm1f1 = room1.feat1
   rm1f2 = room1.feat2

   #Testing - print to screen 
   print "Room ID: " + rm1id
   print "Room name: " + rm1name

   print "North: " + rm1north
   print "South: " + rm1south
   print "East: " + rm1east
   print "West: " + rm1west
   print "Up: " + rm1up
   print "Down: " + rm1down

   print "Long description: " + rm1LD
   print "Short description: " + rm1SD

   print "Feature 1: " + rm1f1
   print "Feature 2: " + rm1f2

   #Test implementation of room


#[END ROOM TESTING]

#[BEGIN GAME STATE TESTING]
def gameStateTest():
   #New game:
   #currentRoom, room1, room2, room3, room4, room5, 
   #item1 (board), item2(keys), item3 (handle)
   currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 
      1, 4, 2)


   #Current room 
   currentRoom = currentState.currRoom
   print "Current Room: " 
   print currentRoom

   #Room 1
   visRoom1 = currentState.rm01vis
   print "Room 1 Visited: " 
   print visRoom1

   #Room 2
   visRoom2 = currentState.rm02vis
   print "Room 2 Visited: " 
   print visRoom2

   #Room 3
   visRoom3 = currentState.rm03vis
   print "Room 3 Visited: " 
   print visRoom3

   #Room 4
   visRoom4 = currentState.rm04vis
   print "Room 4 Visited: " 
   print visRoom4

   #Room 5
   visRoom5 = currentState.rm05vis
   print "Room 5 Visited: " 
   print visRoom5

   #Object 1
   #object1N = currentState.obj1Desc
   object1L = currentState.obj1Loc
   print "Object 1 Location: " 
   print object1L

   #Object 2
   object2L = currentState.obj2Loc
   print "Object 2 Location: " 
   print object2L

   #Object 3
   object3L = currentState.obj3Loc
   print "Object 3 Location: " 
   print object3L

#Need to work on class methods
   #print "Current Room (Get Method): " 
   #print currentState.getCurrentRoom()

#[END GAME STATE TESTING]

#[BEGIN OBJECT TESTING]
def objectTest():
   #Object 1 
   obj1 = objectC.ObjectClass("Lever", "A small lever with a wooden handle")

   obj1Name = obj1.name
   obj1Desc = obj1.desc

   print "Object 1 Name: " + obj1Name
   print "Object 1 Description: " + obj1Desc

#[END OBJECT TESTING]

def bottomLevelTest():
   currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 1, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

   board = objectC.ObjectClass("board", 
      "A handsome, though splintery, board you tore off a bench. It extends your reach and gives nasty splinters.",
      "You don't have a board.",
      "There is a board here.",
      "You carefully take the board. This may come in handy later!",
      "You don't see a board to take.",
      "You drop the board.")
   
   keys = objectC.ObjectClass("keys", 
      "A key ring with two keys on it. One is a dull brass color and the other key is a shiny silver.",
      "You don't have any keys.",
      "There are some keys here.",
      "You take the keys.",
      "You don't see any keys to take.",
      "You drop the keys.")

   handle = objectC.ObjectClass("handle", 
      "A metal handle.",
      "You don't have a handle.",
      "There is a handle here.",
      "You take the handle.",
      "You don't see a handle to take.",
      "You drop the handle.")

   skeletonKey = objectC.ObjectClass("skeleton key", 
      "A skeleton key.",
      "You don't have a skeleton key.",
      "There is a skeleton key here.",
      "You take the skeleton key.",
      "You don't see a skeleton key to take.",
      "You drop the skeleton key.")

   brig = room.RoomClass(1, "Brig", 3, "null", "null", "null", "null", "null",
      "You are in a cold, damp room. The only source of light is coming through a barred window. There is straw on the floor and a low wooden bench in the corner. The only exit is a barred door to the North.", 
      "You are in a room that has straw on the floor and a bench in the corner. Light is coming through a barred window and there is a barred door to the North.",
      "straw", 
      "There is thick layer of straw on the floor. It smells musty.",
      "search, move, lift",
      "You shift the straw around throughout the room. It's slimy underneath but there's nothing else there.",
      "There is a thick layer of straw on the floor. You searched it but found nothing.",
      "Straw Fail - this should never display",
      "bench", 
      "There is a rickety wooden bench in the corner. One of the boards looks loose.",
      "take, move, lift",
      "You grab the board and pull on it hard. It starts to crack. You keep pulling and a jagged piece of board comes off the bench. You gingerly drop the board on the bench and regret the splinters - ouch!",
      "There is a wooden bench in the corner with one of the boards missing.",
      "Bench Fail - this should never display",
      "window", 
      "There is a barred window to another room.  You peer through the window and see that the other room is well lit with neat rows of bottles stacked on a large shelf.  Papers are neatly stacked on a large desk that sits just below the window.  There is also a set of keys on the desk! You try to reach it and find that the keys are just out of reach.",
      "use, reach, lift",
      "You have a great idea! You take your splintered board, slip it through the barred window, and reach for the keys. After several attempts, a large splinter off the board catches the key ring and you are able to gingerly lift the keys high enough to place them on the sill where you can reach them. Success!",
      "There is a barred window with a neatly organized room on the other side.",
      "You stand on your tippy toes and reeeeaccchhh..! But you just can't reach those keys.",
      "door", 
      "There is a barred door to another room. It has a small window in it. You peer through the window and can see just beneath it there is a large brass handle with an ever larger brass lock. It looks like it opens into a hallway. You reach through the window and try the door. It's locked.",
      "open, push",
      "You take the keys and select the brass key.  The lock is brass, after all. You reach through the window and put the key in the lock and turn it. You hear a satisfying click! You try the handle and voila! The door is unlocked.",
      "There is a barred door to a hallway. This door is unlocked, thanks to all your hard work!",
      "You reach through the window and try the door. It's locked.",
      "F5 - NA", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6 - NA", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   storage = room.RoomClass(2, "Storage Room", "null", "null", 3, "null", "null", "null",
      "You are in a room full of large storage lockers. Most of the lockers are chained closed.  There is a paper hanging from a peg by the door. There is one locker that does not appear all the way shut and the chain on it is loose like someone closed it in a hurry. To the east there is a wooden door.", 
      "You are in a room full of storage lockers.  There is a paper hanging from a peg next to the door. One of the lockers is ajar. To the east there is a wooden door.",
      "locker", 
      "One of a series of large metal storage lockers is ajar. They are all roughly the size of a small room. You peer through the crack in the door and there is an object on the floor just out of reach. Your eyes adjust to the darkness and you see that it's a handle of some kind.",
      "use, swing",
      "You use the board to pry the locker open just far enough to get the board and your hand in. You then reach in with the board and, after a few swings, manage to land the end just on the other side of the handle. A splinter digs into your palm fiercely. You slowly nudge the handle close enough to the locker door to be able to reach it.",
      "You peer inside the locker. It's the size of a small room and completely empty.",
      "You get down and reach as far as you can into the locker. The loose chain pulls taught as you cram your arm into the small opening. Your cheek smushes against the cold door as you reeeeaccchhh..! It's no good. The handle is too far away.",
      "paper", 
      "A thin piece of paper is stuck to a peg on the wall. It reads: Subject 11 - Locker A, Subject 45 - Locker B, Subject 15 - Locker C, and the last line appears to be scratched out. The paper is pretty thin. You wonder if there's another way to read what was scratched out.",
      "examine, turn over",
      "A thin piece of paper is stuck to a peg on the wall. It reads: Subject 11 - Locker A, Subject 45 - Locker B, Subject 15 - Locker C, and the last line is scratched out. You know, however, that the last line reads: Subject 13 - Brig.",
      "It's such a thin piece of paper. You lightly turn it over and gaze at the back of the paper. Whoever scratched it out didn't press nearly as hard as the heavy handed person that originally wrote the list. It's backwards so it takes you a moment, but you finally make out: Subject 13 - Brig.",
      "Whoever scratched out the paper used a pretty dark ink. You wonder if there's some other way to read it.",
      "door", 
      "A pretty average looking wooden door.",
      "try, check",
      "A pretty average looking unlocked wooden door.",
      "You try the wooden handle - it's unlocked!",
      "Wooden Door Fail - this should never display",
      "F4 - NA", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5 - NA", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6 - NA", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   hallway = room.RoomClass(3, "Lower Hallway", 5, 1, 4, 2, 6, "null",
      "You are in a narrow hallway.  To the north there is an entry way to another room.  To the south there is a wooden barred door. To the east there is a metal door. To the west there is a wooden door. There is a metal ladder in the middle of the room that leads up to a trap door in the ceiling.", 
      "You are in a hallway. There are doors to the south, east, and west. To the north there is an entry way to another room. There is a metal ladder in the middle of the room that leads up to a trap door.",
      "entryway", 
      "An entryway to another room. You look through the entryway and can see a room with a table in the center with chains attached to it. There are markings on the side of the entryway.",
      "examine, check",
      "You look closer at the markings on the entryway.  At first they looked like tally marks.  On second look, they appear to be more like claw marks... or perhaps from fingernails? *gulp*",
      "An entryway to another room. You look through the entryway and can see a room with a table in the center with chains attached to it. There are markings on the side of the entryway that look like they are from fingernails. They make you uncomfortable.",
      "Entryway Fail - this should never display",
      "barred door", 
      "There is a barred door to another room with a brass handle. It has a small window in it. You peer through the window and can see that it opens into a dungeon of some kind.",
      "try, go, open",
      "You try the brass handle - it's unlocked!",
      "There is a barred door to another room with a brass handle. It has a small window in it. You peer through the window and can see that it opens into a dungeon of some kind. It's unlocked.",
      "Barred Door Fail - this should never display",
      "metal door", 
      "There is a metal door with a sign on it that is neatly engraved with the words Observation Room. The door is missing a handle. It's like someone didn't want anyone to be able to get inside.",
      "open, use",
      "You take the handle and, with a little jimmying, get it to attach to the metal door. You give it a pull to see if it will come back off. Nope, permanent!",
      "There is a metal door with a sign on it that is neatly engraved with the words Observation Room. The door is complete and in working order. Nicely handled!",
      "Without a handle, it's impossible to operate the door. You try but it won't budge an inch.",
      "wooden door", 
      "There is a wooden door.  It is pretty average looking.",
      "go, open, try",
      "You try the wooden handle - it's unlocked!",
      "An unlocked wooden door.",
      "Wooden Door Fail - this should never display",
      "ladder", 
      "A sturdy metal ladder.",
      "climb, go",
      "You climb up the ladder to the trap door in the ceiling.",
      "You climb up the ladder to the trap door in the ceiling. You find it pretty easy to climb, it's a well designed ladder.",
      "Ladder Fail - this should never display", 
      "trap door", 
      "A heavy trap door in the ceiling with a handle on it. There is an old fashioned looking lock on the door.",
      "go, open",
      "You put the skeleton key into the lock and turn it. There is a heavy click. You try the handle and, with much effort, it grinds open. You are able to lift the door.",
      "You lift the heavy trap door and it opens.",
      "You try to lift the trap door. It looks heavy but shouldn't be something you can't open. You try pulling the handle and it doesn't budge - locked! The door has an old fashioned looking lock on it. Distressed, you climb back down the ladder.")

   observation = room.RoomClass(4, "Observation Room", "null", "null", "null", 3, "null", "null",
      "You are in a well lit room with neat rows of bottles stacked on a large shelf. Papers are neatly stacked on a large desk that sits just below a barred window. There is another window across from the barred window. There is a chest tucked in a corner with a shiny lock on it. There is a metal door to the East.", 
      "You are in a room with neat rows of bottles stacked on a large shelf. Papers are neatly stacked on a large desk that sits just below a barred window. There is another window in the room opposite the barred window. There is a chest with a shiny lock on it. There is a door to the East.",
      "door", 
      "A metal door.",
      "go, open",
      "You try the handle - it's unlocked!",
      "An unlocked metal door.",
      "Metal door fail - this should never display",
      "barred window", 
      "A barred window that looks into another room.",
      "examine",
      "You look through the barred window and see a room with straw on the floor and a broken bench in the corner.",
      "A barred window that looks into a room with straw on the floor and a broken bench in the corner.",
      "Barred window fail - this should never display",
      "window", 
      "An odd window made of a single pane of glass. It reflects oddly in the light.",
      "examine",
      "You step up to the window and gaze through it. It reflects the light in the room a little strangely. You are looking into another room with a table suspended from the ceiling from chains.",
      "A window that looks into a room with a table suspended from the ceiling by chains.",
      "Window fail - this should never display",
      "chest", 
      "A plain looking wooden chest with a shiny lock on it.",
      "unlock, use, search",
      "You take out the keys you found and select the shiny key. It fits into the lock and you open the chest. It contains a collection of neatly folded white linens. You rummage through and near the bottom you hand hits something hard. You fish it out and place the object on the pile of linens. To your glee it's a skeleton key! Now THIS should come in handy, hehe!",
      "An unlocked chest full of badly rumpled linens.",
      "You try the shiny lock, however it's, well, locked.",
      "bottles", 
      "A shelf lined with neat rows of tinted bottles.",
      "examine",
      "You try to pick one up and your hand bumps into what could possibly be the clearest glass you've ever seen. The entire shelf is encased. Undeterred, you peruse the shelf and see a label on one of the bottles. It reads: burundanga.",
      "A shelf encased in glass with neat rows of tinted bottles.  One of them contains burundanga.",
      "Bottles fail - this should never display", 
      "papers", 
      "A neat stack of papers on the desk. The first page appears to be of some type of report.",
      "read, examine",
      "You look over the cover page of the report. It's in a language you don't recognize. Under the title, a small penciled in footnote reads: Burundanga, Myth or Mind Control Drug? Shuddering, you can't remember how you got here in the first place. Reading that makes the hair on the back of your neck stand up.",
      "A report on a drug called burundanga. It's in a language you don't recognize.",
      "Papers Fail - this should never display")

   examination = room.RoomClass(5, "Examination Room", "null", 3, "null", "null", "null", "null",
      "You are in a room with a large metal table in the center of the room. Instead of being supported by legs, the table is suspended in the air by heavy chains. There is a mirror on the wall in the corner. There is an entryway to the South.", 
      "You are in a room with a metal table suspended in the air by chains. There is a mirror on the wall in the corner. There is an entryway to the South.",
      "entryway", 
      "An entryway to another room. You look through the entryway and see it opens up into a hallway. There are markings on the side of the entryway.",
      "examine",
      "You look closer at the markings on the entryway. They end on this side abruptly. It appears that whatever caught on the wall was being taken into this room.",
      "An entryway to another room. You look through the entryway and see it opens up into a hallway. There are markings on the side of the entryway that end abruptly.",
      "Entryway Fail - this should never display",
      "table", 
      "A large, heavy looking table hangs from the ceiling suspended by thick chains. There is something carved into one corner.",
      "examine",
      "You look more closely at the carving. It resembles a stick figure drawing of a person except the head isn't the right shape. It's far more oblong and larger than would normally be drawn. Perhaps the artist was in a hurry?",
      "A large, heavy looking table hangs from the ceiling suspended by thick chains. There is a carving of an odd stick figure with a large, oblong head in one corner.",
      "Table Fail - this should never display",
      "mirror", 
      "A mirror hangs on the wall. It is quite large and appears to be permanently affixed to the wall.",
      "examine, gaze",
      "You examine the mirror more closely.  On closer inspection, it's not permanently affixed to the wall, it is actually built into the wall. It seems an odd place for a mirror.",
      "A large mirror is built into the wall.",
      "Mirror fail - this should never display",
      "F4 - NA", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5 - NA", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6 - NA", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")


   userInput = "default"
   userRoom = 0   #Sentinel variable for room

   #currentRoom = currentState.currRoom

   #print "Current Room: " 
   #print currentRoom


   while userInput not in ['exit', 'quit']:

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
         #elif currentState.currRoom ==2

      userInput = raw_input (": ")
      #Temp disable parsing 
      #userInput = parseCommands.getInput(userInput)
	  

      if userInput == "1": #Look at feature 1 - STRAW / ENTRYWAY MARKINGS / LOCKER / EXAM ENTRYWAY / DOOR
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

      elif userInput == "8": #Look at object "keys"
         if currentState.obj2Loc ==99: #In inventory
            print keys.desc
         else: #Not in inventory
            print keys.notInInv 

      elif userInput == "9": #Look at feature 4 - DOOR / WOODEN DOOR / CHEST
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

      elif userInput == "11": #General look around room
         if currentState.currRoom == 1:
            print brig.shortDesc
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

         elif currentState.currRoom == 2:
            print storage.shortDesc
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

         elif currentState.currRoom == 3:
            print hallway.shortDesc
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

         elif currentState.currRoom == 4:
            print observation.shortDesc
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

         elif currentState.currRoom == 5:
            print examination.shortDesc
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
         print "HELPFUL TIPS (NEED TO ADD)"
         print "LIST OF RECOGNIZED VERBS (NEED TO ADD)"

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
         print ""

      elif userInput == "18": #Look at feature 5 - Brig:null - LADDER / BOTTLES
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

      elif userInput == "19": #Interact with feature 5  - LADDER
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
         #Hallway
         elif currentState.currRoom == 4:
            print observation.feat5interactSuccess
            currentState.rm04f5 = 1 #Update to interaction complete

      elif userInput == "20": #Look at feature 6 - Brig:null  - TRAP DOOR / PAPERS
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

      elif userInput == "26": #GO UP
         if currentState.currRoom == 1: #Brig
            print "You cannot go that way."

         elif currentState.currRoom == 2: #Storage
            print "You cannot go that way."

         elif currentState.currRoom == 3: #Lower Hallway
            print "TO DO: Go UP to MIDDLE DECK"

         elif currentState.currRoom == 4: #Observation
            print "You cannot go that way."

         elif currentState.currRoom == 5: #Examination
            print "You cannot go that way."

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

      else:
         print "Invalid input"

      #Take straw 

      #Drop straw

