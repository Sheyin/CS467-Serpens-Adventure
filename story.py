# Story-specific bits.  More specifically, the conclusion.
from utils import display

def ending(injured = True, bracelet = True):
	# Check gamestate for certain variables.  By default they will be true.

	display("You are blinded by the sudden influx of light as the hatch creaks open.  You feel weak with relief.  It's the outdoors - no doubt about it.")
	print ""

	if injured:
		display("As you climb out, you stifle a curse as your injured skin brushes against the hatch.  The gun explosion had left you slightly scorched - but alive.  Hopefully there are no guards around.")
	else:
		display("You climb out of the hatch carefully and quietly.")
	print ""

	display("You wince as the hatch creaks closed.  Looking around, it seems you really are on a boat.  A rather large one, in fact, much bigger than what you had seen inside.")
	print ""
	display("No one seems to be around.  You turn and give the hatch you came from a final look.  A sign reading '4815162342' is above the entryway.  There seem to be similar hatches with other numbers written above them nearby.")
	print ""

	if bracelet:
		display("You idly fiddle with the bracelet around your wrist.  It was strange that it had forcibly been put on you, but you decide not to give it any further thought.  After all, you are now free!")
	else:
		display("You feel a slight chill go through you.  The wind?  Or perhaps it was because of seeing those same numbers again.  Luckily you had found that mysterious hint telling you how to remove it...")
	print ""

	display("You carefully make your way towards a walkway extending from the dock.  You haven't seen anyone else, and it seems like a quiet sunny day, but you don't want to let down your guard.  You make your way off the boat, and onto solid land.")
	print "" 
	display("Freedom, at last.  For a while you thought you were dead in the water.  But now... things seem to be looking up.")
	print ""

if __name__ == "__main__":
	# Same ending printed multiple times
	print "Default ending snippet:"
	ending ()

	print "Used gun, have bracelet (same as default):"
	ending (True, True)

	print "No gun, have bracelet:"
	ending (False, True)

	print "Used gun, no bracelet:"
	ending (True, False)

	print "No gun, no bracelet (best ending):"
	ending (False, False)