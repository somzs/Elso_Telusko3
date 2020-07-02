""""Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable
Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator.

Example
Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

Example
Iterate the values of a tuple

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

Example
Iterate the characters of a string:
mystr = "banana"

for x in mystr:
  print(x)
"""

nums = [7, 8, 9, 5]
print(nums[3])

for i in nums:
    print(i)

it = iter(nums)
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
print(it.__next__())


# create my own iterator, class, object

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = TopTen()

print(next(values))

for i in values:
    print(i)