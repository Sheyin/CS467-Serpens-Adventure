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

   brig = room.RoomClass("1", "Brig", "3", "null", "null", "null", "null", "null",
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
      "You reach through the window and try the door. It's locked.")


   userInput = "default"
   userRoom = 0   #Sentinel variable for room

   currentRoom = currentState.currRoom

   print "Current Room: " 
   print currentRoom


   while userInput not in ['exit', 'quit']:

      if userRoom != currentState.currRoom:  #Displays room description when player moves rooms
         #Display short / long desc
         if currentState.currRoom == 1:
            if currentState.rm01vis == 0:
               print brig.longDesc
               currentState.rm01vis = 1 #Update to visited
            else:
               print brig.shortDesc
         userRoom = currentState.currRoom #Update room the user is currently in
         #elif currentState.currRoom ==2

      #userInput = raw_input (": ")
      userInput = parseCommands.getInput()
      #print "userInput is: " + str(userInput)
	  

      if userInput == "1": #Look at feature 1 - STRAW
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f1 == 0: #Before interaction
               print brig.feat1desc 
            else: #After interaction
               print brig.feat1interactComplete

      if userInput == "2": #Interact with feature 1 
         #Brig
         if currentState.currRoom == 1:
            print brig.feat1interactSuccess
            currentState.rm01f1 = 1 #Update to interaction complete
         #else:
         #   print "Interaction failure message"

      if userInput == "3": #Look at feature 2 - BENCH
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f2 == 0: #Before interaction
               print brig.feat2desc 
            else: #After interaction
               print brig.feat2interactComplete

      if userInput == "4": #Interact with feature 2
         #Brig
         if currentState.currRoom == 1:
            print brig.feat2interactSuccess
            currentState.rm01f2 = 1 #Update to interaction complete
            currentState.rm01o1 = 1 #Board discovered
         #else:
         #   print "Interaction failure message"

      if userInput == "5": #Look at object "board"
         if currentState.obj1Loc ==99: #In iventory
            print board.desc
         else: #Not in inventory
            print board.notInInv 

      if userInput == "6": #Look at feature 3 - WINDOW
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f3 == 0: #Before interaction
               print brig.feat3desc 
            else: #After interaction
               print brig.feat3interactComplete

      if userInput == "7": #Interact with feature 3
         #Brig
         if currentState.currRoom == 1:
            if currentState.obj1Loc == 99:

               print brig.feat3interactSuccess
               currentState.rm01f3 = 1 #Update to interaction complete
               currentState.rm01o2 = 1 #Keys discovered
            else:
               print brig.feat3interactFail

      if userInput == "8": #Look at object "keys"
         if currentState.obj2Loc ==99: #In inventory
            print keys.desc
         else: #Not in inventory
            print keys.notInInv 

      if userInput == "9": #Look at feature 4 - DOOR
         #Brig
         if currentState.currRoom == 1:
            if currentState.rm01f4 == 0: #Before interaction
               print brig.feat4desc 
            else: #After interaction
               print brig.feat4interactComplete

      if userInput == "10": #Interact with feature 4
         #Brig
         if currentState.currRoom == 1:
            if currentState.obj2Loc == 99: #Keys
               print brig.feat4interactSuccess
               currentState.rm01f4 = 1 #Update to interaction complete
            else:
               print brig.feat4interactFail

      if userInput == "11": #General look around room
         if currentState.currRoom == 1:
            print brig.shortDesc
            #Checks objects and if they are DISCOVERED and LOCATED IN ROOM then displays notice they are there
            #Object 1 - board
            if currentState.rm01o1 == 1 and currentState.obj1Loc == 1:
               print board.inRoom
            #Object 2 - keys
            if currentState.rm01o2 == 1 and currentState.obj2Loc == 1:
               print keys.inRoom

      if userInput == "12": #Take board
         if currentState.rm01o1 == 1:
            currentState.obj1Loc = 99 #Add board to player inventory
            print board.take
         else:
            print board.notAvail

      if userInput == "13": #Take keys
         if currentState.rm01o2 == 1:
            currentState.obj2Loc = 99 #Add keys to player inventory
            print keys.take
         else:
            print keys.notAvail

      if userInput == "14": #Drop board
         if currentState.obj1Loc == 99: #In inventory to drop
            currentState.obj1Loc = currentState.currRoom
            print board.drop
         else:
            print board.notInInv

      if userInput == "15": #Drop keys
         if currentState.obj2Loc == 99: #In inventory to drop
            currentState.obj2Loc = currentState.currRoom
            print keys.drop
         else:
            print keys.notInInv

      if userInput == "16": #Help
         print "HELPFUL TIPS (NEED TO ADD)"
         print "LIST OF RECOGNIZED VERBS (NEED TO ADD)"

      if userInput == "17": #Inventory
         print ""
         print "Inventory:"
         if currentState.obj1Loc == 99:   #Board
            print board.name
         if currentState.obj2Loc == 99:   #Keys
            print keys.name
         print ""

      #Go N/S/E/W/Down/Up

      #Take straw 

      #Drop straw
