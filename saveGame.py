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
			currentState.rm01vis = data["rm01vis"]
			currentState.rm02vis = data["rm02vis"]
			currentState.rm03vis = data["rm03vis"]
			currentState.rm04vis = data["rm04vis"]
			currentState.rm05vis = data["rm05vis"]
			currentState.rm06vis = data["rm06vis"]
			currentState.rm07vis = data["rm07vis"]
			currentState.rm08vis = data["rm08vis"]
			currentState.rm09vis = data["rm09vis"]
			currentState.rm10vis = data["rm10vis"]
			currentState.rm11vis = data["rm11vis"]
			currentState.rm12vis = data["rm12vis"]
			currentState.rm13vis = data["rm13vis"]
			currentState.rm14vis = data["rm14vis"]
			currentState.rm15vis = data["rm15vis"]
			
			currentState.obj1Loc = data["obj1Loc"]
			currentState.obj2Loc = data["obj2Loc"]
			currentState.obj3Loc = data["obj3Loc"]
			currentState.obj4Loc = data["obj4Loc"]
			currentState.obj5Loc = data["obj5Loc"]
			currentState.obj6Loc = data["obj6Loc"]
			currentState.obj7Loc = data["obj7Loc"]
			currentState.obj8Loc = data["obj8Loc"]

			currentState.rm01f1 = data["rm01f1"]
			currentState.rm01f2 = data["rm01f2"]
			currentState.rm01f3 = data["rm01f3"]
			currentState.rm01f4 = data["rm01f4"]
			currentState.rm02f1 = data["rm02f1"]
			currentState.rm02f2 = data["rm02f2"]
			currentState.rm02f3 = data["rm02f3"]
			currentState.rm03f1 = data["rm03f1"]
			currentState.rm03f2 = data["rm03f2"]
			currentState.rm03f3 = data["rm03f3"]
			currentState.rm03f4 = data["rm03f4"]
			currentState.rm03f5 = data["rm03f5"]
			currentState.rm03f6 = data["rm03f6"]
			currentState.rm04f1 = data["rm04f1"]
			currentState.rm04f2 = data["rm04f2"]
			currentState.rm04f3 = data["rm04f3"]
			currentState.rm04f4 = data["rm04f4"]
			currentState.rm04f5 = data["rm04f5"]
			currentState.rm04f6 = data["rm04f6"]
			currentState.rm05f1 = data["rm05f1"]
			currentState.rm05f2 = data["rm05f2"]
			currentState.rm05f3 = data["rm05f3"]
			
			currentState.rm06f1 = data["rm06f1"]
			currentState.rm06f2 = data["rm06f2"]
			currentState.rm06f3 = data["rm06f3"]
			currentState.rm06f4 = data["rm06f4"]
			currentState.rm06f5 = data["rm06f5"]
	
			currentState.rm07f1 = data["rm07f1"]
			currentState.rm07f2 = data["rm07f2"]
			currentState.rm07f3 = data["rm07f3"]
			currentState.rm07f4 = data["rm07f4"]
			currentState.rm07f5 = data["rm07f5"]
			
			currentState.rm08f1 = data["rm08f1"]
			currentState.rm08f2 = data["rm08f2"]
			currentState.rm08f3 = data["rm08f3"]
			currentState.rm08f4 = data["rm08f4"]
			currentState.rm08f5 = data["rm08f5"]
			currentState.rm08f6 = data["rm08f6"]
			
			currentState.rm09f1 = data["rm09f1"]
			currentState.rm09f2 = data["rm09f2"]
			currentState.rm09f3 = data["rm09f3"]
			currentState.rm09f4 = data["rm09f4"]
			
			currentState.rm10f1 = data["rm10f1"]
			currentState.rm10f2 = data["rm10f2"]
			
			currentState.rm11f1 = data["rm11f1"]
			currentState.rm11f2 = data["rm11f2"]
			currentState.rm11f3 = data["rm11f3"]
			currentState.rm11f4 = data["rm11f4"]
			currentState.rm11f5 = data["rm11f5"]
			currentState.rm11f6 = data["rm11f5"]
			
			currentState.rm12f1 = data["rm12f1"]
			currentState.rm12f2 = data["rm12f2"]
			currentState.rm12f3 = data["rm12f3"]
			currentState.rm12f4 = data["rm12f4"]
			currentState.rm12f5 = data["rm12f5"]
			currentState.rm12f6 = data["rm12f6"]
			
			currentState.rm13f1 = data["rm13f1"]
			currentState.rm13f2 = data["rm13f2"]
			currentState.rm13f3 = data["rm13f3"]
			currentState.rm13f4 = data["rm13f4"]
			currentState.rm13f5 = data["rm13f5"]
			currentState.rm13f6 = data["rm13f6"]
			
			currentState.rm14f1 = data["rm14f1"]
			currentState.rm14f2 = data["rm14f2"]
			currentState.rm14f3 = data["rm14f3"]
			currentState.rm14f4 = data["rm14f4"]
			currentState.rm14f5 = data["rm14f5"]
			currentState.rm14f6 = data["rm14f6"]
			
			currentState.rm15f1 = data["rm15f1"]
			currentState.rm15f2 = data["rm15f2"]
			currentState.rm15f3 = data["rm15f3"]
			currentState.rm15f4 = data["rm15f4"]
			currentState.rm15f5 = data["rm15f5"]
							
			currentState.rm01o1 = data["rm01o1"]
			currentState.rm01o2 = data["rm01o2"]
			currentState.rm02o1 = data["rm02o1"]
			currentState.rm04o1 = data["rm04o1"]
			currentState.rm06o1 = data["rm06o1"]
			currentState.rm07o1 = data["rm07o1"]
			currentState.rm12o1 = data["rm12o1"]
			currentState.rm14o1 = data["rm14o1"]
	
