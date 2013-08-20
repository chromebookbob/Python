from sys import argv

script, input_file = argv

# the function print_all is defined with f being it's argument
def print_all(f):
#this prints f (the file)
	print f.read()


def rewind(f):
#this sets the line count back to 0
	f.seek(0)

#this function prints the line count then the next line available
def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "FIrst let's print the whole file: \n"

print_all(current_file)

print "Now let's rewind, like a tape."

rewind(current_file)

print "Let's print three lines:"
#current_line does NOT define the line to be read, the program only reads the next line in the text.
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
		