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

#Karen's Room
room1 = RoomClass(1,2,3,4,5,6)
print room1.east


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
        

		

# Open the file if possible
#    with open(file_path_str) as json_data:
with open("data/room2.json") as json_data:
	data = json.load(json_data)
	new_room = Room(data["name"])
	new_room.longDesc = data["longDesc"]


print new_room.name
print new_room.longDesc
