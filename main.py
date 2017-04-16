import engine
import room

def main():
   #code
   print "Hello world!"
   engine.launch()
   room1 = room.RoomClass("default N", "default S", "default E", "default W", "default Up", "default Down")  
   	#declare a room instance 
   #x =  room1.getNorth() 
   rm1north = room1.north
   rm1south = room1.south
   rm1east = room1.east
   rm1west = room1.west
   rm1up = room1.up
   rm1down = room1.down
   print "North: " + rm1north 
   print "South: " + rm1south
   print "East: " + rm1east
   print "West: " + rm1west
   print "Up: " + rm1up
   print "Down: " + rm1down 

if __name__ == "__main__":
   main() 
