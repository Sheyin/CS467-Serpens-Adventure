# Game State Class
# Class manages current state of game

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class GameStateClass(object):	
	def __init__(self, currentRoom, room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, room13, room14, room15, item1, item2, item3, item4, item5, item6, item7, item8, rm1f1, rm1f2, rm1f3, rm1f4, rm1o1, rm1o2, rm2f1, rm2f2, rm2f3, rm2o1, rm3f1, rm3f2, rm3f3, rm3f4, rm3f5, rm3f6, rm4f1, rm4f2, rm4f3, rm4f4, rm4f5, rm4f6, rm4o1, rm5f1, rm5f2, rm5f3, rm6f1, rm6f2, rm6f3, rm6f4, rm6f5, rm6o1, rm7f1, rm7f2, rm7f3, rm7f4, rm7f5, rm7o1, rm8f1, rm8f2, rm8f3, rm8f4, rm8f5, rm8f6, rm9f1, rm9f2, rm9f3, rm9f4, rm10f1, rm10f2, rm11f1, rm11f2, rm11f3, rm11f4, rm11f5, rm11f6, rm12f1, rm12f2, rm12f3, rm12f4, rm12f5, rm12f6, rm12o1, rm13f1, rm13f2, rm13f3, rm13f4, rm13f5, rm13f6, rm14f1, rm14f2, rm14f3, rm14f4, rm14f5, rm14f6, rm14o1, rm15f1, rm15f2, rm15f3, rm15f4, rm15f5):
   		#[BEGIN VARIABLES]
   		self.currRoom = currentRoom #Integer of current room player is in, default = 1 

   		#Visited (1) or unvisited (0) if room has been visited 
   		self.rm01vis = room1	#Bottom deck 
   		self.rm02vis = room2
   		self.rm03vis = room3
   		self.rm04vis = room4
   		self.rm05vis = room5

   		self.rm06vis = room6	#Middle deck
   		self.rm07vis = room7
   		self.rm08vis = room8
   		self.rm09vis = room9
   		self.rm10vis = room10

   		self.rm11vis = room11	#Final deck
   		self.rm12vis = room12
   		self.rm13vis = room13
   		self.rm14vis = room14
   		self.rm15vis = room15

   		#Location of items & item name - room ID integer or 99 (player inv) or 100 (destroyed/permanently used)
   		self.obj1Loc = item1	#Board
   		self.obj2Loc = item2	#Key
   		self.obj3Loc = item3	#Handle
   		self.obj4Loc = item4	#Skeleton Key
   		self.obj5Loc = item5	#Small Key
   		self.obj6Loc = item6	#Gun
   		self.obj7Loc = item7	#Lockpick
   		self.obj8Loc = item8	#Cryptex

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


		#Rum - Room 6
		#Bottle
		self.rm06f1 = rm6f1
		#Lamp
		self.rm06f2 = rm6f2
		#Trap door
		self.rm06f3 = rm6f3
		#Barrels
		self.rm06f4 = rm6f4
		#Wooden door
		self.rm06f5 = rm6f5
		#Keys - discovered (1) or undiscovered (0)
		self.rm06o1 = rm6o1


		#Armory - Room 7
		#Gun Cabinet
		self.rm07f1 = rm7f1
		#Wooden Door
		self.rm07f2 = rm7f2
		#Locker
		self.rm07f3 = rm7f3
		#Gun Case
		self.rm07f4 = rm7f4
		#Metal Door
		self.rm07f5 = rm7f5
		#Gun - discovered (1) or undiscovered (0)
		self.rm07o1 = rm7o1


		#Garrison - Room 8
		#Bunks
		self.rm08f1 = rm8f1
		#Table
		self.rm08f2 = rm8f2
		#Photograph
		self.rm08f3 = rm8f3
		#Wooden Door
		self.rm08f4 = rm8f4
		#Canvas Flap
		self.rm08f5 = rm8f5
		#Metal Door
		self.rm08f6 = rm8f6


		#Galley - Room 9
		#Canvas Flap
		self.rm09f1 = rm9f1
		#Trash Can
		self.rm09f2 = rm9f2
		#Stove
		self.rm09f3 = rm9f3
		#Sink
		self.rm09f4 = rm9f4


		#Ladder - Room 10
		#Ladder
		self.rm10f1 = rm10f1
		#Wooden Door
		self.rm10f2 = rm10f2


		#Hallway - Room 11
		#ladder
		self.rm11f1 = rm11f1
		#metal door
		self.rm11f2 = rm11f2
		#glass door
		self.rm11f3 = rm11f3
		#locked door
		self.rm11f4 = rm11f4
		#painting
		self.rm11f5 = rm11f5
		#plant
		self.rm11f6 = rm11f6


		#Garden - Room 12
		#plants
		self.rm12f1 = rm12f1
		#switch
		self.rm12f2 = rm12f2
		#note
		self.rm12f3 = rm12f3
		#east door
		self.rm12f4 = rm12f4
		#west door
		self.rm12f5 = rm12f5
		#plant
		self.rm12f6 = rm12f6
		#Object - lockpick
		self.rm12o1 = rm12o1


		#Control - Room 13
		#chair
		self.rm13f1 = rm13f1
		#glass
		self.rm13f2 = rm13f2
		#door
		self.rm13f3 = rm13f3
		#group A
		self.rm13f4 = rm13f4
		#group B
		self.rm13f5 = rm13f5
		#group C
		self.rm13f6 = rm13f6


		#Side - Room 14
		#door
		self.rm14f1 = rm14f1
		#photo
		self.rm14f2 = rm14f2
		#drawer
		self.rm14f3 = rm14f3
		#fireplace
		self.rm14f4 = rm14f4
		#letter
		self.rm14f5 = rm14f5
		#chest
		self.rm14f6 = rm14f6
		#Object - cryptex 
		self.rm14o1 = rm14o1


		#Processing - Room 15
		#hatch
		self.rm15f1 = rm15f1
		#device
		self.rm15f2 = rm15f2
		#handle
		self.rm15f3 = rm15f3
		#bracelet
		self.rm15f4 = rm15f4
		#door
		self.rm15f5 = rm15f5


   		#[END VARIABLES]

   	#@classmethod
	#def getCurrentRoom(cls):	#Need to work on class method syntax 
   	#	return cls.currRoom
   		#print "Yahoo!"

