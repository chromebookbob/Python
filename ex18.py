#this is like an argv script

#def tells python that we want to define a function
#we then define the function with a name and assign it some variables
#this line makes it like argv
def print_two(*args):###the colon is important!!####
	arg1, arg2 = args
	#here is a line of code the function executes
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	

	#same stuff here
#*args is not nescessary:
def print_two_again(arg1, arg2):
	print "arg1: %r arg2: %r" % (arg1, arg2)

#and here
# with one argument
def print_one(arg1):
	print "arg1: %r" % arg1
	
#and none
#putting nothing in the brackets makes it behave like a folder of text that can be executed as a variable
def print_nothing():
	print "I'm livin' on sweet, sweet nothing"
	
	
	#here we execute the functions!!
print_two("Zed","Shaw")
print_two_again("cool", "uncool")
print_one("hjey")
print_nothing()

