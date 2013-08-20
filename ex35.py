from sys import exit

def gold_room():
	print "THis room is full of gold! How much do you take?"
	
	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number."	)
		
	if how_much < 50:
		print "Nice, not greedy. You win!"
		exit(0)
	else:
		dead("You greedy bastard")
		
def bear_room():
	"""this function asks how player is to move the bear, 
	there are three options: take honey, taunt bear, and taunt bear and bear moved.
	the first results in death
	the second asks if bear has been moved, if he hasn't then he is moved and you can proceed
	the last ends in death.
	If the player then types in open door he will proceed to the gold room. """
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input(">")
		
		if next == "take honey":
			dead("The bear looks at you and then slaps your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You may go through it now."
			bear_moved = True
		elif next == "taunt bear and bear_moved":
			dead("The bear get's pissed off and chew your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()			
		else: 
			print " I don't know what that means..."
			
			
def cthulu_room():
	print "Here you see the great evil Cthulu."
	print "He, it, whatever stares at you and you go insane."
	print "Do you flee for your life or eat your head?"
	
	next = raw_input(">")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("Well, that  was tasty!")
	else:
		cthulu_room()
		
def dead(why) :
	print why, "Good Job!"
	exit(0)
	
	
def start():
	print "You are alone in a dark room."
	print "There is a door to your right and last."
	print "Which one do you take?"	
	
	next = raw_input(">")
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulu_room()
	else:
		dead("You stumble around the room until you starve.")		
		
start()													