## ========================================================================== ##
#%__Object_Oriented_Programming__ (part 1)
## ========================================================================== ##

"""
Everything in Python is an object.
When we assign variables, we create instances of those objects.
E.g.: x = list((1,2,3)) --> x is an instance of the object list

in a class we have:
- *attributes* --> characteristics of objects
- *methods* --> operations we can perform on objects --> they look like functions inside of a class
"""

# Object Oriented Programming (OOP) tends to be one of the major obstacles for
# beginners when they are first starting to learn Python.
#
# There are many,many tutorials and lessons covering OOP so feel free to Google
# search other lessons, and I have also put some links to other useful tutorials
# online at the bottom of this Notebook.
#
# For this lesson we will construct our knowledge of OOP in Python by building
# on the following topics:
#
# * Objects
# * Using the *class* keyword
# * Creating class attributes
# * Creating methods in a class
# * Learning about Inheritance
# * Learning about Special Methods for classes
#
# Lets start the lesson by remembering about the Basic Python Objects.
# For example:
l = [1,2,3]


# Remember how we could call methods on a list?
l.count(2)


# What we will basically be doing in this lecture is exploring how we could
# create an Object type like a list. We've already learned about how to create
# functions. So lets explore Objects in general:
#

## ========================================================================== ##
#%__Objects__
## ========================================================================== ##
# In Python, *everything is an object*. Remember from previous lectures we can
# use type() to check the type of object something is:


type(1)
type([])
type(())
type({})


# So we know all these things are objects, so how can we create our own Object
#  types? That is where the *class* keyword comes in.

## ========================================================================== ##
#%__Class__ (part 2)
## ========================================================================== ##

# The user defined objects are created using the class keyword. The class is a
# blueprint that defines a nature of a future object. From classes we can
# construct instances. An instance is a specific object created from a particular
# class.

# For example, above we created the object 'l' which was an instance of a list object.
#
# Let see how we can use **class**:


# Create a new object type called Sample
class Sample():
    pass

# Instance of Sample
x = Sample()

print(type(x))


# By convention we give classes a name that starts with a capital letter.
# Note how x is now the reference to our new instance of a Sample class.
# In other words, we **instantiate** the Sample class.
#
# Inside of the class we currently just have pass.
#  But we can define class attributes and methods.
#
# An **attribute** is a characteristic of an object.
# A **method** is an operation we can perform with the object.
#
# For example we can create a class called Dog. An attribute of a dog may be its
# breed or its name, while a method of a dog may be defined by a .bark() method
# which returns a sound.
#
# Let's get a better understanding of attributes through an example.
#

## ============================ ##
#%__ATTRIBUTES__
## ============================ ##
"""
The syntax for creating an attribute is:
            self.attribute = something
here is a special method called:
            __init__()
which is used to initialize the attributes of an object

there are many special methods
special methods are those methods surounded by a set of underscores --> __specialmethod__

__init__(self)
the __init__method is the most basic special method (initialization)
the self keyword is always necessary: it tells that the method refers to itself (i.e. the class object)

you can pass the __init__ method more attributes:
e.g. breed (the breed attribute)
see below:
"""
class Dog():
    def __init__(self,breed): 
        ## each ATTRIBUTE in a class definition begins with a REFERENCE to the instance object!! i.e. SELF
        ## which says: refer to this particular instance of this object
        ## breed is the ARGUMENT! and its VALUE is passed during the INSTANTIATION or INITIALIZATION of the class
        self.breed = breed 
        
"""
but now, to create an instance of the Dog class, you require breed as an argument!!
def __init__(self,breed): <-- referred to this breed!!
"""

sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')

# Lets break down what we have above.The special method
#
#     __init__()
# is called automatically right after the object has been created:
#
#     def __init__(self, breed):
# Each attribute in a class definition begins with a reference to the instance
# object. It is by convention named self. The breed is the argument. The value
# is passed during the class instantiation.
#
#      self.breed = breed

