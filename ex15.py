from sys import argv

script, filename = argv
# open() opens a file
txt = open(filename)

print "Here's your file %r:" % filename
# read() takes the opened file and prints it
print txt.readlines()

txt.close()

print"Type that filename again:"
file_again = raw_input(">")
#here the user input is asked instead of argv being used but the same happens
txt_again = open(file_again)
# readlines() reads a number of lines from a file!
print txt_again.readlines(3-4)
## using close on files is important##
txt_again.close()

#using raw_input() would be better for a user as it is easier
