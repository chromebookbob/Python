ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not ten things in that list, let's fix that."

#split(ten_things, ' ')
stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'COrn', 'Banana', 'girl', 'Boy']

while len(stuff) != 10:
	#pop(more_stuff)
	next_one = more_stuff.pop()
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's now %d items on the list." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff		."

print stuff[1]
print stuff[-1]
print stuff.pop()
#join(' ', stuff)
print ' '.join(stuff)
#ditto
print '#'.join(stuff[3:5])		