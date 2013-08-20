name = 'Jim C Bruges'
age = 14.12 #for real!
height = 74.5 #inches
weight = 180.234 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He is a mere boy at %f." % age
print "He is about %d inches tall." % height
print "He's %f pounds heavy." % weight
print "So, not that heavy."
print "His eyes are %s but his hair is %s !" % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#the tricky line
print "If I add %f, %f, and %f then I get %f." % (age, height, weight, round(age + height + weight))