def add(a, b):
	# Function called with two arguments
	# WHat the function is doing is printed when variable = blah is typed
	print "ADDING %d + %d" % (a, b)
	#this line returns the answer to any variable assigned to this function
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some maths with just functions!"
# Here the prints will be printed but not the answer
age = add( float(raw_input("first age value")), 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
# The returned results become the variable and can be used normally.
print "Age: %d, Height: %d, Weight: %d, IQ: %d"	% (age, height, weight, iq)


#a puzzle
print "Here is the puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
