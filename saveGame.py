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
from gamestate import *
#[END IMPORTS]


#objects = {}
current_state = MattsGameStateClass(1)
	
def load_gamestate ():
	"This function loads data from each json file that is present in the /data/objects folder"
	"For each json file, an ObjectClass object is instantiated and populated with data.  The "
	"objects are then stored in a dictionary 'objects' that is keyed on the object name"
#	objects = {}
	gs_list = os.listdir("data/gamestate")
	
	for game in gs_list:

	#open each file as json	
		with open("data/gamestate/" + game) as json_data:
	
	#instantiate temporary ObjectClass object as populate with data
			data = json.load(json_data)
			global current_state
			current_state = MattsGameStateClass(data["name"])
			
			
			current_state.name = data["name"]
			current_state.currRoom = data["currRoom"]
			current_state.rm01vis = data["rm01vis"]
			current_state.rm02vis = data["rm02vis"]
			current_state.obj1Loc = data["obj1Loc"]
			current_state.obj2Loc = data["obj2Loc"]
			current_state.rm01f1 = data["rm01f1"]
			current_state.rm01f2 = data["rm01f2"]
		

	#add object to dictionary (object name is dictionary key)

#			objects[current_object.name] = current_object

	
	#test prints for objects dictionary

	print current_state.rm01f2
	
		
			


load_gamestate()
print current_state.rm01f2
