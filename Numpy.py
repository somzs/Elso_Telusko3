from numpy import *
# A NumPy nyílt forráskódú kiegészítő csomag a Python programozási nyelvhez,
# mely a nagy, többdimenziós tömbök és mátrixok használatát támogatja egy nagy
# magas szintű matematikai függvénykönyvtárral.
arr = array([1,2,3],int)
print(arr)

# creating arrays in Numpy
# 6 ways: array(), linspace(),logspace(),arange(),zeros(),ones()

arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr = array([1,2,3,4,5.0])
print(arr)
print(arr.dtype)
# minden értékből float lesz

arr2 = linspace(0,2,6) # [0.  0.4 0.8 1.2 1.6 2. ]
print(arr2)

arr3 = arange(1,15,2)
print(arr3)

arr4 = logspace(1,40,5)
print(arr4)
print('%.2f' %arr[2])

arr5 = zeros(5) # float values
print(arr5)

arr6 = ones(6) # float values
print(arr6)

arr7 = zeros(5,int) # float values
print(arr7)

arr8 = ones(6,int) # float values
print(arr8)

# copy an array
arrtocopy1 = array([1,2,3,4,5])
arrtocopy1 = arrtocopy1 + 5
print(arrtocopy1)    # [ 6  7  8  9 10]

arrtocopy2 = array([6,1,9,3,2])
arrtocopy3 = arrtocopy1 + arrtocopy2 # vectorized operation
print(arrtocopy3)    # [12  8 17 12 12]
print(cos(arrtocopy3))
print(sqrt(arrtocopy3))

arrtocopy4 = concatenate([arrtocopy1,arrtocopy2])
print(arrtocopy4)   # [ 6  7  8  9 10  6  1  9  3  2]

arrtocopy1 = arrtocopy2 # ha igy csinálom, akkor az ID azonos marad, ezért:
arrtocopy2 = arrtocopy1.view()
arrtocopy1[4] = 20 # ezért kell a copy-t használni, hogy ne mindkettőben változzon ez az érték:
arrtocopy2 = arrtocopy1.copy()
arrtocopy1[3] = 40
print(arrtocopy2)

