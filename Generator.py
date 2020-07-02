# Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

"""There is a lot of work in building an iterator in Python.
We have to implement a class with __iter__() and __next__() method, keep track of internal states,
and raise StopIteration when there are no values to be returned.

This is both lengthy and counterintuitive. Generator comes to the rescue in such situations.

Python generators are a simple way of creating iterators. All the work we mentioned above are automatically handled by
generators in Python.

Simply speaking, a generator is a function that returns an object (iterator)
which we can iterate over (one value at a time)."""


def topten():
    yield 1
    yield 2
    yield 3
    yield 4  # generator


values = topten()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)


def topten2():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


values2 = topten2()

for i in values2:
    print(i)

"""The difference is that while a return statement terminates a function entirely, yield statement pauses the 
function saving all its states and later continues from there on successive calls. """