#[END CLASS IMPLEMENTATION]

class MattsGameStateClass(object):
    """
    
    """
    def __init__(self, name):
		#[BEGIN VARIABLES]
		self.name = ""
		self.saveNum = ""
		self.currRoom = "" #Integer of current room player is in, default = 1 

   		#Visited (1) or unvisited (0) if room has been visited 
   		self.rm01vis = ""	#Bottom deck 
   		self.rm02vis = ""
		self.rm03vis = ""
		self.rm04vis = ""
		self.rm05vis = ""
		self.rm06vis = ""
		self.rm07vis = ""
		self.rm08vis = ""
		self.rm09vis = ""
		self.rm010vis = ""
		self.rm011vis = ""
		self.rm012vis = ""
		self.rm013vis = ""
		self.rm014vis = ""
		self.rm015vis = ""
   	
		
   		#Location of items & item name - room ID integer or 99 (player inv) or 100 (destroyed/permanently used)
   		self.obj1Loc = ""	#Board
   		self.obj2Loc = ""	#Key
		self.obj3Loc = ""
		self.obj4Loc = ""
		self.obj5Loc = ""
		self.obj6Loc = ""
		self.obj7Loc = ""
		self.obj8Loc = ""
		self.obj9Loc = ""
		self.obj10Loc = ""
		
			
   		
		#Brig - Room 1
		#Straw - searched (1) or unsearched (0)
		self.rm01f1 = ""
		#Bench - searched (1) or unsearched (0)
		self.rm01f2 = ""
		#Window - searched (1) or unsearched (0)
		self.rm01f3 = ""
		#Door - unlocked (1) or locked (0)
		self.rm01f4 = ""
		#Board - discovered (1) or undiscovered (0)
		self.rm01o1 = ""
		#Keys - discovered (1) or undiscovered (0)
		self.rm01o2 = ""


		#Storage - Room 2
		#Locker - searched (1) or unsearched (0)
		self.rm02f1 = ""
		#Paper - read (1) or unread (0)
		self.rm02f2 = ""
		#Door - examined (1) or unexamined (0)
		self.rm02f3 = ""
		#Handle - discovered (1) or undiscovered (0)
		self.rm02o1 = ""


		#Hallway- Room 3
		#Entryway - examined (1) or unexamined (0)
		self.rm03f1 = ""
		#Barred Door - searched (1) or unsearched (0)
		self.rm03f2 = ""
		#Metal Door - unlocked (1) or locked (0)
		self.rm03f3 = ""
		#Wooden Door - searched (1) or unsearched (0)
		self.rm03f4 = ""
		#Ladder - climbed (1) or unclimbed (0)
		self.rm03f5 = ""
		#Trap Door - unlocked (1) or locked (0)
		self.rm03f6 = ""


		#Observation - Room 4
		#Door - examined (1) or unexamined (0)
		self.rm04f1 = ""
		#Barred Window - examined (1) or unexamined (0)
		self.rm04f2 = ""
		#Window - examined (1) or unexamined (0)
		self.rm04f3 = ""
		#Chest- unlocked (1) or locked (0)
		self.rm04f4 = ""
		#Bottles - examined (1) or unexamined (0)
		self.rm04f5 = ""
		#Papers- examined (1) or unexamined (0)
		self.rm04f6 = ""
		#Skeleton Key - discovered (1) or undiscovered (0)
		self.rm04o1 = ""


		#Examination - Room 5
		#Entryway - examined (1) or unexamined (0)
		self.rm05f1 = ""
		#Table - examined (1) or unexamined (0)
		self.rm05f2 = ""
		#Mirror - examined (1) or unexamined (0)
		self.rm05f3 = ""
		
		self.rm06f1 = ""
		self.rm06f2 = ""
		self.rm07f1 = ""
		self.rm07f2 = ""
		self.rm08f1 = ""
		self.rm08f2 = ""
		self.rm09f1 = ""
		self.rm09f2 = ""
		self.rm10f1 = ""
		self.rm10f2 = ""
		self.rm11f1 = ""
		self.rm11f2 = ""
		self.rm11f3 = ""
		self.rm11f4 = ""
		self.rm11f5 = ""
		self.rm11f6 = ""
		self.rm12f1 = ""
		self.rm12f2 = ""
		self.rm12f3 = ""
		self.rm12f4 = ""
		self.rm12f5 = ""
		self.rm12f6 = ""
		self.rm13f1 = ""
		self.rm13f2 = ""
		self.rm13f3 = ""
		self.rm13f4 = ""
		self.rm13f5 = ""
		self.rm13f6 = ""
		self.rm14f1 = ""
		self.rm14f2 = ""
		self.rm14f3 = ""
		self.rm14f4 = ""
		self.rm14f5 = ""
		self.rm14f6 = ""
		self.rm15f1 = ""
		self.rm15f2 = ""
		self.rm15f3 = ""
		self.rm15f4 = ""
		self.rm15f5 = ""
		self.rm15f6 = ""
		self.rm16f1 = ""
		self.rm16f2 = ""
		self.rm16f3 = ""
		self.rm16f4 = ""
		self.rm16f5 = ""
		self.rm16f6 = ""
		
		

		


