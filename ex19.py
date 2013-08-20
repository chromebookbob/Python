
# defines cheese and crackers with the arguments cheese count and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "So you have %d cheese and crackers!" % (cheese_count + boxes_of_crackers)
	print "Man, that's enough for a party!"
	print "Get a blanket. \n"
	

print "We can just give the function numbers directly:"
# defines cheese count and boxes of crackers as 20 and 30 respectively
cheese_and_crackers(20, 30)

print "OR we can use variables from our script:"
# defines variables which can be used to transfer data to the function
amount_of_cheese = int(raw_input("Please Define Your Cheese Count:"))
amount_of_crackers = int(raw_input("please define the number of cracker boxes in your possesion"))

# uses the defined variables as arguments for cheese and crackers
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do maths inside it too!"
cheese_and_crackers(10 +20, 5 + 6)

print "And we can combine the two, variables and maths!"
#combines all three methods!
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

	