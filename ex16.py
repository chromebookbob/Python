from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
#poen() opens the file, but you have to say you want to write to the file by typing "w"
target = open(filename, "w+ r+")

print "Truncating the file. Goodbye!"
# truncate deletes all the data in the file
target.truncate()

print "Now I'm going to ask you for three lines."
# user input
line1 = raw_input("line 1:  ")
line2 = raw_input("line 2:  ")
line3 = raw_input("line 3:  ")

print "I'm going to write these to the file"

# these lines say open the file then write what isin the variable linex
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "You wrote your lines, are they correct?"
target
#remember when using read, you have to print it!!!!
target.close()
target = open(filename)

print target.read()

correct = raw_input("???")

print "okay."

print "Now we close the file. Bye!"
# this closes the file
target.close()