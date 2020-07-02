# syntax error - compile time error
# logical error - wrong output
# run time error - for example divide by zero

a = 5
b = 2



try:
    print("resource open")
    print(a/b)  # if there is an error it jumps out of this block
    k = int(input("Enter a number: "))
    print(k)

# except Exception as e:   # it will be executed if there is an error
except ZeroDivisionError as e:   # it will be executed if there is an error
    print("You cannot divide a number by zero", e)

except ValueError as e:
    print("invalid input")

except Exception as e:
    print("something went wrong")

finally:
    print("resource closed")    # it will be executed always
print("Bye")

