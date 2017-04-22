# Room Class
# Implementation of room class - contains mythos and room description which
# allows user to interact with environment

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class RoomClass:
   def __init__(self, inputNorth, inputSouth, inputEast, inputWest, inputUp, inputDown, longDescription, shortDescription, roomName, feature1, feature2):	 

      #[BEGIN VARIABLES]
      self.north = inputNorth
      self.south = inputSouth
      self.east = inputEast
      self.west = inputWest
      self.up = inputUp
      self.down = inputDown
      self.name = roomName
      self.longDesc = longDescription
      self.shortDesc = shortDescription
      self.feat1 = feature1
      self.feat2 = feature2
   	#[END VARIABLES]

#[END CLASS IMPLEMENTATION]


#[BEGIN REFERENCES]

#[END REFERENCES]