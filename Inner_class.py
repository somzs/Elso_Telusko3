# outer class

class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

# inner class
    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = '8'
        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student("Zsuzsi", 2)  # instance variable
s2 = Student("Marci", 3)

s1.show()
s2.show()

lap1 = s1.lap.brand
lap2 = s2.lap

print('1')
print(lap1)
print('2')
print(lap2)

# you can create object of inner class inside the outer class or
# outside the outer class provided you use the outer class name to call it
lap1 = Student.Laptop()
lap2 = Student.Laptop().brand
print('3')
print(lap1)
print('4')
print(lap2)