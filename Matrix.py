from numpy import *
arr1 = array ([
                [1,2,3],
                [4,5,6]
                ])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)   # (2, 3)
print(arr1.size)    # 6
arr2 = arr1. flatten()
print(arr2) # [1 2 3 4 5 6]
arr3 = arr2.reshape(3,2)
print(arr3)
arr4 = array ([
                [1,2,3,6]
                [4,5,6,7]
                ])



