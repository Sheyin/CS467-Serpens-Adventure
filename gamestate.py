# Game State Class
# Class manages current state of game

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class GameStateClass(object):
	#def __init__(self, currentRoom, room1, room2, room3, room4, room5, item1, item2, item3, rm1f1):	
	def __init__(self, currentRoom, room1, room2, room3, room4, room5, item1, item2, item3, rm1f1, rm1f2, rm1f3, rm1f4, rm1o1, rm1o2):
   		#[BEGIN VARIABLES]
   		self.currRoom = currentRoom #Integer of current room player is in, default = 1 

   		#Visited (1) or unvisited (0) if room has been visited 
   		self.rm01vis = room1	#Bottom deck 
   		self.rm02vis = room2
   		self.rm03vis = room3
   		self.rm04vis = room4
   		self.rm05vis = room5

   		#Location of items & item name - room ID integer or 99 (player inv)
   		self.obj1Loc = item1	#Board
   		self.obj2Loc = item2	#Keys
   		self.obj3Loc = item3

		#Puzzle solved (1) or unsolved (0) 

		#Brig - Room 1
		#Straw - searched (1) or unsearched (0)
		self.rm01f1 = rm1f1
		#Bench - searched (1) or unsearched (0)
		self.rm01f2 = rm1f2
		#Window - searched (1) or unsearched (0)
		self.rm01f3 = rm1f3
		#Door - locked (1) or unlocked (0)
		self.rm01f4 = rm1f4
		#Board - discovered (1) or undiscovered (0)
		self.rm01o1 = rm1o1
		#Keys - discovered (1) or undiscovered (0)
		self.rm01o2 = rm1o2


   		#[END VARIABLES]

   	#@classmethod
	#def getCurrentRoom(cls):	#Need to work on class method syntax 
   	#	return cls.currRoom
   		#print "Yahoo!"

#[END CLASS IMPLEMENTATION]

