f = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'r')  # r: reading
print(f.read())
f2 = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'r')  # r: reading
print(f2.readline(), end = "")  # it prints only the first line
print(f2.readline())
f3 = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'w')  # w: writing - overwrite
f3.write("meggy") # overwrites the files
f4 = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'a')  # a: writing - append
f4.write(", cseresznye") # append
f5 = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'r')
print(f5.read())

# copy data into another file
# How do we know that we have copied everything?

f = open('c:\Zsuzsi\Python_programozas\gyümölcsök1.txt', 'r')   # the copied file
f6 = open('c:\Zsuzsi\Python_programozas\gyümölcsök.txt', 'w')

for data in f:
    f6.write(data)

# copy an image

f = open('c:\Zsuzsi\Python_programozas\dacia.jpg', 'rb')    # read binary
f1 = open('c:\Zsuzsi\Python_programozas\dacia_copied.jpg', 'wb')

for i in f:
    f1.write(i)

# copy a pdf file

f = open('c:\Zsuzsi\Python_programozas\szerzodes.pdf', 'rb')    # read binary
f1 = open('c:\Zsuzsi\Python_programozas\szerzodes2.pdf', 'wb')

for i in f:
    f1.write(i)