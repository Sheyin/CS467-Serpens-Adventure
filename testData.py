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
import gamestate

 
#[END IMPORTS]

global currentState
currentState = MattsGameStateClass(1)

#print currentState.currRoom

#set initial gamestate
currentState = resume_gamestate("0")

print currentState.currRoom

#test with gamestate 4
currentState.currRoom = 10
save_gamestate("4", currentState)
currentState.currRoom = 99
currentState = resume_gamestate("4")

#should print saved value of 10
print currentState.currRoom

