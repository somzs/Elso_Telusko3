import sys
# Fibonacci-sorozat
def fibonacci(c):
    x = 0
    y = 1
    i = 2
    if c == 1:
        print(x)
    else:
        print(x)
        print(y)
        while i < c:
            n = x + y
            print(n)
            b = y
            y = x + y
            x = b
            i += 1
fibonacci(5)

# recurson
print(sys.getrecursionlimit()) # 1000
sys.setrecursionlimit(3000)
print(sys.getrecursionlimit()) # 1000
i = 0
def reggel():
    global i
    i += 1
    print("Szia Marci" , "i: ", i)
    reggel()
reggel()