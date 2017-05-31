# Room Class
# Implementation of room class - contains mythos and room description which
# allows user to interact with environment

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#Room implementation template:
#declaredName = room.RoomClass("Room ID", "Room Name", "North Room ID", "South Room ID", "East Room ID", "West Room ID", "Up Room ID", "Down Room ID",
#      "Long Description.", 
#      "Short Description.",
#      "F1", 
#      "F1 description",
#      "F1 interaction options",
#      "F1 interaction success",
#      "F1 interaction complete",
#      "F1 interaction fail",
#      "F2", 
#      "F2 description",
#      "F2 interaction options",
#      "F2 interaction success",
#      "F2 interaction complete",
#      "F2 interaction fail",
#      "F3", 
#      "F3 description",
#      "F3 interaction options",
#      "F3 interaction success",
#      "F3 interaction complete",
#      "F3 interaction fail",
#      "F4", 
#      "F4 description",
#      "F4 interaction options",
#      "F4 interaction success",
#      "F4 interaction complete",
#      "F4 interaction fail",
#      "F5", 
#      "F5 description",
#      "F5 interaction options",
#      "F5 interaction success",
#      "F5 interaction complete",
#      "F5 interaction fail", 
#      "F6", 
#      "F6 description",
#      "F6 interaction options",
#      "F6 interaction success",
#      "F6 interaction complete",
#      "F6 interaction fail")


#[BEGIN IMPORTS]

#[END IMPORTS]

#[BEGIN CLASS IMPLEMENTATION]
class RoomClass:
   #def __init__(self, inputID, inputName, inputNorth, inputSouth, inputEast, inputWest, inputUp, inputDown, longDescription, shortDescription, feature1, feature1desc, feat1IO, feat1IS, feature2):	 
   def __init__(self, inputID, inputName, inputNorth, inputSouth, inputEast, inputWest, inputUp, inputDown, longDescription, shortDescription, feature1, feature1desc, feat1IO, feat1IS, feat1IC, feat1IF, feature2, feature2desc, feat2IO, feat2IS, feat2IC, feat2IF, feature3, feature3desc, feat3IO, feat3IS, feat3IC, feat3IF, feature4, feature4desc, feat4IO, feat4IS, feat4IC, feat4IF, feature5, feature5desc, feat5IO, feat5IS, feat5IC, feat5IF, feature6, feature6desc, feat6IO, feat6IS, feat6IC, feat6IF):

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
      self.feat1interactFail = feat1IF

      self.feat2 = feature2
      self.feat2desc = feature2desc
      self.feat2interactOptions = feat2IO
      self.feat2interactSuccess = feat2IS
      self.feat2interactComplete = feat2IC
      self.feat2interactFail = feat2IF

      self.feat3 = feature3
      self.feat3desc = feature3desc
      self.feat3interactOptions = feat3IO
      self.feat3interactSuccess = feat3IS
      self.feat3interactComplete = feat3IC
      self.feat3interactFail = feat3IF

      self.feat4 = feature4
      self.feat4desc = feature4desc
      self.feat4interactOptions = feat4IO
      self.feat4interactSuccess = feat4IS
      self.feat4interactComplete = feat4IC
      self.feat4interactFail = feat4IF

      self.feat5 = feature5
      self.feat5desc = feature5desc
      self.feat5interactOptions = feat5IO
      self.feat5interactSuccess = feat5IS
      self.feat5interactComplete = feat5IC
      self.feat5interactFail = feat5IF

      self.feat6 = feature6
      self.feat6desc = feature6desc
      self.feat6interactOptions = feat6IO
      self.feat6interactSuccess = feat6IS
      self.feat6interactComplete = feat6IC
      self.feat6interactFail = feat6IF
   	#[END VARIABLES]

#[END CLASS IMPLEMENTATION]


#[BEGIN REFERENCES]

#[END REFERENCES]

class MattsRoomClass(object):
    """
    
    """

    def __init__(self, name):
      #[BEGIN VARIABLES]
      self.id = ""
      self.name = name
      self.aliases = []

      self.north = ""
      self.south = ""
      self.east = ""
      self.west = ""
      self.up = ""
      self.down = ""

      self.longDesc = ""
      self.shortDesc = ""

      self.feat1 = ""
      self.feat1desc = "" 
      self.feat1interactOptions = ""
      self.feat1interactSuccess = ""
      self.feat1interactComplete = ""
      self.feat1interactFail = ""

      self.feat2 = ""
      self.feat2desc = ""
      self.feat2interactOptions = ""
      self.feat2interactSuccess = ""
      self.feat2interactComplete = ""
      self.feat2interactFail = ""

      self.feat3 = ""
      self.feat3desc = ""
      self.feat3interactOptions = ""
      self.feat3interactSuccess = ""
      self.feat3interactComplete = ""
      self.feat3interactFail = ""

      self.feat4 = ""
      self.feat4desc = ""
      self.feat4interactOptions = ""
      self.feat4interactSuccess = ""
      self.feat4interactComplete = ""
      self.feat4interactFail = ""
	  
      self.feat5 = ""
      self.feat5desc = ""
      self.feat5interactOptions = ""
      self.feat5interactSuccess = ""
      self.feat5interactComplete = ""
      self.feat5interactFail = ""
	  
      self.feat6 = ""
      self.feat6desc = ""
      self.feat6interactOptions = ""
      self.feat6interactSuccess = ""
      self.feat6interactComplete = ""
      self.feat6interactFail = ""