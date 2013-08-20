print "Let's practice everything."
#remember the escapes
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
#and triple" for multi-line text
poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explaination
\n\t\twhere there is none.
"""

print "--------------"
print poem 
print "--------------"


five = 10 - 2 + 3 - 6
print "This should be five: %d" % five
#started is the variable used in jelly beans
def secret_formula (started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	#this is used to define started
start_point = 100000000000000000000000000000 * 10
#these \/ \/ \/ \/ etc. are equal to what secret formula returns with start_point as the argument
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %s" % start_point
print 'We\'d have %d beans, %d jars, and %d crates.' % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

	