load_gamestate("0")

def save_gamestate(saveNum):
    "Creates a new json file having name, saveNum.json, populated with data from currentState object and"
    "saves the json file in the /data/gamestate folder"
    jsonObject = dict()
    jsonObject["name"] = currentState.name
    jsonObject["saveNum"] = saveNum
    jsonObject["currRoom"] = currentState.currRoom
    jsonObject["rm01vis"] = currentState.rm01vis
    jsonObject["rm02vis"] = currentState.rm02vis
    jsonObject["rm03vis"] = currentState.rm03vis
    jsonObject["rm04vis"] = currentState.rm04vis
    jsonObject["rm05vis"] = currentState.rm05vis
    jsonObject["rm06vis"] = currentState.rm06vis
    jsonObject["rm07vis"] = currentState.rm07vis
    jsonObject["rm08vis"] = currentState.rm08vis
    jsonObject["rm09vis"] = currentState.rm09vis
    jsonObject["rm10vis"] = currentState.rm10vis
    jsonObject["rm11vis"] = currentState.rm11vis
    jsonObject["rm12vis"] = currentState.rm12vis
    jsonObject["rm13vis"] = currentState.rm13vis
    jsonObject["rm14vis"] = currentState.rm14vis
    jsonObject["rm15vis"] = currentState.rm15vis

    jsonObject["obj1Loc"] = currentState.obj1Loc
    jsonObject["obj2Loc"] = currentState.obj2Loc
    jsonObject["obj3Loc"] = currentState.obj3Loc
    jsonObject["obj4Loc"] = currentState.obj4Loc
    jsonObject["obj5Loc"] = currentState.obj5Loc
    jsonObject["obj6Loc"] = currentState.obj6Loc
    jsonObject["obj7Loc"] = currentState.obj7Loc
    jsonObject["obj8Loc"] = currentState.obj8Loc
    jsonObject["rm01f1"] = currentState.rm01f1
    jsonObject["rm01f2"] = currentState.rm01f2
    jsonObject["rm01f3"] = currentState.rm01f3
    jsonObject["rm01f4"] = currentState.rm01f4
    jsonObject["rm02f1"] = currentState.rm02f1
    jsonObject["rm02f2"] = currentState.rm02f2
    jsonObject["rm02f3"] = currentState.rm02f3
    jsonObject["rm03f1"] = currentState.rm03f1
    jsonObject["rm03f2"] = currentState.rm03f2
    jsonObject["rm03f3"] = currentState.rm03f3
    jsonObject["rm03f4"] = currentState.rm03f4
    jsonObject["rm03f5"] = currentState.rm03f5
    jsonObject["rm03f6"] = currentState.rm03f6
    jsonObject["rm04f1"] = currentState.rm04f1
    jsonObject["rm04f2"] = currentState.rm04f2
    jsonObject["rm04f3"] = currentState.rm04f3
    jsonObject["rm04f4"] = currentState.rm04f4
    jsonObject["rm04f5"] = currentState.rm04f5
    jsonObject["rm04f6"] = currentState.rm04f6
    jsonObject["rm05f1"] = currentState.rm05f1
    jsonObject["rm05f2"] = currentState.rm05f2
    jsonObject["rm05f3"] = currentState.rm05f3

    jsonObject["rm06f1"] = currentState.rm06f1
    jsonObject["rm06f2"] = currentState.rm06f2
    jsonObject["rm06f3"] = currentState.rm06f3
    jsonObject["rm06f4"] = currentState.rm06f4
    jsonObject["rm06f5"] = currentState.rm06f5
    jsonObject["rm07f1"] = currentState.rm07f1
    jsonObject["rm07f2"] = currentState.rm07f2
    jsonObject["rm07f3"] = currentState.rm07f3
    jsonObject["rm07f4"] = currentState.rm07f4
    jsonObject["rm07f5"] = currentState.rm07f5
    jsonObject["rm08f1"] = currentState.rm08f1
    jsonObject["rm08f2"] = currentState.rm08f2
    jsonObject["rm08f3"] = currentState.rm08f3
    jsonObject["rm08f4"] = currentState.rm08f4
    jsonObject["rm08f5"] = currentState.rm08f5
    jsonObject["rm08f6"] = currentState.rm08f6
    jsonObject["rm09f1"] = currentState.rm09f1
    jsonObject["rm09f2"] = currentState.rm09f2
    jsonObject["rm09f3"] = currentState.rm09f3
    jsonObject["rm09f4"] = currentState.rm09f4
    jsonObject["rm10f1"] = currentState.rm10f1
    jsonObject["rm10f2"] = currentState.rm10f2
    jsonObject["rm11f1"] = currentState.rm11f1
    jsonObject["rm11f2"] = currentState.rm11f2
    jsonObject["rm11f3"] = currentState.rm11f3
    jsonObject["rm11f4"] = currentState.rm11f4
    jsonObject["rm11f5"] = currentState.rm11f5
    jsonObject["rm11f6"] = currentState.rm11f5
    jsonObject["rm12f1"] = currentState.rm12f1
    jsonObject["rm12f2"] = currentState.rm12f2
    jsonObject["rm12f3"] = currentState.rm12f3
    jsonObject["rm12f4"] = currentState.rm12f4
    jsonObject["rm12f5"] = currentState.rm12f5
    jsonObject["rm12f6"] = currentState.rm12f6
    jsonObject["rm13f1"] = currentState.rm13f1
    jsonObject["rm13f2"] = currentState.rm13f2
    jsonObject["rm13f3"] = currentState.rm13f3
    jsonObject["rm13f4"] = currentState.rm13f4
    jsonObject["rm13f5"] = currentState.rm13f5
    jsonObject["rm13f6"] = currentState.rm13f6
    jsonObject["rm14f1"] = currentState.rm14f1
    jsonObject["rm14f2"] = currentState.rm14f2
    jsonObject["rm14f3"] = currentState.rm14f3
    jsonObject["rm14f4"] = currentState.rm14f4
    jsonObject["rm14f5"] = currentState.rm14f5
    jsonObject["rm14f6"] = currentState.rm14f6
    jsonObject["rm15f1"] = currentState.rm15f1
    jsonObject["rm15f2"] = currentState.rm15f2
    jsonObject["rm15f3"] = currentState.rm15f3
    jsonObject["rm15f4"] = currentState.rm15f4
    jsonObject["rm15f5"] = currentState.rm15f5
    jsonObject["rm01o1"] = currentState.rm01o1
    jsonObject["rm01o2"] = currentState.rm01o2
    jsonObject["rm02o1"] = currentState.rm02o1
    jsonObject["rm04o1"] = currentState.rm04o1
    jsonObject["rm06o1"] = currentState.rm06o1
    jsonObject["rm07o1"] = currentState.rm07o1
    jsonObject["rm12o1"] = currentState.rm12o1
    jsonObject["rm14o1"] = currentState.rm14o1
	

    file_content = json.dumps(jsonObject, separators=(',', ': '), indent=3, sort_keys=True)

    with open("data/gamestate/" + saveNum + ".json", "w+") as json_data:
        json_data.write(file_content)

