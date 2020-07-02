
from functools import reduce
def is_even(n):
    return n%2 == 0
nums = [2,3,4,5,3,5,6,7]
# Return value from filter()
# The filter() method returns an iterator that passed the function check for each element in the iterable.
#
# The filter() method is equivalent to:
#
# # when function is defined
# (element for element in iterable if function(element))
#
# # when function is None
# (element for element in iterable if element)
evens = list(filter(is_even,nums))
print(evens)

# lambda
x = lambda a : a + 10
print(x(5))

# a fenti filter lambdával, függvény nélkül
evens = list(filter(lambda n: n % 2 == 0,nums))
print(evens)

# map(function, iterables)
def update(n):
    return n+2
doubles = list(map(lambda n: n + 2,evens))
print(doubles)

# reduce() in Python
# The reduce(fun,seq) function is used to apply a particular function passed in its argument
# to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
#
# Working :
#
# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result
# and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.
def add_all(a,b):
    return a + b
sum = reduce(add_all,doubles)
print(sum)
sum = reduce(lambda a,b : a + b,doubles)
print(sum)

# decorator
# Decorators are very powerful and useful tool in Python since it allows programmers to modify
# the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior
# of wrapped function, without permanently modifying it.
# In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.
def div(a, b):
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return func(a,b)
    return inner
div = smart_div(div)
div(2, 4)