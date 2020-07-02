# search an element in a list
# search 9

""""
age = 23

globals()['age'] = 25
print('The age is:', age)

Result:

The age is: 25
"""

pos = -1


def search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True;
        i = i + 1
    return False;


list = [3, 7, 8, 12, 45, 99]
n = 12

if search(list, n):
    print("Found at ", pos + 1)
else:
    print("Not found")

""""
Binary search
Python Program for Binary Search (Recursive and Iterative)
In a nutshell, this search algorithm takes advantage of a collection of elements that is already sorted
by ignoring half of the elements after just one comparison.

Compare x with the middle element.
If x matches with the middle element, we return the mid index.
Else if x is greater than the mid element, then x can only lie in the right (greater) half subarray
after the mid element. Then we apply the algorithm again for the right half.
Else if x is smaller, the target x must lie in the left (lower) half. So we apply the algorithm for the left half.
"""

pos = -1


def search2(list2, n2):
    l = 0
    u = len(list2) - 1
    while l <= u:
        mid = (l + u) // 2
        if list2[mid] == n2:
            globals()['pos'] = mid
            return True
        else:
            if list2[mid] < n2:
                l = mid;
            else:
                u = mid;
    return False


list2 = [4, 7, 8, 12, 45, 99]
n2 = 4

if search2(list2, n2):
    print("Found at ", pos + 1)
else:
    print("Not found")

""""
Binary Search (bisect) in Python
Binary Search is a technique used to search element in a sorted list. In this article, 
we will looking at library functions to do Binary Search.

Finding first occurrence of an element.

bisect.bisect_left(a, x, lo=0, hi=len(a)) : 
Returns leftmost insertion point of x in a sorted list. Last two parameters are optional, 
they are used to search in sublist.


brightness_4
# Python code to demonstrate working 
# of binary search in library 
"""

from bisect import bisect_left


def BinarySearch(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1


a = [1, 2, 4, 4, 8]
x = int(4)
res = BinarySearch(a, x)
if res == -1:
    print(x, "is absent")
else:
    print("First occurrence of", x, "is present at", res)
