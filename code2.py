from threading import *
from time import *
class a(Thread):
    def run(self):
        for p in range (10):
            print("a")
            sleep(1)

class b(Thread):   
    def run(self):
        for q in range (10):
            print("b")
            sleep(1)


x = a()
y = b()
x.start()
sleep(0.5)
y.start()
x.join()
y.join()
print("output was obtained")
