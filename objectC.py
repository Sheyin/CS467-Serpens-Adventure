# Object Class
# Implementation of object class - contains variables and functions that 
# allow user and environment to interact with objects

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

#[END IMPORTS]

#Object implementation template:
#declaredObject = objectC.ObjectClass("object name", 
#   "description",
#   "You don't have a *.",
#   "There is a * here.",
#   "take message",
#   "You don't see a * to take.",
#   "You drop the *.")

#[BEGIN CLASS IMPLEMENTATION]
class ObjectClass:
	"""
    This is a test class for use with hard coded data in engine.py to test engine functionality
    """
	def __init__(self, name, description, notInInvMessage, inRoomMessage, takeMessage, notAvailMessage, dropMessage): 
		#[BEGIN VARIABLES]
		self.name = name
		self.desc = description
		self.notInInv = notInInvMessage
		self.inRoom = inRoomMessage
		self.take = takeMessage
		self.notAvail = notAvailMessage
		self.drop = dropMessage

		#[END VARIABLES]


#[END CLASS IMPLEMENTATION]


#[BEGIN REFERENCES]

#[END REFERENCES]
# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
class MattsObjectClass(object):
	def __init__(self, name):
		#[BEGIN VARIABLES]
		self.name = ""
		self.synonyms = []
		self.desc = ""
		self.notInInv = ""
		self.inRoom = ""
		self.take = ""
		self.notAvail = ""
		self.drop = ""