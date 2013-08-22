## Animal is-a object
class Animal(object):
	pass
	
## Dog is-a animal 
class Dog(Animal):

	def __init__(self, name):
	## has-a name
		self.name = name
		
## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
		## Cat has-a name
		self.name = name
		
## Person is-a object
class Person(object):
	
	def __init__(self, name):
		## Person has-a name
		self.name = name
		
		#Person has-a pet of some kind						
		self.pet = None
		
## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
		##	Employee has-a name
		super(Employee, self).__init__(name)
		## Employee has-a salary
		self.salary = salary
		
		
## FIsh is-a Object		
class Fish(object):
	pass
	
## Salmon is-a fish				
class Salmon(Fish):
	pass
	
## Halibut is-a FIsh:
class Halibut(Fish):
	pass
	
## Rovwer is-a dog
rover = Dog("Rover")

## Satan is-a cat		
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet called satan
mary.pet = satan

## Frank is-a employee who has-a 120000 salary
frank = Employee("Frank", 120000)

## Frank has-a pet called rover
frank.pet = rover

## flipper is-a fish
flipper = Fish()

## crouse is-a salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()