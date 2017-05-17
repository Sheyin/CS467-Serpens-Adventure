# Data Function
# File which handles loading text data from files and parses data into python objects

# CS 467
# Capstone Project 
# Text Loading and software parsing - Matt Hillman 

#[BEGIN IMPORTS]
import os
import json
from gamestate import *
#[END IMPORTS]

currentState = MattsGameStateClass(1)
	
def load_gamestate (saveNum):
	"This function loads data from each json file that is present in the /data/gamestate folder"
	"For each json file, an ObjectClass object is instantiated and populated with data.  The "
	"objects are then stored in a dictionary 'objects' that is keyed on the object name"

	gs_list = os.listdir("data/gamestate")
	
	#open  file as json	
	with open("data/gamestate/" + saveNum + ".json") as json_data:
	
	#instantiate gamestate object and populate with data
			data = json.load(json_data)
			global currentState
			currentState = MattsGameStateClass(data["name"])
			currentState.name = data["name"]
			currentState.saveNum = saveNum
			currentState.currRoom = data["currRoom"]
			currentState.rm01vis = data["rm01vis"]
			currentState.rm02vis = data["rm02vis"]
			currentState.obj1Loc = data["obj1Loc"]
			currentState.obj2Loc = data["obj2Loc"]
			currentState.rm01f1 = data["rm01f1"]
			currentState.rm01f2 = data["rm01f2"]
		

#inside function test print
	print currentState.rm01f2

load_gamestate("0")

#outside function test print
print currentState.rm01f2
print currentState.saveNum

