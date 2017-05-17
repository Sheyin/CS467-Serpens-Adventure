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
	"This function loads data from a file named saveNum.json in the /data/gamestate folder"
	"An object named currentState is instantiated and populated with the file data."


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
			# currentState.rm01vis = data["rm01vis"]
			# currentState.rm02vis = data["rm02vis"]
			# currentState.obj1Loc = data["obj1Loc"]
			# currentState.obj2Loc = data["obj2Loc"]
			# currentState.rm01f1 = data["rm01f1"]
			# currentState.rm01f2 = data["rm01f2"]
		

#inside function test print
	print currentState.name

load_gamestate("1")

#outside load_gamestate function test print
#print currentState.rm01f2
print currentState.saveNum

def save_gamestate(saveNum):
    """
    Creates a new json file with data from currentState object 
    """
    jsonObject = dict()
    jsonObject["name"] = currentState.name
    jsonObject["saveNum"] = saveNum
    jsonObject["currRoom"] = currentState.currRoom
    file_content = json.dumps(jsonObject, sort_keys=True, indent=4, separators=(',', ': '))

    with open("data/gamestate/" + saveNum + ".json", "w+") as json_data:
        json_data.write(file_content)

save_gamestate("1")