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


objects = {}
	
def load_objects ():
	"This function loads data from each json file that is present in the /data/objects folder"
	"For each json file, an ObjectClass object is instantiated and populated with data.  The "
	"objects are then stored in a dictionary 'objects' that is keyed on the object name"
#	objects = {}
	object_list = os.listdir("data/gamestate")
	
	for object in object_list:

	#open each file as json	
		with open("data/gamestate/" + object) as json_data:
	
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

	
	#test prints for objects dictionary

	print objects["gun"].name
	print objects["gun"].synonyms[1]

	

			
			


load_objects()

print objects["gun"].name
print objects["gun"].synonyms[1]
