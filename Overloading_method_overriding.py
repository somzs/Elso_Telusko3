# type of polymorphism:
# 1: overriding: the method has the same name, the arguments are also the same
# 2: overloading: the method has the same name, but the arguments are different

# method overloading:


class Student():
    def __int__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None): # default values
        s = 0
        if a!=None and b!=None and c!=None:
            s = a + b + c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s

s1 = Student()

print(s1.sum(13,16,2))
print(s1.sum(13,16))


# method overriding:

class A:
    def show(self):
        print("Show A")

class B(A):
    def show(self):
        print("Show B")
# ha itt pass lenne csak, akkor Show A-t tudná kiírni, de mivel a B-ben is van, ezért felülírja az örököltet

a1 = B()
a1.show() # B inherits from A
