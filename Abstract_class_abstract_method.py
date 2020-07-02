# abstract classes:
# Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
# A class that is derived from an abstract class cannot be instantiated
# unless all of its abstract methods are overridden.

from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("it is running")


# mi van, ha nincs statement?
# print("running") helyett pass

# com = Computer()
com1 = Laptop()
# com.process()
com1.process()

"""class AbstractClass:

     def do_something(self):
       # pass

class B(AbstractClass):
    pass

a = AbstractClass()
b = B()
this is not an abstract class , because:
we can instantiate an instance from we are not required to implement do_something in the class defintition of B"""


class Whiteboard():
    def write(self):
        print("it is writing")


class Programmer:
    def work(self, com):
        print("solving bugs")
        com.process()


prog1 = Programmer()
com2 = Whiteboard()
prog1.work(com1)

"""Abstract Classes in Python
An abstract class can be considered as a blueprint for other classes. It allows you to create a set of methods 
that must be created within any child classes built from the abstract class. A class which contains one or more 
abstract methods is called an abstract class. An abstract method is a method that has a declaration but does not have
an implementation. While we are designing large functional units we use an abstract class. When we want to provide 
a common interface for different implementations of a component, we use an abstract class.
 
Why use Abstract Base Classes :
By defining an abstract base class, you can define a common Application Program Interface(API) for a set of subclasses.
 This capability is especially useful in situations where a third-party is going to provide implementations, 
 such as with plugins, but can also help you when working in a large team or with a large code-base where keeping all
  classes in your mind is difficult or not possible.
 
How Abstract Base classes work :
By default, Python does not provide abstract classes. Python comes with a module which provides the base for defining
 Abstract Base classes(ABC) and that module name is ABC. 
ABC works by decorating methods of the base class as abstract and then registering concrete classes as implementations
 of the abstract base. A method becomes abstract when decorated with the keyword @abstractmethod. 

# Python program showing 
# abstract base class work 
  
from abc import ABC, abstractmethod 
  
class Polygon(ABC): 
  
    # abstract method 
    def noofsides(self): 
        pass
  
class Triangle(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 3 sides") 
  
class Pentagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 5 sides") 
  
class Hexagon(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 6 sides") 
  
class Quadrilateral(Polygon): 
  
    # overriding abstract method 
    def noofsides(self): 
        print("I have 4 sides") 
  
# Driver code 
R = Triangle() 
R.noofsides() 
  
K = Quadrilateral() 
K.noofsides() 
  
R = Pentagon() 
R.noofsides() 
  
K = Hexagon() 
K.noofsides()

Output:

I have 3 sides
I have 4 sides
I have 5 sides
I have 6 sides """