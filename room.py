# Room Class
# Implementation of room class - contains mythos and room description which
# allows user to interact with environment

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#Declaration:


#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class RoomClass:
   #def __init__(self, inputID, inputName, inputNorth, inputSouth, inputEast, inputWest, inputUp, inputDown, longDescription, shortDescription, feature1, feature1desc, feat1IO, feat1IS, feature2):	 
   def __init__(self, inputID, inputName, inputNorth, inputSouth, inputEast, inputWest, inputUp, inputDown, longDescription, shortDescription, feature1, feature1desc, feat1IO, feat1IS, feat1IC, feature2, feature2desc, feat2IO, feat2IS, feat2IC, feature3, feature3desc, feat3IO, feat3IS, feat3IC, feature4, feature4desc, feat4IO, feat4IS, feat4IC):

      #[BEGIN VARIABLES]
      self.id = inputID
      self.name = inputName

      self.north = inputNorth
      self.south = inputSouth
      self.east = inputEast
      self.west = inputWest
      self.up = inputUp
      self.down = inputDown

      self.longDesc = longDescription
      self.shortDesc = shortDescription

      self.feat1 = feature1
      self.feat1desc = feature1desc
      self.feat1interactOptions = feat1IO
      self.feat1interactSuccess = feat1IS
      self.feat1interactComplete = feat1IC

      self.feat2 = feature2
      self.feat2desc = feature2desc
      self.feat2interactOptions = feat2IO
      self.feat2interactSuccess = feat2IS
      self.feat2interactComplete = feat2IC

      self.feat3 = feature3
      self.feat3desc = feature3desc
      self.feat3interactOptions = feat3IO
      self.feat3interactSuccess = feat3IS
      self.feat3interactComplete = feat3IC

      self.feat4 = feature4
      self.feat4desc = feature4desc
      self.feat4interactOptions = feat4IO
      self.feat4interactSuccess = feat4IS
      self.feat4interactComplete = feat4IC
   	#[END VARIABLES]

#[END CLASS IMPLEMENTATION]


#[BEGIN REFERENCES]

#[END REFERENCES]