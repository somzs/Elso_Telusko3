# Polymorphism (many forms) is a very important concept in programming. It refers to the use of a single type entity (method,
# operator or object) to represent different types in different scenarios.

# Polymorphism with Inheritance: In Python,
# Polymorphism lets us define methods in the child class that have the same name as the methods in the parent class.
# In inheritance, the child class inherits the methods from the parent class. However, it is possible to modify a
# method in a child class that it has inherited from the parent class. This is particularly useful in cases where the
# method inherited from the parent class doesn’t quite fit the child class. In such cases, we re-implement the method
# in the child class. This process of re-implementing a method in the child class is known as Method Overriding.

# A single operator + has been used to carry out different operations for distinct data types. This is one of the
# most simple occurrences of polymorphism in Python.

# 1. Duck typing
# 2. operator overloading
# 3. method overloading
# 4. method overriding

# 1. Duck typing Duck typing is a concept related to dynamic typing, where the type or the class of an object is less
# important than the methods it defines. When you use duck typing, you do not check types at all. Instead,
# you check for the presence of a given method or attribute.

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")


class Laptop:
    def code(self, ide):
        ide.execute()

ide = PyCharm()

lap1 = Laptop()
lap1.code(ide)

ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)
