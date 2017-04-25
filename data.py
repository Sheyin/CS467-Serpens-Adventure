# Data Function
# File which handles loading text data from files and parses data into python objects

# CS 467
# Capstone Project 
# Text Loading and software parsing - Matt Hillman 

#[BEGIN IMPORTS]
import os
import json
from room import *
#[END IMPORTS]

#verify import of Karen's RoomClass
#room1 = RoomClass(1,2,3,4,5,6)
#print room1.east


class Room(object):
    """
    
    """

    def __init__(self, name):
        """
        this will initialize the Room.
        :param name: room name as a string
        """
        self.name = name
        self.longDesc = ""
        self.shortDesc = ""
        self.is_visited = False
        

def load_rooms ():
	rooms = {}
	room_list = os.listdir("data/rooms")

	#print room_list[0]
	#rint room_list[1]
			
	# Open the files

	n=0
	for room in room_list:
		with open("data/rooms/" + room) as json_data:
		
	#with open("data/room1.json") as json_data:
			data = json.load(json_data)
			current_room = Room(data["name"])
			current_room.longDesc = data["longDesc"]

	#add nth room to dictionary
			rooms[n] = current_room
			n = n + 1



	#test that room objects are in rooms dictionary
	print rooms[0].name
	print rooms[1].name
	print rooms[2].name

load_rooms()