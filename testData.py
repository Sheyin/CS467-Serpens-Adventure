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

#[END IMPORTS]

#currentState = MattsGameStateClass(1)
	
#load_gamestate("0")

print currentState.rm01f2
 
print currentState.saveNum

currentState.currRoom = 5

save_gamestate("1")

load_gamestate("1")

print currentState.currRoom

currentState.currRoom = 6

save_gamestate("2")

load_gamestate("2")

print currentState.currRoom

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
#print objects["smallKey"].name
print objects["gun"].name
print objects["gun"].synonyms[1]
print objects["board"].name