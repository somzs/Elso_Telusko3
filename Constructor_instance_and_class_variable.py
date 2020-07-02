# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class
# when an object of class is created.In Python the __init__() method is called the constructor
# and is always called when an object is created.

class Computer:
    def __init__(self):
        self.name = "Zsuzsi"
        self.age = 37

    def update(self):
        self.age = "40"

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()  # it is in the Heap memory
c2 = Computer()  # it is in the Heap memory

print(id(c1))
print(id(c2))
# minden futtatásnál más az id értéke

c2.name = "Marci"
c2.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)

# comparing two objects
if c1 == c2:
    print("They are same")
else:
    print("They are different")

if c1.compare(c2):
    print("They are same")
else:
    print("They are different")


class Car:
    # class variable:
    wheels = 4  # common for all objects

    # instance variables:
    def __init__(self):
        self.mil = 10  # instance namespace
        self.company = "BMW"


c1 = Car()
c2 = Car()

print(c1.mil, c1.company)
print(c2.mil, c2.company)

c1.mil = 8
print(c1.mil, c1.company, c1.wheels)
print(c2.mil, c2.company, c2.wheels)

Car.wheels = 5
print(c1.mil, c1.company, c1.wheels)
print(c2.mil, c2.company, c2.wheels)
