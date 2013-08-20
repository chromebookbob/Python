



def start():
	def restart():
		print "Do you want to restart?"
		restart = raw_input(">")
		if restart == "yes" or "y":
			print "restarting...."
			start()
		elif restart == "no" or "n":
			print "quitting"
			quit()
	
	
	
	
	
	print "You enter a dark room with two doors, do you go through door #1 or door #2?"
	door = raw_input(">")
	if door == "1":
		print "There's a giant bear here eating a cheese cake. What do you do?"
		print" 1. Take the cake."
		print " 2. Scream at the bear."
	
		bear = raw_input(">")
	
		if bear == "1":
			print "The bear eats your face off. Good Job!"
			restart()
		elif bear == "2":
			print "The bear eats your legs off. Good job."
			restart()
		else:		
			print "Well, doing %s is probably better. Bear runs away." % bear
			print "You look around the room, there is a mysterious lamp in the corner, what do you do?"
			print "1. rub it and hope that this game turns into a classic disney film."
			print "2. Throw it at the wall in desparation."
			
			lamp = raw_input(">")
			if lamp == 	"1":
				print "Nothing happens, you look like a fool"
				print "what next?"
				print "1. eat one of the strange nuts on the table."
				print "2. walk across the room."
				
				next = raw_input(">")
				if next == "1":
					print " You remember your nut allergy just after you place the nut in your mouth..."
					restart()
				elif next ==  "2":
					print "You walk into the mantrap in the darkness."
					restart()
				else:
					print "You stand still, falling into the quicksand that appears under your feet."
					restart()		
			elif lamp == "2":
				print " you throw the lamp and it ruins the structural integrity of the building, it collapses."
				restart()
			else:
				print "You stand still, falling into the quicksand that appears under your feet."
				restart() 			
							
	elif door == "2":
		print "You stare into the endless abyss at cluthu's retina."
		print "1. Blueberries."
		print "2. Yellow jacket clothespins	"
		print "3. Understanding revolvers yelling melodies."
	
		insanity = raw_input(">")	
	
	
		if insanity == "1" or insanity == "2":
			print "Your body survives powered by a mind of jello. Good Job!"
		else:
			print "The insanity rots your eyes into a pool of muck. Good job!"
			restart()
		
	else:
		print "You stumble and fall on a knife and die. Good Job!"				
		restart()
start()