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

   #Data dev/parse dev
   #Accept user input for selection - new, load, exit

   #if new
   #engine.newGame()
   #if load
   #engine.loadGame()
   #if exit
   #engine.exitGame()

   #Engine testing 
   enginetest.roomTest()
   

if __name__ == "__main__":
   main() 
#[END MAIN FUNCTION]