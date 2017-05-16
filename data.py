# Data Function
# File which handles loading text data from files and parses data into python objects

# CS 467
# Capstone Project 
# Text Loading and software parsing - Matt Hillman 

#[BEGIN IMPORTS]
import os
import json
from room import *
from objectC import *
#[END IMPORTS]



rooms = {}        

def load_rooms ():
	"This function loads data from each json file that is present in the /data/rooms folder"
	"For each json file, a RoomClass object is instantiated and populated with data.  The "
	"objects are then stored in a dictionary 'rooms' that is keyed on the room id"
#	rooms = {}
	room_list = os.listdir("data/rooms")


	for room in room_list:
	
	#open each file as json	
		with open("data/rooms/" + room) as json_data:
			data = json.load(json_data)
	#instantiate temporary RoomClass object as populate with data
			current_room = MattsRoomClass(data["name"])
			current_room.id = data["id"]
			
			current_room.north = data["north"]
			current_room.south = data["south"] 
			current_room.east = data["east"] 
			current_room.west = data["west"] 
			current_room.up = data["up"] 
			current_room.down = data["down"] 
			
			current_room.longDesc = data["longDesc"] 
			current_room.shortDesc = data["shortDesc"] 
			
			current_room.feat1 = data["feat1"] 
			current_room.feat1desc = data["feat1desc"] 
			current_room.feat1interactOptions = data["feat1interactOptions"] 
			current_room.feat1interactSuccess = data["feat1interactSuccess"] 
			current_room.feat1interactComplete = data["feat1interactComplete"] 
			current_room.feat1interactFail = data["feat1interactFail"] 
			
			current_room.feat2 = data["feat2"] 
			current_room.feat2desc = data["feat2desc"] 
			current_room.feat2interactOptions = data["feat2interactOptions"] 
			current_room.feat2interactSuccess = data["feat2interactSuccess"] 
			current_room.feat2interactComplete = data["feat2interactComplete"] 
			current_room.feat2interactFail = data["feat2interactFail"] 
			
			current_room.feat3 = data["feat3"] 
			current_room.feat3desc = data["feat3desc"] 
			current_room.feat3interactOptions = data["feat3interactOptions"] 
			current_room.feat3interactSuccess = data["feat3interactSuccess"] 
			current_room.feat3interactComplete = data["feat3interactComplete"] 
			current_room.feat3interactFail = data["feat3interactFail"] 
			
			current_room.feat4 = data["feat4"] 
			current_room.feat4desc = data["feat4desc"] 
			current_room.feat4interactOptions = data["feat4interactOptions"] 
			current_room.feat4interactSuccess = data["feat4interactSuccess"] 
			current_room.feat4interactComplete = data["feat4interactComplete"] 
			current_room.feat4interactFail = data["feat4interactFail"]

			current_room.feat5 = data["feat5"] 
			current_room.feat5desc = data["feat5desc"] 
			current_room.feat5interactOptions = data["feat5interactOptions"] 
			current_room.feat5interactSuccess = data["feat5interactSuccess"] 
			current_room.feat5interactComplete = data["feat5interactComplete"] 
			current_room.feat5interactFail = data["feat5interactFail"]
			
			current_room.feat6 = data["feat6"] 
			current_room.feat6desc = data["feat6desc"] 
			current_room.feat6interactOptions = data["feat6interactOptions"] 
			current_room.feat6interactSuccess = data["feat6interactSuccess"] 
			current_room.feat6interactComplete = data["feat6interactComplete"] 
			current_room.feat6interactFail = data["feat6interactFail"]
			
	# save temporary object in rooms dictionary, keyed on room id
			rooms[current_room.id] = current_room
			


objects = {}
	
def load_objects ():
	"This function loads data from each json file that is present in the /data/objects folder"
	"For each json file, an ObjectClass object is instantiated and populated with data.  The "
	"objects are then stored in a dictionary 'objects' that is keyed on the object name"
#	objects = {}
	object_list = os.listdir("data/objects")
	
	for object in object_list:

	#open each file as json	
		with open("data/objects/" + object) as json_data:
	
	#instantiate temporary ObjectClass object as populate with data
			data = json.load(json_data)
			current_object = MattsObjectClass(data["name"])
			current_object.name = data["name"]
			current_object.synonyms = data["synonyms"]
			current_object.desc = data["desc"]
			current_object.notInInv = data["notInInv"]
			current_object.inRoom = data["inRoom"]
			current_object.take = data["take"]
			current_object.notAvail = data["notAvail"]
			current_object.drop = data["drop"]
			

	#add object to dictionary (object name is dictionary key)

			objects[current_object.name] = current_object

	
			

load_rooms()
load_objects()

#test prints for rooms dictionary
print rooms[6].id
print rooms[6].name
print (rooms[6].north + 100)
print rooms[6].longDesc
print rooms[7].longDesc
	
#test prints for objects dictionary
print objects["template"].name
print objects["smallKey"].name
print objects["gun"].name
print objects["gun"].synonyms[1]
print objects["board"].name