# Now we have created two instances of the Dog class. With two breed types, we
# can then access these attributes like this:

sam.breed

frank.breed


# Note how we don't have any parenthesis after breed, this is because it is an
# attribute and doesn't take any arguments.

##- add one more attribute
class Dog():
    def __init__(self,breed,name): 
        self.breed = breed
        self.name = name

sam = Dog(breed='Lab',name='Sammy')
sam.breed
sam.name

#! to understand what refers to what:
"""
class Dog():
    def __init__(self,breed,THIS_NAME): # --> THIS_NAME is the input name
        self.breed = breed
        self.name = THIS_NAME # --> THIS_NAME refers to the input name
        -> "self.name" assigns the attribute "name" to the initialization of that Dog()

sam = Dog('Lab','Kira') # you don't have to specify the attribute name as long as you go in the correct order
"""

## ========================================================================== ##
##%___CLASS_OBEJCT_ATTRIBUTES__
## ========================================================================== ##
"""
CLASS OBJECT ATTRIBUTES are always the same for any instance of the class!!
"""
# e.g. all dogs are mammals, regardless of their breed or their name.
# therefore we could create the attribute *species* for the Dog class. 

# We apply this logic in the following manner:

class Dog():

    # Class Object Attribute 
    # place them at the top, before the first __init__
    # it is defined outside of any methods in the class
    species = 'mammal'

    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

sam = Dog('Lab','Sam')

sam.name
sam.species

## ========================================================================== ##
#%______METHODS______
## ========================================================================== ##
"""
Methods are functions defined inside the body of a class.
They are used to perform operations with the attributes of our Objects.
Basically, methods are the whole point of why you would want to create Objects.

Methods are essential in ENCAPSULATION concept of the OOP paradigm.
This is essential in dividing responsibilities in programming, especially in large applications.

Think of methods as functions acting on an Object that 
take the Object itself into account through its *self* argument.
"""

# Lets go through an example of creating a Circle class:
class Circle():

    pi = 3.14 # Class Object Attribute

    # Circle get instantiated with a radius (default is 1) --> 1 by default is used when you don't provide a radius
    def __init__(self, radius=1):
        self.radius = radius

    # Area method calculates the area. Note the use of self.
    def area(self): # --> the *self* keyword says that this method area is actually a *method of this class*, not some free floating function inside of this class!!
        return self.radius * self.radius * Circle.pi 
        # --> self.radius because you want to refer to the radius of this circle 
        # --> otherwise, if you write return radius*radius*pi what radius are you talking about? the circle's radius or a variable called radius?
        # --> self.radius tells to the method area to look at the radius of the current Circle Object
        # --> since pi is a Class Object Attribute, you say Circle.pi

myc = Circle(3)
print(myc.radius)
print(myc.area) # <bound method Circle.area of <__main__.Circle object at 0x7fdc33b5e470>> is the output
# bound method Circle.area --> this tells that are is a method bound to the Circle class
# __main__.Circle object at 0x7fdc33b5e470 --> this particular instance is located at this position in my computer's memory
# if you want to execute the method:
print(myc.area())


## now you want to have a method that resets the radius
"""
There are 2 ways in which you can change the attributes of a class:
1.
you can call directly the attribute off the object:
"""
myc.radius = 100
myc.area()
"""
2.
sometimes you want to have a method to redefine something like that
"""
class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    ## Method for resetting Radius
    def setRadius(self, new_radius):
        self.radius = new_radius 
        # --> NB: there is no "return" --> not all object methods need to return something!!
        # --> some methods just affect the objects in place

    # Method for getting radius (Same as just calling .radius)
    def getRadius(self):
        return self.radius

# Notice how we used self. notation to reference attributes of the class
# within the method calls.

# instantiate
myc = Circle()
myc.radius # this is the same as the next line
myc.getRadius()
myc.area()

