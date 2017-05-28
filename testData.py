# Test file
# File which tests the data loading and saving functions

# CS 467
# Capstone Project 
# Text Loading and software parsing - Matt Hillman 

#[BEGIN IMPORTS]
import os
import json
from data import *
from saveGame import *
import saveGame
from gamestate import *

 
#[END IMPORTS]

#global currentState
currentState = MattsGameStateClass(1)

#content = dir(saveGame)
#print content


save_gamestate("4")
currentState.currRoom = 5
save_gamestate("4")
currentState.currRoom = 99
load_gamestate("4")
print currentState.currRoom

# load_gamestate("1")
# print currentState.saveNum

# #currentState = MattsGameStateClass(1)
# save_gamestate("10")

# #test 1: save new GS 3.json
# currentState.currRoom = 3
# save_gamestate("3")

# #test 2: overwrite 3.json
# currentState.currRoom = 4
# save_gamestate("3")

# #test 3: load 3.json, check object
# currentState.currRoom = 99
# load_gamestate("3")
# print currentState.currRoom

# #test 4: save, change, load repeat, check object

# save_gamestate("4")
# currentState.currRoom = 5
# load_gamestate("4")
# print currentState.currRoom

# save_gamestate("4")
# currentState.currRoom = 6
# load_gamestate("4")
# print currentState.currRoom

# save_gamestate("4")
# currentState.currRoom = 7
# load_gamestate("4")
# print currentState.currRoom

# #test 5: reload initial state, check object
# load_gamestate("0")
# print currentState.currRoom

# #test 5: reload initial state, check object
# currentState.currRoom = 8
# load_gamestate("1")
# print currentState.currRoom
# save_gamestate("1")
# currentState.currRoom = 9
# load_gamestate("1")
# print currentState.currRoom





# print currentState.rm01f2
 
# print currentState.saveNum

# currentState.currRoom = 5

# save_gamestate("1")

# load_gamestate("1")

# print currentState.currRoom

# currentState.currRoom = 6

# save_gamestate("2")

# load_gamestate("2")

# print currentState.currRoom

# load_rooms()
# load_objects()

# #test prints for rooms dictionary
# print rooms[6].id
# print rooms[6].name
# print (rooms[6].north + 100)
# print rooms[6].longDesc
# print rooms[7].longDesc
	
# #test prints for objects dictionary
# print objects["template"].name
# #print objects["smallKey"].name
# print objects["gun"].name
# print objects["gun"].synonyms[1]
# print objects["board"].name