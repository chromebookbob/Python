people = 20
cats = 30
dogs = 15
# the code underneath the if statement will only be implemented if the if statement is true
if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not many cats, the world is saved!"
	# if it is not indented the code will not work, see below.
#print "Not many cats, the world is saved!"	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print " The world is dry"
	
			
	# \/ allows you to edit dogs and add  a number more to it.		
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people != dogs:
	print "People are less than or equal to dogs."
	
	
if people == dogs:
	print "People are dogs."					
	