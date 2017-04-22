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
#[END IMPORTS]

#[BEGIN ROOM TESTING]
def roomTest():
	#Testing - create and assign variables to room class
   room1 = room.RoomClass("default N", "default S", "default E", "default W", "default Up", "default Down", "long Desc", "short Desc", "Name of Room", "feature 1", "feature 2")  

   rm1north = room1.north
   rm1south = room1.south
   rm1east = room1.east
   rm1west = room1.west
   rm1up = room1.up
   rm1down = room1.down
   rm1LD = room1.longDesc
   rm1SD = room1.shortDesc
   rm1name = room1.name
   rm1f1 = room1.feat1
   rm1f2 = room1.feat2

   #Testing - print to screen 
   print "North: " + rm1north
   print "South: " + rm1south
   print "East: " + rm1east
   print "West: " + rm1west
   print "Up: " + rm1up
   print "Down: " + rm1down
   print "Long description: " + rm1LD
   print "Short description: " + rm1SD
   print "Room name: " + rm1name
   print "Feature 1: " + rm1f1
   print "Feature 2: " + rm1f2

#[END ROOM TESTING]

#[BEGIN GAME STATE TESTING]
def gameStateTest():
   currentState = gamestate.GameStateClass(1, 1, 0, 0, 0, 0, 0, 99, 1, 2)

   #Current room 
   currentRoom = currentState.currRoom
   print "Current Room: " 
   print currentRoom

   #Room 1
   visRoom1 = currentState.rm01vis
   print "Room 1 Visited: " 
   print visRoom1

   #Object 1
   #object1N = currentState.obj1Desc
   object1L = currentState.obj1Loc

   #print "Object 1 Name: " + object1N
   print "Object 1 Location: " 
   print object1L

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