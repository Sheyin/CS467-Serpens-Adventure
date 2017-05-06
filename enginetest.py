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
import parseCommands
#[END IMPORTS]

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
   currentState = gamestate.GameStateClass(1, 0, 0, 0, 0, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0)

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
      "F5", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   storage = room.RoomClass(2, "Storage Room", "null", "null", 3, "null", "null", "null",
      "You are in a room full of storage lockers. Most of the lockers are chained closed.  There is a clipboard hanging from a peg by the door. There is one locker that does not appear all the way shut. To the east there is a wooden door.", 
      "You are in a room full of storage lockers.  There is a clipboard hanging from a peg next to the door. One of the lockers is ajar. To the east there is a wooden door.",
      "F1", 
      "F1 description",
      "F1 interaction options",
      "F1 interaction success",
      "F1 interaction complete",
      "F1 interaction fail",
      "F2", 
      "F2 description",
      "F2 interaction options",
      "F2 interaction success",
      "F2 interaction complete",
      "F2 interaction fail",
      "F3", 
      "F3 description",
      "F3 interaction options",
      "F3 interaction success",
      "F3 interaction complete",
      "F3 interaction fail",
      "F4", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   hallway = room.RoomClass(3, "Lower Hallway", 5, 1, 4, 2, 6, "null",
      "You are in a narrow hallway.  To the north there is an entry way to another room.  To the south there is a wooden barred door. To the east there is a metal door. To the west there is a wooden door. There is a metal ladder in the middle of the room that leads up to a trap door in the ceiling.", 
      "You are in a hallway. There are doors to the south, east, and west. To the north there is an entry way to another room. There is a metal ladder in the middle of the room that leads up to a trap door.",
      "F1", 
      "F1 description",
      "F1 interaction options",
      "F1 interaction success",
      "F1 interaction complete",
      "F1 interaction fail",
      "F2", 
      "F2 description",
      "F2 interaction options",
      "F2 interaction success",
      "F2 interaction complete",
      "F2 interaction fail",
      "F3", 
      "F3 description",
      "F3 interaction options",
      "F3 interaction success",
      "F3 interaction complete",
      "F3 interaction fail",
      "F4", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   observation = room.RoomClass(4, "Observation Room", "null", "null", "null", 3, "null", "null",
      "You are in a well lit room with neat rows of bottles stacked on a large shelf. Papers are neatly stacked on a large desk that sits just below a barred window. There is a metal door to the East.", 
      "You are in a room with neat rows of bottles stacked on a large shelf. Papers are neatly stacked on a large desk that sits just below a barred window. There is a metal door to the East.",
      "F1", 
      "F1 description",
      "F1 interaction options",
      "F1 interaction success",
      "F1 interaction complete",
      "F1 interaction fail",
      "F2", 
      "F2 description",
      "F2 interaction options",
      "F2 interaction success",
      "F2 interaction complete",
      "F2 interaction fail",
      "F3", 
      "F3 description",
      "F3 interaction options",
      "F3 interaction success",
      "F3 interaction complete",
      "F3 interaction fail",
      "F4", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6", 
      "F6 description",
      "F6 interaction options",
      "F6 interaction success",
      "F6 interaction complete",
      "F6 interaction fail")

   anchor = room.RoomClass(5, "Anchor Room", "null", 3, "null", "null", "null", "null",
      "You are in a room with a large winch in the center connected to two heavy chains that run through holes in the sides of the room. There is a large wooden shelf in the corner. There is an entryway to the South.", 
      "You are in a room with a winch in the center connected to two heavy chains that run through holes in the sides of the room. There is a shelf in the corner. There is an entryway to the South.",
      "F1", 
      "F1 description",
      "F1 interaction options",
      "F1 interaction success",
      "F1 interaction complete",
      "F1 interaction fail",
      "F2", 
      "F2 description",
      "F2 interaction options",
      "F2 interaction success",
      "F2 interaction complete",
      "F2 interaction fail",
      "F3", 
      "F3 description",
      "F3 interaction options",
      "F3 interaction success",
      "F3 interaction complete",
      "F3 interaction fail",
      "F4", 
      "F4 description",
      "F4 interaction options",
      "F4 interaction success",
      "F4 interaction complete",
      "F4 interaction fail",
      "F5", 
      "F5 description",
      "F5 interaction options",
      "F5 interaction success",
      "F5 interaction complete",
      "F5 interaction fail", 
      "F6", 
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

         elif currentState.currRoom == 5:    #Anchor
            if currentState.rm05vis == 0: 
               print anchor.longDesc
               currentState.rm05vis = 1 #Update to visited
            else:
               print anchor.shortDesc

         userRoom = currentState.currRoom #Update room the user is currently in
         #elif currentState.currRoom ==2

      userInput = raw_input (": ")
      #Temp disable parsing 
      #userInput = parseCommands.getInput(userInput)
	  

      if userInput == "1": #Look at feature 1 - STRAW
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f1 == 0: #Before interaction
               print brig.feat1desc 
            else: #After interaction
               print brig.feat1interactComplete

      elif userInput == "2": #Interact with feature 1 
         #Brig
         if currentState.currRoom == 1:
            print brig.feat1interactSuccess
            currentState.rm01f1 = 1 #Update to interaction complete
         #else:
         #   print "Interaction failure message"

      elif userInput == "3": #Look at feature 2 - BENCH
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f2 == 0: #Before interaction
               print brig.feat2desc 
            else: #After interaction
               print brig.feat2interactComplete

      elif userInput == "4": #Interact with feature 2
         #Brig
         if currentState.currRoom == 1:
            print brig.feat2interactSuccess
            currentState.rm01f2 = 1 #Update to interaction complete
            currentState.rm01o1 = 1 #Board discovered
         #else:
         #   print "Interaction failure message"

      elif userInput == "5": #Look at object "board"
         if currentState.obj1Loc ==99: #In iventory
            print board.desc
         else: #Not in inventory
            print board.notInInv 

      elif userInput == "6": #Look at feature 3 - WINDOW
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f3 == 0: #Before interaction
               print brig.feat3desc 
            else: #After interaction
               print brig.feat3interactComplete

      elif userInput == "7": #Interact with feature 3
         #Brig
         if currentState.currRoom == 1:
            if currentState.obj1Loc == 99:

               print brig.feat3interactSuccess
               currentState.rm01f3 = 1 #Update to interaction complete
               currentState.rm01o2 = 1 #Keys discovered
            else:
               print brig.feat3interactFail

      elif userInput == "8": #Look at object "keys"
         if currentState.obj2Loc ==99: #In inventory
            print keys.desc
         else: #Not in inventory
            print keys.notInInv 

      elif userInput == "9": #Look at feature 4 - DOOR
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f4 == 0: #Before interaction
               print brig.feat4desc 
            else: #After interaction
               print brig.feat4interactComplete

      elif userInput == "10": #Interact with feature 4
         #Brig
         if currentState.currRoom == 1:
            if currentState.obj2Loc == 99: #Keys
               print brig.feat4interactSuccess
               currentState.rm01f4 = 1 #Update to interaction complete
            else:
               print brig.feat4interactFail

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

         elif currentState.currRoom == 2:
            print "STORAGE ROOM"

         elif currentState.currRoom == 3:
            print hallway.shortDesc

      elif userInput == "12": #Take board
         if currentState.rm01o1 == 1:
            currentState.obj1Loc = 99 #Add board to player inventory
            print board.take
         else:
            print board.notAvail

      elif userInput == "13": #Take keys
         if currentState.rm01o2 == 1:
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
         print ""

      elif userInput == "18": #Look at feature 5 - Brig:null 
         #Brig
         if currentState.currRoom == 1:
            print "Brig feature 5 null"
            #if currentState.rm01f4 == 0: #Before interaction
            #   print brig.feat4desc 
            #else: #After interaction
            #   print brig.feat4interactComplete

      elif userInput == "19": #Interact with feature 5
         #Brig
         if currentState.currRoom == 1:
            print "Brig feature 5 null"
            #if currentState.obj2Loc == 99: #Keys
            #   print brig.feat4interactSuccess
            #   currentState.rm01f4 = 1 #Update to interaction complete
            #else:
            #   print brig.feat4interactFail

      elif userInput == "20": #Look at feature 6 - Brig:null 
         #Brig
         if currentState.currRoom == 1:
            print "Brig feature 6 null"
            #if currentState.rm01f4 == 0: #Before interaction
            #   print brig.feat4desc 
            #else: #After interaction
            #   print brig.feat4interactComplete

      elif userInput == "21": #Interact with feature 6
         #Brig
         if currentState.currRoom == 1:
            print "Brig feature 6 null"
            #if currentState.obj2Loc == 99: #Keys
            #   print brig.feat4interactSuccess
            #   currentState.rm01f4 = 1 #Update to interaction complete
            #else:
            #   print brig.feat4interactFail

      elif userInput == "22": #GO NORTH
         if currentState.currRoom == 1: #Brig
            if currentState.rm01f4 == 1: #If door unlocked, proceed North into Lower Hallway
               currentState.currRoom = 3 #Updates current user location to ID 3 (Lower Hallway)
            else:
               print brig.feat4interactFail  #Else, failure statement

         elif currentState.currRoom == 2: #Storage
            print "You cannot go that way."

         elif currentState.currRoom == 3: #Lower Hallway
            currentState.currRoom = hallway.north #Updates current user location to ID 5 (Anchor Room)

         elif currentState.currRoom == 4: #Observation
            print "You cannot go that way."

         elif currentState.currRoom == 5: #Anchor
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

         elif currentState.currRoom == 5: #Anchor
            currentState.currRoom = anchor.south #Updates current user location to ID 3 (Hallway)

      elif userInput == "24": #GO WEST
         if currentState.currRoom == 1: #Brig
            print "You cannot go that way."

         elif currentState.currRoom == 2: #Storage
            print "You cannot go that way."

         elif currentState.currRoom == 3: #Lower Hallway
            currentState.currRoom = hallway.west #Updates current user location to ID 2 (Storage Room)

         elif currentState.currRoom == 4: #Observation
            currentState.currRoom = observation.west #Updates current user location to ID 3 (Hallway)

         elif currentState.currRoom == 5: #Anchor
            print "You cannot go that way."

      elif userInput == "25": #GO EAST
         if currentState.currRoom == 1: #Brig
            print "You cannot go that way."

         elif currentState.currRoom == 2: #Storage
            currentState.currRoom = storage.east #Updates current user location to ID 3 (Hallway)

         elif currentState.currRoom == 3: #Lower Hallway
            currentState.currRoom = hallway.east #Updates current user location to ID 4 (Observation)

         elif currentState.currRoom == 4: #Observation
            print "You cannot go that way."

         elif currentState.currRoom == 5: #Anchor
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

         elif currentState.currRoom == 5: #Anchor
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

         elif currentState.currRoom == 5: #Anchor
            print "You cannot go that way."

      else:
         print "Invalid input"

      #Take straw 

      #Drop straw
