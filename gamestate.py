# Game State Class
# Class manages current state of game

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class GameStateClass(object):
	def __init__(self, currentRoom, room1, room2, room3, room4, room5, room6, item1, item2, item3):	
   		#[BEGIN VARIABLES]
   		self.currRoom = currentRoom #Integer of current room player is in, default = 1 

   		#Visited (1) or unvisited (0) if room has been visited 
   		self.rm01vis = room1	#Bottom deck 
   		self.rm02vis = room2
   		self.rm03vis = room3
   		self.rm04vis = room4
   		self.rm05vis = room5
   		self.rm06vis = room6

   		#Puzzle solved (1) or unsolved (0) 

   		#Location of items & item name - room ID integer or 99 (player inv)
   		self.obj1Loc = item1
   		#self.obj1Desc = "Lever"

   		self.obj2 = item2
   		self.obj3 = item3
   		#[END VARIABLES]

   	#@classmethod
	#def getCurrentRoom(cls):	#Need to work on class method syntax 
   	#	return cls.currRoom
   		#print "Yahoo!"

#[END CLASS IMPLEMENTATION]

