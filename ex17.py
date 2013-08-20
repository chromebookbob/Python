from sys import argv
# Returns true/false if file exists
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)
#opens the file
in_file = open(from_file) ;indata = in_file.read()
#assigns data in the file to a variable
#says how big the file is 
print "The input file is %d bytes long" % len(indata)
#outputs whether the file exists
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
#allows user to choose whether or not to carry on
raw_input()
#opens copy.txt for writing to
out_file = open(to_file, "w")
#opens copy txt then writes the data holding variable to it.
out_file.write(indata)

print "Alright, all done."
#closes the files.
out_file.close()
in_file.close()
