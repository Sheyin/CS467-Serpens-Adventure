# Engine Test
# Handles testing of engine components 

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import engine
import room
import object
import gamestate
#[END IMPORTS]

#[BEGIN ROOM TESTING]
def roomTest():
	#Testing - create and assign variables to room class 
	room1 = room.RoomClass("default N", "default S", "default E", "default W", "default Up", "default Down")  

   	rm1north = room1.north
   	rm1south = room1.south
   	rm1east = room1.east
   	rm1west = room1.west
   	rm1up = room1.up
   	rm1down = room1.down

   	#Testing - print to screen 
   	print "North: " + rm1north 
   	print "South: " + rm1south
   	print "East: " + rm1east
   	print "West: " + rm1west
   	print "Up: " + rm1up
   	print "Down: " + rm1down 

#[END ROOM TESTING]