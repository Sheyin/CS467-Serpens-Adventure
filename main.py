# Main Function
# File which handles engine control and game initiation 

# CS 467
# Capstone Project 
# Engine Dev - Karen Thrasher 

#[BEGIN IMPORTS]
import engine
import enginetest    #Engine testing functions
#[END IMPORTS]

#[BEGIN MAIN FUNCTION]
def main():

   engine.launch() # Engine launch sequence to initiate game menu

   #Engine testing 
   #enginetest.roomTest()
   #enginetest.gameStateTest()
   #enginetest.objectTest()
   

if __name__ == "__main__":
   main() 
#[END MAIN FUNCTION]