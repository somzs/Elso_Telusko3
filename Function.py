def update(x):
    x = 8
    print("x: ", x)

update(10)
x = 7
update(x)
a = 10
update(a)   # 8, de más az id(x)!
# pass by value; pass by reference

list = [10,20]

a = 10
def change_variable():
    global a # emiatt változik meg a globáis változó
    a = 15
    print("function a: ", a)

change_variable()
print("global: ",a)

# igy is lehet - összes gobális:

b = 7
c = 8
def change_variable2():
    x = globals()
#   c = 5
    print("function c: ", c)

change_variable2()
print("global: ",c)

# pass list to a function
def count(list):

    even = 0
    odd = 0

    for i in list:
        if i%2 == 0:
            even +=1
        else:
            odd +=1
    return even, odd

list = [34,45,35,67,88,9,89]
even, odd = count(list)
print("Even: {} and odd: {}".format(even,odd))