class A:
    def feature1(self):
        print("Feature 1")

    def feature2(self):
        print("Feature 2")


a1 = A()
a1.feature1()
a1.feature2()


class B(A):  # child / sub class
    def feature3(self):
        print("Feature 3")

    def feature4(self):
        print("Feature 4")


b1 = B()
b1.feature1()
b1.feature2()
b1.feature4()
b1.feature4()


# multilevel inheritence
class C(B):
    def feature5(self):
        print("Feature 5")


c1 = C()
c1.feature1()


# inheritance from more classes:
class D(B, A):
    def feature6(self):
        print("Feature 6")


d1 = D()
d1.feature1()


# Constructor in inheritance
# method resolution order (MRO)

class E:

    def __init__(self):
        print("E init")

    def feature10(self):
        print("Feature 10")

    def feature11(self):
        print("Feature 11")


class F(E):  # child / sub class

    def __init__(self):
        super().__init__()  # super(): ilyenkor lefut az ősosztály init metódusa is, akkor is ha az alosztályban is van
        print("F init")

    def feature12(self):
        print("Feature 12")

    def feature13(self):
        print("Feature 13")


e1 = E()  # E init
e1.feature10()
e1.feature11()

f1 = F()  # F init


# if you create object of Sub class it will first try find init of Sub class
# if it is not found then

class G():  # child / sub class

    def __init__(self):
        super().__init__()  # super(): ilyenkor lefut az ősosztály init metódusa is, akkor is ha az alosztályban is van
        print("G init")

    def feature12(self):
        print("Feature 14")

    def feature15(self):
        print("Feature 15")
class H(E,G):
    def __init__(self):
        super().__init__()    # method resolution order
        # method resolution order defines the order in which the base classes are searched when executing a method
        print("H init")

    def feat(self):
        super().feature10()

print("H")
h1 = H()
h1.feat()
