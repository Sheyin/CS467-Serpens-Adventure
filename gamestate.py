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
	def __init__(self, currentRoom, room1, room2, room3, room4, room5, item1, item2, item3, item4, rm1f1, rm1f2, rm1f3, rm1f4, rm1o1, rm1o2, rm2f1, rm2f2, rm2f3, rm2o1, rm3f1, rm3f2, rm3f3, rm3f4, rm3f5, rm3f6, rm4f1, rm4f2, rm4f3, rm4f4, rm4f5, rm4f6, rm4o1, rm5f1, rm5f2, rm5f3):
   		#[BEGIN VARIABLES]
   		self.currRoom = currentRoom #Integer of current room player is in, default = 1 

   		#Visited (1) or unvisited (0) if room has been visited 
   		self.rm01vis = room1	#Bottom deck 
   		self.rm02vis = room2
   		self.rm03vis = room3
   		self.rm04vis = room4
   		self.rm05vis = room5

   		#Location of items & item name - room ID integer or 99 (player inv) or 100 (destroyed/permanently used)
   		self.obj1Loc = item1	#Board
   		self.obj2Loc = item2	#Key
   		self.obj3Loc = item3	#Handle
   		self.obj4Loc = item4	#Skeleton Key

		#Puzzle solved (1) or unsolved (0) 

		#Brig - Room 1
		#Straw - searched (1) or unsearched (0)
		self.rm01f1 = rm1f1
		#Bench - searched (1) or unsearched (0)
		self.rm01f2 = rm1f2
		#Window - searched (1) or unsearched (0)
		self.rm01f3 = rm1f3
		#Door - unlocked (1) or locked (0)
		self.rm01f4 = rm1f4
		#Board - discovered (1) or undiscovered (0)
		self.rm01o1 = rm1o1
		#Keys - discovered (1) or undiscovered (0)
		self.rm01o2 = rm1o2


		#Storage - Room 2
		#Locker - searched (1) or unsearched (0)
		self.rm02f1 = rm2f1
		#Paper - read (1) or unread (0)
		self.rm02f2 = rm2f2
		#Door - examined (1) or unexamined (0)
		self.rm02f3 = rm2f3
		#Handle - discovered (1) or undiscovered (0)
		self.rm02o1 = rm2o1


		#Hallway- Room 3
		#Entryway - examined (1) or unexamined (0)
		self.rm03f1 = rm3f1
		#Barred Door - searched (1) or unsearched (0)
		self.rm03f2 = rm3f2
		#Metal Door - unlocked (1) or locked (0)
		self.rm03f3 = rm3f3
		#Wooden Door - searched (1) or unsearched (0)
		self.rm03f4 = rm3f4
		#Ladder - climbed (1) or unclimbed (0)
		self.rm03f5 = rm3f5
		#Trap Door - unlocked (1) or locked (0)
		self.rm03f6 = rm3f6


		#Observation - Room 4
		#Door - examined (1) or unexamined (0)
		self.rm04f1 = rm4f1
		#Barred Window - examined (1) or unexamined (0)
		self.rm04f2 = rm4f2
		#Window - examined (1) or unexamined (0)
		self.rm04f3 = rm4f3
		#Chest- unlocked (1) or locked (0)
		self.rm04f4 = rm4f4
		#Bottles - examined (1) or unexamined (0)
		self.rm04f5 = rm4f5
		#Papers- examined (1) or unexamined (0)
		self.rm04f6 = rm4f6
		#Skeleton Key - discovered (1) or undiscovered (0)
		self.rm04o1 = rm4o1


		#Examination - Room 5
		#Entryway - examined (1) or unexamined (0)
		self.rm05f1 = rm5f1
		#Table - examined (1) or unexamined (0)
		self.rm05f2 = rm5f2
		#Mirror - examined (1) or unexamined (0)
		self.rm05f3 = rm5f3


   		#[END VARIABLES]

   	#@classmethod
	#def getCurrentRoom(cls):	#Need to work on class method syntax 
   	#	return cls.currRoom
   		#print "Yahoo!"

#[END CLASS IMPLEMENTATION]

