#import allows you to add features to your script from the python feature set
#this means you can see what is used, it also keeps programs small
#argv = argument variable holds arguments you pass to your python script

from sys import argv
#this line takes what's in argv and assigns it to the variables
script, first, second, third = argv

print "The script is called:", script
print "Your first variable is called:", first
print "Your second variable is called:", second
print "Your third variable is called:", third

#when running this script 3 variables have to be defined in the command line
# e.g. python ex13.py first second third