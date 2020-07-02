# OOPs object oriented programming

class Computer:
     '''define variable in class
    _init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts.\
    This method called when an object is created from the class and
    it allow the class to initialize the attributes of a class.'''

     def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram

     def config(self):
        print("Config is ", self.cpu, self.ram);


a = '8'
x = 9
com1: Computer = Computer('i5', 16)
com2: Computer = Computer('Ryzen 3',8)

print(type(com1)) # <class '__main__.Computer'>
print(type(a)) # <class 'str'> in-built class
print(type(x)) # <class 'int'> in-built class

Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()

a = 5
a.bit_length()

# _init__ method