myc.setRadius(2) # reset radius
myc.radius
myc.getRadius()
myc.area()


## ========================================================================== ##
#%______INHERITANCE______ (part 3)
## ========================================================================== ##
"""
INHERITANCE is a way to FORM NEW CLASSES USING CLASSES THAT HAVE ALREADY BEEN DEFINED.

- DERIVED CLASSES (DESCENDANTS) are the newly formed classes
- BASE CLASSES (ANCESTORS) are the classes that we derive from

# DERIVED CLASSES override or EXTEND the functionality of BASE CLASSES

"code reuse" and "reduction of complexity" of a program are important benefits of inheritance.
"""

## BASE CLASS
class Animal():

    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")

    def eat(self):
        print("Eating")

mya = Animal()
mya.whoAmI()
mya.eat()

## DERIVED CLASS - INHERITANCE
# all dogs are animals, therefor I want to inherit from the base class of animal
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self) # initializes Animal, but you don't actually really need this line
        print("Dog created")

d = Dog()
d.whoAmI() # inherited method
d.eat() # inherited method

## DERIVED CLASS - OVERRIDE & EXTENSION
class Dog(Animal):

    def __init__(self):
        print("Dog created")

    ## override
    def whoAmI(self): # this overrides the same method of the Animal base class
        print("Dog")

    ## new methods (extension)
    def bark(self):
        print("Woof!")

d = Dog()
d.whoAmI() # overridden method
d.eat() # inherited method
d.bark() # new method (extension)

"""
The derived class inherits the functionality of the base class.
--> the eat() method

The derived class modifies existing behavior of the base class.
--> the whoAmI() method

Finally, the derived class extends the functionality of the base class,
--> the bark() method

"""

## ========================================================================== ##
#%______SPECIAL_METHODS_______
## ========================================================================== ##
"""
Classes in Python can implement certain operations with special method names.

Special Methods allow to perform special operations.

Special Methods are not called directly, but they are called by Python specific language syntax.

They allow us to use Python specific functions on objects created through our class
"""

mylist = [1,2,3]
print(mylist)

class Book():
    
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b = Book('MyPythonBook','Elisa',400)
print(b)
# it prints <__main__.Book object at 0x7fe688b5a0f0>
# But how can I print something nicer?
"""
NB: when you call "print" on an Object, it looks for its ^string representation^
but we haven't define the Book's string representation!

You need to use a Special Method to do that!!

All Special Methods are annotated among underscores:
"""
class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #- this is the string representation of my object
    #- so whenever a function calls for the string representation of my object
    #- it will return what you define it to return
    def __str__(self):
        # "Title: %s, author: %s, pages: %s " %(self.title, self.author, self.pages)
        return "Title: {}, author: {}, pages: {}".format(self.title, self.author, self.pages)

b = Book('MyPythonBook','Elisa',400)
print(b)

#= OTHER USEFUL SPECIAL METHODS

class Book():

    def __init__(self, title, author, pages):
        print('A book is created')
        self.title = title
        self.author = author
        self.pages = pages

    #- SPECIAL METHOD: the string representation method
    def __str__(self):
        return "Title: {}, author: {}, pages: {}".format(self.title, self.author, self.pages)

    #- SPECIAL METHOD: the length method
    def __len__(self):
        return self.pages

    #- SPECIAL METHOD: the delete method
    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

#Special Methods
print(book)
print(len(book))
del(book)

"""
For more great resources on this topic, check out:
[Jeff Knupp's Post](https://www.jeffknupp.com/blog/2014/06/18/improve-your-python-python-classes-and-object-oriented-programming/)
[Mozilla's Post](https://developer.mozilla.org/en-US/Learn/Python/Quickly_Learn_Object_Oriented_Programming)
[Tutorial's Point](http://www.tutorialspoint.com/python/python_classes_objects.htm)
[Official Documentation](https://docs.python.org/2/tutorial/classes.html)
"""

