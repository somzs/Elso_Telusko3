import math
# 1. you can import it with other name:
# for example: import math as m
# 2. if you use this importing method then math. is not needed:
# for example: from math import sqrt - call: print(sqrt(25))

#Python Bitwise Operators
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left,
# and let the rightmost bits fall off

# a = 0011 1100
# b = 0000 1101
# a&b = 0000 1100
# a|b = 0011 1101
# a^b = 0011 0001
# ~a  = 1100 0011

a = 5
print(bin(a)) # 101
b = 6
print(bin(b)) # 110
a = a ^ b
print(a)
print(bin(a)) # 11

#swap
a = 4
b = 5
print(a,b)
a,b = b,a
print(a,b)

# if math is imported
print(math.sqrt(25))
# math.ceil(x)
# Return the ceiling of x as a float, the smallest integer value greater than or equal to x.

# math.floor(x)
# Return the floor of x as a float, the largest integer value less than or equal to x.

# math.pow(x, y)
# Return x raised to the power y.

# math.pi

# math.e