# \t is the equivalent of the tab key
cat = "cat"
tabby_cat = '\tI\'m tabbed in with my friend\'s %s '
# \n starts a new line
persian_cat = "I'm split \non a line."
# \\ allows use of backslash so \\ = \
backslash_cat = "I'm \\ a \\ %s." % cat
random_shiz = ' I\'m not a \'cat\' at all. I am 6\"4\' '
# \t tabs in, the star following it means nothing
fat_cat = '''
I'll do a list:
\t* %s food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat % cat
print persian_cat
print backslash_cat
print fat_cat % cat
#this line shows that escape sequences don't work when %r prints them
print "A cat walked up to me and said %r" % random_shiz

