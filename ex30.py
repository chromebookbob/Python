people = 30
cars = 40
buses = 15
# this block will run if it is true
if cars > people:
	print "We should take the cars."
# this block will run if the above block is false and this is true	
elif cars < people:
	print "We shouldn't take the cars."
# This will run if both are false	
else:
	print "We can't decide."
	
if buses > cars:
	print "That's too many buses."		
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."
	
if people > buses:
	print "ALright, let's take the buses."
else:
	print "Fine, let's stay home then."
				