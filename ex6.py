#%d allows you do define data (d) outside of the string
x = 'There are %d types of people.' % 10
binary = 'binary'
do_not = "don't"
# %s allows you to define a string to place inside the string, can be a variable. as there are multiple %s you need to enclose the variables in brackets with commas in between
y = "Those who know %s and those who %s" % (binary, do_not)

# this prints x, then y
print x
print y

# %r prints exactly the string from the variable, quotation marks and all
print 'I said: %r.' % x
# %s only prints what is contained in the string
print 'I also said: "%s".' %y


hilarious = False
joke_evaluation = "Isn't this joke funny?!?! %r"

#you can define a % when you print as well as when defining the variable
print joke_evaluation % hilarious

w = "This is the left side of..."
e = 'a string with a right side'

#adding two variables prints them together
print w + e
