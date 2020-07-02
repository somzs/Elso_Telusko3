from array import *

# array with array module: all elements must be of the same numeric type
# list: we cannot constrain the type of elements

vals = array('i',[5,9,8,4,2]) # int
newArr = array(vals.typecode,(a for a in vals))
# newArr = array(vals.typecode,(a*a for a in vals)) - művelet is lehet benne: ld. a*a
vals2 = array ('u', ['a','e','i'])
print(vals)
print(vals.buffer_info())
print(vals.typecode)
print(vals[0])
vals.reverse()
print(vals[0])

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

for e in vals2:
    print(e)

for e in newArr:
    print(e)

i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1

# I want to add elements:
arr = array("i",[])
n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)
print(arr)
# I add a value and it gives back the index:
val = int(input("Enter the value for search: "))
k = 0
for e in arr:
    if e == val:
        print(k)
        break
    k+=1

print(arr.index(val))






