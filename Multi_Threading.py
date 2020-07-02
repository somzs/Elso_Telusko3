from time import sleep
from threading import *

# multi threading: több függvény fusson párhuzamosan és az eredmények felváltva jelenjenek meg

class Hello:
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Hi:
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)


t1 = Hello()
t2 = Hi()

t1.run()
t2.run()


# result:

# Hello
# Hello
# Hello
# Hello
# Hello
# Hi
# Hi
# Hi
# Hi
# Hi

# How could we execute the two function in the same time?

class Hello2(Thread):
    def run(self):
        for i in range(5):
            print("Hello2")
            sleep(1)


class Hi2(Thread):
    def run(self):
        for i in range(5):
            print("Hi2")
            sleep(1)


t3 = Hello2()
t4 = Hi2()

t3.start()
sleep(0.2)
t4.start()

t3.join()
t4.join()

print("Bye") # akkor fut le, amikor a másik két szál már véget ér, mert ott van a join()

# we have to give a schedule, because the system is too fast
