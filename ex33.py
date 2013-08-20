from sys import exit

def appendy(add, big):
	
	i = 0
	numbers = []
	
	while i < big:
		print "At the top is is %d" % i
		numbers.append(i)
	
		i += add
		print "Numbers now:", numbers
		print "At the bottom i is %d" %i
	print "The numbers: "

	for num in numbers:
		print num	 
print "DO you want to append numbers?"
answer = raw_input(">")
if answer == "yes" or "y":
	appendy(int(raw_input("what increment do you want?")), int(raw_input("what number do you want")))
else:
	exit()	
